#!/usr/bin/env python3
"""Builds the Word and PDF editions of the documentation with WordCraft.

    python3 tools/build.py                 # every document, both languages
    python3 tools/build.py --lang it --doc user-manual

Pipeline, per document and language (src/<lang>/<doc>.md):
  1. diagrams: src/img/<name>.<lang>.svg (tools/diagrams.py) are rasterised with ImageMagick;
  2. Markdown is prepared (title block, heading levels, figure markers, wide tables as lists);
  3. `wordcraft-cli convert` turns it into a Word document;
  4. `wordcraft-cli run` styles it (A4, fonts, headings, tables, code), inserts the pictures,
     builds the table of contents, adds the header and footer, and saves
     dist/<lang>/<doc>.docx and dist/<lang>/<doc>.pdf.

Needs: wordcraft-cli (WordCraft), ImageMagick (`magick`), the Inter and Liberation Mono fonts.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SRC = os.path.join(ROOT, "src")
DIST = os.path.join(ROOT, "dist")
BUILD = os.path.join(ROOT, ".build")

DOCS = ["user-manual", "developer-guide", "architecture", "sources"]
LANGS = ["en", "it"]

ACCENT = "1F4E99"
INK = "1B2530"
MUTED = "5E6B73"

T = {
    "en": {"contents": "Contents", "page": "Page ", "of": " of ", "header": "DentalCraft"},
    "it": {"contents": "Indice", "page": "Pagina ", "of": " di ", "header": "DentalCraft"},
}


def run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        sys.stderr.write(f"command failed: {' '.join(cmd)}\n{r.stdout}\n{r.stderr}\n")
        raise SystemExit(1)
    return r


# ---------------------------------------------------------------------------
# Markdown preparation
# ---------------------------------------------------------------------------
def split_row(line: str) -> list[str]:
    """Splits a pipe-table row, honouring escaped pipes and pipes inside code spans."""
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    cells, cur, in_code, i = [], "", False, 0
    while i < len(s):
        ch = s[i]
        if ch == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            cur += "\\|"
            i += 2
            continue
        if ch == "`":
            in_code = not in_code
        if ch == "|" and not in_code:
            cells.append(cur.strip())
            cur = ""
        else:
            cur += ch
        i += 1
    cells.append(cur.strip())
    return cells


def table_to_list(header: list[str], rows: list[list[str]]) -> list[str]:
    """Wide bibliography tables become one entry per row: far more readable on an A4 page."""
    out = []
    for cells in rows:
        cells = cells + [""] * (len(header) - len(cells))
        cells = [c.replace("<br>", " · ") for c in cells]
        if len(header) >= 6 and header[1].lower() in ("year", "anno"):
            authors, year, title, venue, doi, used = cells[:6]
            line = f"**{authors}** ({year}). {title}."
            if venue:
                line += f" {venue}."
            if doi:
                line += f" {doi}"
            if used:
                line += f" — *{header[5].replace('`', '')}:* {used}"
        else:
            parts = [f"**{cells[0]}**"]
            for i in range(1, len(header)):
                if cells[i]:
                    parts.append(f"*{header[i].replace('`', '')}:* {cells[i]}")
            line = " · ".join(parts)
        out.append("- " + line)
    return out


def prepare(md: str, bibliography: bool = False) -> tuple[str, str, list[dict]]:
    """Returns (markdown for WordCraft, document title, figures)."""
    lines = md.split("\n")
    out: list[str] = []
    figures: list[dict] = []
    title = ""
    in_code = False
    toc_done = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            in_code = not in_code
            out.append(line)
            i += 1
            continue
        if in_code:
            out.append(line)
            i += 1
            continue
        m = re.match(r"^# (.*)$", line)
        if m and not title:
            title = m.group(1).strip()
            out.append(title)
            i += 1
            continue
        m = re.match(r"^(#{2,6}) (.*)$", line)
        if m:
            if not toc_done:
                out.append("[[TOC]]")
                out.append("")
                toc_done = True
            out.append("#" * (len(m.group(1)) - 1) + " " + m.group(2))
            i += 1
            continue
        m = re.match(r"^!\[(.*)\]\((.*)\)\s*$", line)
        if m:
            n = len(figures) + 1
            figures.append({"n": n, "alt": m.group(1), "src": m.group(2)})
            out.append(f"[[FIG:{n}]]")
            i += 1
            continue
        if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|\s*$", lines[i + 1]):
            header = split_row(line)
            j = i + 2
            rows = []
            while j < len(lines) and lines[j].startswith("|"):
                rows.append(split_row(lines[j]))
                j += 1
            if len(header) >= 5 or (bibliography and len(header) >= 4):
                out.extend(table_to_list(header, rows))
            else:
                out.extend(lines[i:j])
            i = j
            continue
        out.append(line)
        i += 1
    return "\n".join(out) + "\n", title, figures


# ---------------------------------------------------------------------------
# Diagrams
# ---------------------------------------------------------------------------
def rasterise(svg: str, png: str) -> None:
    if os.path.exists(png) and os.path.getmtime(png) >= os.path.getmtime(svg):
        return
    run(["magick", "-density", "192", "-background", "white", svg, "-flatten", png])


# ---------------------------------------------------------------------------
# WordCraft script
# ---------------------------------------------------------------------------
def pos(block: int, off: int = 0, path: list[int] | None = None) -> dict:
    return {"story": "body", "path": path if path is not None else [block], "off": off}


def sel_block(block: int, length: int) -> dict:
    return {"command": "select.range", "params": {"anchor": pos(block, 0), "focus": pos(block, length)}}


def utf8len(s: str) -> int:
    return len(s.encode("utf-8"))


OPTIONAL_STYLES = {"Heading2", "Heading3", "Heading4", "ListParagraph", "Code", "Quote"}


def style_commands(used: set[str]) -> list[dict]:
    c = lambda command, **params: {"command": command, "params": params}  # noqa: E731
    cmds = [
        c("layout.size", name="A4"),
        c("layout.margins", top=64, bottom=64, left=62, right=62),
        c("design.themeFonts", heading="Inter", body="Inter"),
        c("styles.modify", style="Normal", chr={"font": "Inter", "size": 10, "color": INK}, para={"spaceAfter": 6}),
        c("styles.modify", style="Title", chr={"font": "Inter", "size": 30, "bold": True, "color": "0B2A5B"}, para={"spaceBefore": 8, "spaceAfter": 8}),
        c("styles.modify", style="Heading1", chr={"font": "Inter", "size": 19, "bold": True, "color": ACCENT},
          para={"spaceBefore": 24, "spaceAfter": 8, "keepNext": True}),
        c("styles.modify", style="Heading2", chr={"font": "Inter", "size": 14, "bold": True, "color": ACCENT},
          para={"spaceBefore": 16, "spaceAfter": 5, "keepNext": True}),
        c("styles.modify", style="Heading3", chr={"font": "Inter", "size": 11.5, "bold": True, "color": INK},
          para={"spaceBefore": 12, "spaceAfter": 4, "keepNext": True}),
        c("styles.modify", style="Heading4", chr={"font": "Inter", "size": 10.5, "bold": True, "color": INK},
          para={"spaceBefore": 10, "spaceAfter": 3, "keepNext": True}),
        c("styles.modify", style="ListParagraph", chr={"font": "Inter", "size": 10}, para={"spaceAfter": 3}),
        c("styles.modify", style="Code", chr={"font": "Liberation Mono", "size": 8.5, "color": INK},
          para={"spaceAfter": 0, "shading": "F1F3F5", "indentLeft": 4}),
        c("styles.modify", style="Quote", chr={"font": "Inter", "size": 10, "italic": False, "color": "4A2C00"},
          para={"align": "left", "shading": "FFF3DC", "indentLeft": 6, "indentRight": 6, "spaceBefore": 8, "spaceAfter": 12}),
        c("styles.modify", style="Hyperlink", chr={"color": ACCENT}),
        c("styles.modify", style="TOC1", chr={"font": "Inter", "size": 9, "bold": True}, para={"spaceBefore": 3, "spaceAfter": 0}),
        c("styles.modify", style="TOC2", chr={"font": "Inter", "size": 8, "bold": False}, para={"spaceBefore": 0, "spaceAfter": 0}),
    ]
    # styles WordCraft creates only when the document uses them
    return [x for x in cmds if x["params"].get("style") not in OPTIONAL_STYLES or x["params"]["style"] in used]


def build_one(lang: str, doc: str) -> None:
    md_path = os.path.join(SRC, lang, f"{doc}.md")
    if not os.path.exists(md_path):
        raise SystemExit(f"missing {md_path}")
    work = os.path.join(BUILD, lang)
    os.makedirs(work, exist_ok=True)
    os.makedirs(os.path.join(DIST, lang), exist_ok=True)
    text = open(md_path, encoding="utf-8").read()
    tmp_md, title, figures = prepare(text, bibliography=(doc == "sources"))
    tmp_md_path = os.path.join(work, f"{doc}.md")
    tmp_docx = os.path.join(work, f"{doc}.docx")
    open(tmp_md_path, "w", encoding="utf-8").write(tmp_md)
    run(["wordcraft-cli", "convert", tmp_md_path, tmp_docx])

    for f in figures:
        src = os.path.normpath(os.path.join(SRC, lang, f["src"]))
        if src.endswith(".svg"):
            png = os.path.join(work, os.path.basename(src)[:-4] + ".png")
            rasterise(src, png)
            f["png"], f["width"] = png, 460
        else:
            f["png"], f["width"] = src, 430

    info = json.loads(run(["wordcraft-cli", "inspect", tmp_docx]).stdout)
    blocks = info["blocks"]
    cmds = style_commands({b.get("style") for b in blocks if b.get("type") == "paragraph"})

    # block 0 is the title, block 1 the italic line under it
    cmds += [sel_block(0, utf8len(blocks[0]["text"])), {"command": "para.style", "params": {"style": "Title"}}]
    if len(blocks) > 1 and blocks[1].get("type") == "paragraph":
        cmds += [sel_block(1, utf8len(blocks[1]["text"])),
                 {"command": "format.color", "params": {"color": MUTED}},
                 {"command": "format.size", "params": {"size": 10.5}}]

    # tables: light borders, shaded bold header row, repeated on every page
    for b in blocks:
        if b.get("type") != "table":
            continue
        i, rows, cols = b["index"], b["rows"], b["cols"]
        last = {"story": "body", "path": [i, rows - 1, cols - 1, 0], "off": utf8len(b["cells"][rows - 1][cols - 1])}
        first = {"story": "body", "path": [i, 0, 0, 0], "off": 0}
        cmds += [
            {"command": "select.range", "params": {"anchor": first, "focus": last}},
            {"command": "table.borders", "params": {"kind": "all", "width": 0.5, "color": "C3CBD3"}},
        ]
        weights, minw = [], []
        for c_ in range(cols):
            texts = [row[c_] for row in b["cells"]]
            longest = max((len(t) for t in texts), default=6)
            weights.append(min(max(longest, 8), 420) ** 0.55)
            token = max((len(tok) for t in texts for tok in t.split()), default=4)
            minw.append(min(215.0, token * 5.0 + 14))
        total_w = 471.0
        widths = [max(minw[c_], total_w * weights[c_] / sum(weights)) for c_ in range(cols)]
        excess = sum(widths) - total_w
        if excess > 0:
            flex = [widths[c_] - minw[c_] for c_ in range(cols)]
            if sum(flex) > 0:
                widths = [widths[c_] - excess * flex[c_] / sum(flex) for c_ in range(cols)]
        for c_ in range(cols):
            w = max(44.0, widths[c_])
            cell = {"story": "body", "path": [i, 0, c_, 0], "off": 0}
            cmds += [
                {"command": "select.range", "params": {"anchor": cell, "focus": cell}},
                {"command": "table.columnWidth", "params": {"width": round(w, 1)}},
            ]
        cmds += [
            {"command": "select.range", "params": {"anchor": first, "focus": last}},
            {"command": "table.autofit", "params": {"mode": "fixed"}},
            {"command": "para.spacing", "params": {"before": 2, "after": 2}},
            {"command": "format.size", "params": {"size": 9}},
            {"command": "para.alignLeft", "params": {}},
            {"command": "select.range", "params": {"anchor": first, "focus": {"story": "body", "path": [i, 0, cols - 1, 0], "off": utf8len(b["cells"][0][cols - 1])}}},
            {"command": "table.shading", "params": {"color": "E3ECFA"}},
            {"command": "format.bold", "params": {}},
            {"command": "table.repeatHeader", "params": {}},
        ]
        nxt = blocks[i + 1] if i + 1 < len(blocks) else None
        if nxt and nxt.get("type") == "paragraph" and nxt.get("style") == "Normal" and nxt.get("text"):
            cmds += [sel_block(i + 1, utf8len(nxt["text"])), {"command": "para.spacing", "params": {"before": 8}}]

    # figures: replace the marker paragraph with the picture, centre it, style its caption
    by_text = {b["text"]: b for b in blocks if b.get("type") == "paragraph" and b.get("text")}
    for f in figures:
        b = by_text.get(f"[[FIG:{f['n']}]]")
        if not b:
            raise SystemExit(f"{doc} ({lang}): marker of figure {f['n']} not found")
        idx = b["index"]
        cmds += [
            sel_block(idx, utf8len(b["text"])),
            {"command": "text.delete", "params": {}},
            {"command": "insert.picture", "params": {"path": f["png"], "width": f["width"], "alt": f["alt"]}},
            {"command": "para.alignCenter", "params": {}},
            {"command": "para.keepNext", "params": {}},
            {"command": "para.spacing", "params": {"before": 6, "after": 4}},
        ]
        if idx + 1 < len(blocks) and blocks[idx + 1].get("type") == "paragraph" and blocks[idx + 1].get("text"):
            cap = blocks[idx + 1]
            cmds += [
                sel_block(idx + 1, utf8len(cap["text"])),
                {"command": "para.alignCenter", "params": {}},
                {"command": "format.size", "params": {"size": 9}},
                {"command": "format.color", "params": {"color": MUTED}},
                {"command": "para.spacing", "params": {"before": 0, "after": 12}},
            ]

    # the first chapter starts a new page, after the title block and the contents
    first_chapter = next((b for b in blocks if b.get("style") == "Heading1"), None)
    if first_chapter:
        cmds += [
            {"command": "select.range", "params": {"anchor": pos(first_chapter["index"], 0), "focus": pos(first_chapter["index"], 0)}},
            {"command": "para.pageBreakBefore", "params": {"value": True}},
        ]

    # table of contents, in place of its marker (last: it adds paragraphs)
    toc = by_text.get("[[TOC]]")
    if toc:
        cmds += [
            sel_block(toc["index"], utf8len("[[TOC]]")),
            {"command": "text.delete", "params": {}},
            {"command": "references.toc", "params": {"levels": 2, "title": T[lang]["contents"]}},
        ]

    # header and footer; the title page has none (different first page is set once both exist)
    cmds += [
        {"command": "insert.header", "params": {"text": f"{T[lang]['header']}  |  {title}"}},
        {"command": "para.alignRight", "params": {}},
        {"command": "format.size", "params": {"size": 8}},
        {"command": "format.color", "params": {"color": MUTED}},
        {"command": "insert.closeHeader", "params": {}},
        {"command": "insert.footer", "params": {"text": T[lang]["page"]}},
        {"command": "caret.end", "params": {}},
        {"command": "insert.field", "params": {"instr": "PAGE", "result": "1"}},
        {"command": "text.insert", "params": {"text": T[lang]["of"]}},
        {"command": "insert.field", "params": {"instr": "NUMPAGES", "result": "1"}},
        {"command": "para.alignCenter", "params": {}},
        {"command": "format.size", "params": {"size": 8}},
        {"command": "format.color", "params": {"color": MUTED}},
        {"command": "insert.closeHeader", "params": {}},
        {"command": "layout.differentFirstPage", "params": {}},
        {"command": "file.properties", "params": {"title": title, "subject": "DentalCraft", "keywords": "DentalCraft, aligners"}},
        {"command": "references.updateFields", "params": {"all": True}},
    ]

    out_docx = os.path.join(DIST, lang, f"{doc}.docx")
    out_pdf = os.path.join(DIST, lang, f"{doc}.pdf")
    script = {"file": tmp_docx, "commands": cmds, "save": [out_docx, out_pdf]}
    script_path = os.path.join(work, f"{doc}.run.json")
    json.dump(script, open(script_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    run(["wordcraft-cli", "run", "--script", script_path])
    r = run(["wordcraft-cli", "info", out_docx])
    pages = json.loads(r.stdout).get("pages")
    print(f"{lang}/{doc}: {pages} pages -> dist/{lang}/{doc}.docx, .pdf")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", choices=LANGS + ["all"], default="all")
    ap.add_argument("--doc", choices=DOCS + ["all"], default="all")
    a = ap.parse_args()
    if shutil.which("wordcraft-cli") is None or shutil.which("magick") is None:
        raise SystemExit("wordcraft-cli and ImageMagick (magick) are required")
    run([sys.executable, "-I", os.path.join(ROOT, "tools", "diagrams.py")])
    os.makedirs(BUILD, exist_ok=True)
    for lang in LANGS if a.lang == "all" else [a.lang]:
        for doc in DOCS if a.doc == "all" else [a.doc]:
            build_one(lang, doc)


if __name__ == "__main__":
    main()
