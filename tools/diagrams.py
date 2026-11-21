#!/usr/bin/env python3
"""Writes the diagrams of the DentalCraft documentation as SVG.

One SVG per diagram and language: src/img/<name>.<lang>.svg (en, it).
The Markdown sources link these files, GitHub shows them, and tools/build.py
rasterises them (ImageMagick) to embed them in the Word and PDF editions.

Run from the repository root:  python3 tools/diagrams.py
"""
from __future__ import annotations

import os
from xml.sax.saxutils import escape

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "img")

FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"
MONO = "'Liberation Mono', 'DejaVu Sans Mono', monospace"
INK = "#1B2530"
SCALE = 1.15  # text size factor; the box helper shrinks the font again when a box is too small

# kind -> (fill, stroke, text)
KINDS = {
    "blue": ("#E8F0FC", "#1F4E99", "#0B2A5B"),
    "amber": ("#FFF3DC", "#B36B00", "#4A2C00"),
    "green": ("#E6F4EC", "#1E7B4F", "#0C3A25"),
    "grey": ("#F2F3F4", "#5E6B73", "#1B2530"),
    "white": ("#FFFFFF", "#5E6B73", "#1B2530"),
    "red": ("#FCE9EB", "#B4232F", "#4D0F15"),
}


class Svg:
    def __init__(self, w: int, h: int, title: str):
        self.w, self.h, self.title = w, h, title
        self.parts: list[str] = []

    @staticmethod
    def _wrap(line, width, size, mono=False):
        """Greedy word wrap with an estimated glyph width (Inter ~0.56 em, mono 0.6 em)."""
        cw = size * (0.6 if mono else 0.535)
        maxc = max(8, int(width / cw))
        words, out, cur = line.split(" "), [], ""
        for w in words:
            t = (cur + " " + w).strip()
            if len(t) <= maxc or not cur:
                cur = t
            else:
                out.append(cur)
                cur = w
        out.append(cur)
        return out

    def box(self, x, y, w, h, lines, kind="blue", bold_first=True, size=14, mono=False, dash=False):
        fill, stroke, ink = KINDS[kind]
        size = size * SCALE
        d = ' stroke-dasharray="6 4"' if dash else ""
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="1.6"{d}/>'
        )
        if isinstance(lines, str):
            lines = [lines]
        multi = len(lines) > 1
        # wrap every line to the box width; shrink the font until everything fits the height
        while True:
            rows = []
            for i, t in enumerate(lines):
                head = bold_first and i == 0 and multi
                for piece in self._wrap(t, w - 18, size if head or not mono else size - 1, mono and not head):
                    rows.append((piece, head))
            lh = size + 4
            if len(rows) * lh <= h - 10 or size <= 9:
                break
            size -= 1
        top = y + h / 2 - (len(rows) - 1) * lh / 2 + size * 0.35
        for i, (t, head) in enumerate(rows):
            fam = MONO if mono and not head else FONT
            sz = size if not (mono and not head) else size - 1
            self.parts.append(
                f'<text x="{x + w / 2}" y="{top + i * lh:.1f}" font-family="{fam}" '
                f'font-size="{sz}" font-weight="{"700" if head else "400"}" text-anchor="middle" fill="{ink}">{escape(t)}</text>'
            )

    def frame(self, x, y, w, h, title, kind="grey"):
        fill, stroke, ink = KINDS[kind]
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="none" stroke="{stroke}" '
            f'stroke-width="1.4" stroke-dasharray="3 5"/>'
        )
        self.parts.append(
            f'<text x="{x + 14}" y="{y + 20}" font-family="{FONT}" font-size="{13 * SCALE:.1f}" font-weight="700" '
            f'fill="{stroke}">{escape(title)}</text>'
        )

    def text(self, x, y, t, size=13, anchor="middle", weight="400", fill=INK, mono=False):
        size = size * SCALE
        fam = MONO if mono else FONT
        self.parts.append(
            f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}" font-weight="{weight}" '
            f'text-anchor="{anchor}" fill="{fill}">{escape(t)}</text>'
        )

    def arrow(self, x1, y1, x2, y2, color="#1F4E99", dash=False, label=None, lx=None, ly=None, both=False):
        d = ' stroke-dasharray="6 4"' if dash else ""
        start = ' marker-start="url(#ah)"' if both else ""
        self.parts.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.8"{d}'
            f'{start} marker-end="url(#ah)"/>'
        )
        if label:
            self.text(lx if lx is not None else (x1 + x2) / 2, ly if ly is not None else (y1 + y2) / 2 - 6, label, 12)

    def path_arrow(self, d, color="#1F4E99", dash=False):
        ds = ' stroke-dasharray="6 4"' if dash else ""
        self.parts.append(
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="1.8"{ds} marker-end="url(#ah)"/>'
        )

    def render(self) -> str:
        head = (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
            f'viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{escape(self.title)}">'
            f"<title>{escape(self.title)}</title>"
            '<defs><marker id="ah" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto-start-reverse">'
            '<path d="M0 0 L8 4.5 L0 9z" fill="#1F4E99"/></marker></defs>'
            f'<rect width="{self.w}" height="{self.h}" fill="#FFFFFF"/>'
        )
        return head + "".join(self.parts) + "</svg>\n"


def save(name: str, lang: str, svg: Svg):
    path = os.path.join(OUT, f"{name}.{lang}.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg.render())


# --------------------------------------------------------------------------
# 1. Layers
# --------------------------------------------------------------------------
def layers(lang: str):
    T = {
        "en": dict(
            title="DentalCraft layers: core, module and application",
            app="Application  (dentalcraft-app)", mod="Module  (dentalcraft-aligners)", core="Engine  (dentalcraft-core, headless)",
            appd=["dc-app: screens, settings", "dc-workspace: menu, viewport, inspector", "dc-viewport, dc-ui", "dc-scan-ui, dc-print-ui (popups)", "dc-update, dc-diagnostics, dc-auth-client", "dc-cli: command line and MCP"],
            modd=["dca-module: menu, inspectors, commands", "dca-algo: one file per pipeline stage", "dca-model: state stored in the case"],
            cored=["dc-mesh, dc-geom: meshes, geometry kernels", "dc-case, dc-command: case, undo, step history", "dc-jobs, dc-scene: jobs, scene description", "dc-project: .dcprj format", "dc-module-api: the module contract", "dc-session, dc-mcp: command registry, MCP", "dc-scanner, dc-ble, dc-turntable: scanning", "dc-print, dc-raster: printing, headless render", "dc-i18n, dc-theme: languages, design tokens"],
            dep="depends on", srv="Sign-in and diagnostics server", srv2="(separate, closed)",
            https="HTTPS, only when the user signs in or opts in",
        ),
        "it": dict(
            title="Livelli di DentalCraft: motore, modulo e applicazione",
            app="Applicazione  (dentalcraft-app)", mod="Modulo  (dentalcraft-aligners)", core="Motore  (dentalcraft-core, senza interfaccia)",
            appd=["dc-app: schermate, impostazioni", "dc-workspace: menu, vista 3D, ispettore", "dc-viewport, dc-ui", "dc-scan-ui, dc-print-ui (finestre)", "dc-update, dc-diagnostics, dc-auth-client", "dc-cli: riga di comando e MCP"],
            modd=["dca-module: menu, ispettori, comandi", "dca-algo: un file per fase della pipeline", "dca-model: stato salvato nel caso"],
            cored=["dc-mesh, dc-geom: mesh, kernel geometrici", "dc-case, dc-command: caso, annulla, cronologia", "dc-jobs, dc-scene: lavori, descrizione scena", "dc-project: formato .dcprj", "dc-module-api: il contratto dei moduli", "dc-session, dc-mcp: registro comandi, MCP", "dc-scanner, dc-ble, dc-turntable: scansione", "dc-print, dc-raster: stampa, render senza GUI", "dc-i18n, dc-theme: lingue, token di design"],
            dep="dipende da", srv="Server di accesso e diagnostica", srv2="(separato, chiuso)",
            https="HTTPS, solo con l'accesso o il consenso dell'utente",
        ),
    }[lang]
    s = Svg(900, 640, T["title"])
    # app band
    s.frame(20, 16, 640, 196, T["app"], "blue")
    for i, t in enumerate(T["appd"]):
        cx = 36 + (i % 2) * 310
        cy = 42 + (i // 2) * 52
        s.box(cx, cy, 296, 42, t, "blue", size=13)
    s.frame(20, 262, 640, 136, T["mod"], "amber")
    for i, t in enumerate(T["modd"]):
        s.box(36, 286 + i * 34, 608, 30, t, "amber", size=13)
    s.frame(20, 448, 640, 176, T["core"], "green")
    for i, t in enumerate(T["cored"]):
        cx = 36 + (i % 2) * 310
        cy = 472 + (i // 2) * 30
        w = 296 if i < 8 else 608
        s.box(cx, cy, w, 26, t, "green", size=12)
    s.arrow(340, 214, 340, 260)
    s.text(420, 242, T["dep"], 12, "start")
    s.arrow(340, 400, 340, 446)
    s.text(420, 428, T["dep"], 12, "start")
    s.box(690, 40, 190, 76, [T["srv"], T["srv2"]], "grey", size=13, dash=True)
    s.arrow(660, 78, 688, 78, dash=True)
    s.box(690, 130, 190, 70, [T["https"]], "white", size=11, bold_first=False)
    return s


# --------------------------------------------------------------------------
# 2. Aligner pipeline
# --------------------------------------------------------------------------
def pipeline(lang: str):
    T = {
        "en": dict(
            title="The aligner pipeline, from scan to export",
            steps=[
                ("1  Import scans", "STL, OBJ, PLY or scanner;\nclosed with a base"),
                ("2  Find the teeth", "FDI numbers, one mark\nper tooth; orientation"),
                ("3  Separate teeth and gum", "every face of the scan\ngets a tooth label"),
                ("4  3D teeth", "closed solid per tooth,\naxes, gingiva"),
                ("5  Case analysis", "space, Little index,\nBolton, complexity"),
                ("6  Bite", "upper to lower arch:\nbite scans or virtual bite"),
                ("7  Final position", "target pose of every\ntooth, IPR, arch line"),
                ("8  Aligners", "stages, calendar,\nattachments"),
                ("9  Clinical review", "proposals confirmed\nby the clinician"),
            ],
            out=["Export for printing", "shells, models, report, manifest"],
            out2=["Print", "plates (GOO) for the printer"],
            case="The case (.dcprj): scans, tooth marks, labels, solids, poses, stages, review records",
            undo="every step is one undoable command and one step in the history",
        ),
        "it": dict(
            title="La pipeline degli allineatori, dalla scansione all'esportazione",
            steps=[
                ("1  Importa scansioni", "STL, OBJ, PLY o scanner;\nchiuse con una base"),
                ("2  Trova i denti", "numeri FDI, un segno\nper dente; orientamento"),
                ("3  Separa denti e gengiva", "ogni faccia della scansione\nriceve l'etichetta del dente"),
                ("4  Denti 3D", "solido chiuso per dente,\nassi, gengiva"),
                ("5  Analisi del caso", "spazio, indice di Little,\nBolton, complessità"),
                ("6  Morso", "arcata superiore su inferiore:\nscansioni del morso o virtuale"),
                ("7  Posizione finale", "posa finale di ogni\ndente, IPR, linea d'arcata"),
                ("8  Allineatori", "stadi, calendario,\nattachment"),
                ("9  Revisione clinica", "proposte confermate\ndal clinico"),
            ],
            out=["Esporta per la stampa", "gusci, modelli, relazione, elenco file"],
            out2=["Stampa", "piastre (GOO) per la stampante"],
            case="Il caso (.dcprj): scansioni, segni, etichette, solidi, pose, stadi, record di revisione",
            undo="ogni passo è un comando annullabile e un passo della cronologia",
        ),
    }[lang]
    s = Svg(900, 520, T["title"])
    bw, bh = 160, 84
    xs = [20 + i * 176 for i in range(5)]
    for i, (t, d) in enumerate(T["steps"][:5]):
        s.box(xs[i], 20, bw, bh, [t] + d.split("\n"), "blue", size=12)
        if i:
            s.arrow(xs[i - 1] + bw, 62, xs[i], 62)
    # second row right-to-left would confuse; keep left to right
    for i, (t, d) in enumerate(T["steps"][5:]):
        s.box(xs[i], 150, bw, bh, [t] + d.split("\n"), "blue", size=12)
        if i:
            s.arrow(xs[i - 1] + bw, 192, xs[i], 192)
    s.path_arrow(f"M {xs[4] + bw / 2} 104 L {xs[4] + bw / 2} 126 L {xs[0] + bw / 2} 126 L {xs[0] + bw / 2} 148")
    s.box(xs[4], 150, bw, bh, T["out"][:1] + [T["out"][1]], "amber", size=12)
    s.arrow(xs[3] + bw, 192, xs[4], 192)
    s.box(xs[4], 270, bw, 70, T["out2"], "amber", size=12)
    s.arrow(xs[4] + bw / 2, 234, xs[4] + bw / 2, 268)
    s.frame(20, 370, 860, 130, "")
    s.box(40, 396, 820, 44, T["case"], "green", size=13, bold_first=False)
    s.text(450, 470, T["undo"], 12)
    s.arrow(100, 234, 100, 394, dash=True, color="#1E7B4F")
    s.arrow(780, 340, 780, 394, dash=True, color="#1E7B4F")
    return s


# --------------------------------------------------------------------------
# 3. Print pipeline
# --------------------------------------------------------------------------
def printpipe(lang: str):
    T = {
        "en": dict(
            title="The print pipeline: orient, supports, nest, slice, GOO",
            src=["Export for printing", "shells + stage models"],
            steps=[("Orient", "fitting side away\nfrom the plate"), ("Supports", "outer side only,\ntip + shaft + U raft"),
                   ("Nest", "plates, gap and\nmargin kept"), ("Slice", "layer runs, never a\nfull bitmap"), ("GOO V3", "one file per plate,\nMD5 and previews")],
            chk=["Hard checks", "no support contact on the fitting side", "no unsupported island in any layer", "every part fits the plate and height"],
            usb=["USB stick (FAT32)", "plate_01.goo, plate_02.goo ..."],
            prn=["Printer", "Saturn 4 Ultra 16K, DENTAL 45"],
            trk=["Tracking in the case", "to print, queued, sent, printed, failed, to print again"],
            inp=["Inputs", "resin values entered by the user:", "layer, exposure, first layers, rest, density"],
        ),
        "it": dict(
            title="La pipeline di stampa: orienta, supporti, disponi, affetta, GOO",
            src=["Esporta per la stampa", "gusci + modelli degli stadi"],
            steps=[("Orienta", "lato di calzata lontano\ndalla piastra"), ("Supporti", "solo lato esterno,\npunta + fusto + zattera a U"),
                   ("Disponi", "piastre, distanza e\nmargine rispettati"), ("Affetta", "strati a tratti, mai\nuna bitmap intera"), ("GOO V3", "un file per piastra,\nMD5 e anteprime")],
            chk=["Controlli obbligatori", "nessun supporto sul lato di calzata", "nessuna isola senza supporto in uno strato", "ogni pezzo sta su piastra e altezza"],
            usb=["Chiavetta USB (FAT32)", "plate_01.goo, plate_02.goo ..."],
            prn=["Stampante", "Saturn 4 Ultra 16K, DENTAL 45"],
            trk=["Tracciamento nel caso", "da stampare, in coda, inviato, stampato, fallito, da ristampare"],
            inp=["Dati di partenza", "valori della resina inseriti dall'utente:", "strato, esposizione, primi strati, pausa, densità"],
        ),
    }[lang]
    s = Svg(900, 450, T["title"])
    s.box(520, 14, 360, 62, T["inp"], "grey", size=12)
    s.arrow(682, 76, 682, 108, dash=True)
    s.box(20, 110, 150, 80, T["src"], "amber", size=12)
    x0 = 200
    for i, (t, d) in enumerate(T["steps"]):
        x = x0 + i * 140
        s.box(x, 110, 124, 80, [t] + d.split("\n"), "blue", size=12)
        s.arrow(x - 30 if i == 0 else x - 16, 150, x, 150)
    s.box(20, 215, 580, 92, T["chk"], "red", size=12)
    s.path_arrow("M 822 190 L 822 335 L 150 335 L 150 358")
    s.box(20, 360, 260, 70, T["usb"], "green", size=13)
    s.box(330, 360, 260, 70, T["prn"], "green", size=13)
    s.box(630, 360, 250, 70, T["trk"], "amber", size=12)
    s.arrow(280, 395, 328, 395)
    s.arrow(590, 395, 628, 395, dash=True)
    return s


# --------------------------------------------------------------------------
# 4. Scanner connector
# --------------------------------------------------------------------------
def scanner(lang: str):
    T = {
        "en": dict(
            title="The scanner connector",
            dev=["Scanner backends", "Revopoint MINI 2 over USB", "(V4L2 / UVC, Media Foundation)", "optional vendor SDK", "simulated scanner"],
            tt=["Turntable", "Revopoint dual-axis table", "over Bluetooth LE", "(BlueZ, WinRT, CoreBluetooth)", "simulated table"],
            trk=["Live tracking", "pose from the table angle,", "ICP only to refine"],
            fuse=["Fusion", "TSDF volume, 0.1 mm", "weights, consistency gate"],
            fin=["Mesh finish", "clean, close holes,", "denoise, simplify"],
            out=["ScanOutput", "a mesh file the host owns"],
            host=["Hosts", "New project screen", "Import scans in the workspace", "any other module"],
            popup=["dc-scan-ui popup", "steps: Acquisition, Surface, Import", "(advanced options: point cloud,", "surface tools, readouts)"],
            cmds=["Agents: scan.* and turntable.* commands, scan.auto"],
        ),
        "it": dict(
            title="Il connettore dello scanner",
            dev=["Backend dello scanner", "Revopoint MINI 2 via USB", "(V4L2 / UVC, Media Foundation)", "SDK del produttore (opzionale)", "scanner simulato"],
            tt=["Piatto rotante", "Revopoint a doppio asse", "via Bluetooth LE", "(BlueZ, WinRT, CoreBluetooth)", "piatto simulato"],
            trk=["Tracciamento", "posa dall'angolo del piatto,", "ICP solo per rifinire"],
            fuse=["Fusione", "volume TSDF, 0,1 mm", "pesi, controllo di coerenza"],
            fin=["Rifinitura mesh", "pulizia, chiusura buchi,", "denoise, semplificazione"],
            out=["ScanOutput", "un file mesh del chiamante"],
            host=["Chi la usa", "schermata Nuovo progetto", "Importa scansioni nel workspace", "qualunque altro modulo"],
            popup=["Finestra dc-scan-ui", "passi: Acquisizione, Superficie, Importa", "(opzioni avanzate: nuvola di punti,", "strumenti di superficie, letture)"],
            cmds=["Agenti: comandi scan.* e turntable.*, scan.auto"],
        ),
    }[lang]
    s = Svg(900, 470, T["title"])
    s.box(20, 24, 250, 120, T["dev"], "blue", size=12)
    s.box(20, 170, 250, 120, T["tt"], "blue", size=12)
    s.box(320, 80, 170, 100, T["trk"], "amber", size=12)
    s.box(530, 80, 170, 100, T["fuse"], "amber", size=12)
    s.box(530, 220, 170, 90, T["fin"], "amber", size=12)
    s.box(320, 230, 170, 70, T["out"], "green", size=13)
    s.box(730, 80, 150, 130, T["host"], "grey", size=12)
    s.arrow(270, 84, 318, 120)
    s.arrow(270, 230, 318, 150)
    s.arrow(490, 130, 528, 130)
    s.arrow(615, 182, 615, 218)
    s.arrow(530, 265, 492, 265)
    s.path_arrow("M 405 302 L 405 340 L 805 340 L 805 212")
    s.box(20, 350, 700, 80, T["popup"], "green", size=12)
    s.text(450, 455, T["cmds"][0], 12)
    return s


# --------------------------------------------------------------------------
# 5. Agent interface
# --------------------------------------------------------------------------
def agent(lang: str):
    T = {
        "en": dict(
            title="Driving DentalCraft from a script or an agent",
            ag=["Agent or script", "MCP client, shell"],
            cli=["dentalcraft-cli", "run, describe, mcp, render"],
            h=["Headless session", "(dc-session)"],
            app=["dentalcraft --control PORT", "the app, bridge on 127.0.0.1"],
            reg=["One command registry", "project.*, case.*, scan.*, print.*, aligners.*, app.*", "same ids, same parameters, same results"],
            m1="stdio, JSON-RPC (MCP)", m2="mcp --connect PORT",
            a="Mode A: headless", b="Mode B: bridge to the running app",
            n="Changes made through the bridge appear in the window and are undoable there.",
        ),
        "it": dict(
            title="Pilotare DentalCraft da uno script o da un agente",
            ag=["Agente o script", "client MCP, shell"],
            cli=["dentalcraft-cli", "run, describe, mcp, render"],
            h=["Sessione senza GUI", "(dc-session)"],
            app=["dentalcraft --control PORTA", "l'app, ponte su 127.0.0.1"],
            reg=["Un solo registro di comandi", "project.*, case.*, scan.*, print.*, aligners.*, app.*", "stessi id, stessi parametri, stessi risultati"],
            m1="stdio, JSON-RPC (MCP)", m2="mcp --connect PORTA",
            a="Modo A: senza GUI", b="Modo B: ponte verso l'app aperta",
            n="Le modifiche fatte dal ponte compaiono nella finestra e lì si possono annullare.",
        ),
    }[lang]
    s = Svg(900, 420, T["title"])
    s.box(20, 140, 170, 70, T["ag"], "grey", size=13)
    s.box(250, 140, 200, 70, T["cli"], "blue", size=13)
    s.arrow(190, 175, 248, 175, both=True)
    s.text(220, 160, "", 11)
    s.frame(500, 24, 380, 130, T["a"], "green")
    s.box(530, 60, 320, 70, T["h"], "green", size=13)
    s.frame(500, 200, 380, 130, T["b"], "amber")
    s.box(530, 236, 320, 70, T["app"], "amber", size=13)
    s.path_arrow("M 450 160 L 480 160 L 480 95 L 528 95")
    s.path_arrow("M 450 190 L 480 190 L 480 271 L 528 271")
    s.text(472, 140, "", 11)
    s.box(20, 352, 860, 56, T["reg"], "white", size=12)
    s.text(350, 118, T["m1"], 12)
    s.text(350, 232, T["m2"], 12)
    s.text(450, 316, "", 11)
    return s


# --------------------------------------------------------------------------
# 6. Development flow
# --------------------------------------------------------------------------
def devflow(lang: str):
    T = {
        "en": dict(
            title="From a change to a release",
            st=[("Branch", "feat/* or fix/*\nconventional commits"), ("Local gate", "fmt, clippy -D warnings,\ntests (+ Kani laws)"),
                ("Pull request", "ci-local.sh --pr\non the merge result"), ("Squash merge", "title = conventional\ncommit"),
                ("Release PR", "release-please\nbumps, changelog"), ("Tag + release", "vX.Y.Z, binaries,\ninstallers")],
            pins="Consumers pin the new tag (core, then aligners, then app); the website is updated in the same release.",
            note="scripts/ci-local.sh, scripts/pr-merge-local.sh, scripts/release-local.sh replay the workflows locally while GitHub Actions is suspended.",
        ),
        "it": dict(
            title="Da una modifica a una release",
            st=[("Ramo", "feat/* o fix/*\ncommit convenzionali"), ("Controllo locale", "fmt, clippy -D warnings,\ntest (+ leggi Kani)"),
                ("Pull request", "ci-local.sh --pr\nsul risultato del merge"), ("Squash merge", "titolo = commit\nconvenzionale"),
                ("PR di release", "release-please:\nversione, changelog"), ("Tag + release", "vX.Y.Z, binari,\ninstaller")],
            pins="I consumatori puntano al nuovo tag (core, poi aligners, poi app); il sito si aggiorna nella stessa release.",
            note="scripts/ci-local.sh, scripts/pr-merge-local.sh, scripts/release-local.sh riproducono i workflow in locale finché GitHub Actions è sospeso.",
        ),
    }[lang]
    s = Svg(900, 300, T["title"])
    for i, (t, d) in enumerate(T["st"]):
        x = 20 + i * 146
        s.box(x, 30, 130, 96, [t] + d.split("\n"), "blue" if i < 4 else "amber", size=12)
        if i:
            s.arrow(x - 16, 78, x, 78)
    s.box(20, 160, 860, 44, T["pins"], "green", size=12, bold_first=False)
    s.arrow(810, 128, 810, 158, dash=True)
    s.text(450, 240, T["note"], 11)
    return s


# --------------------------------------------------------------------------
# 7. .dcprj container
# --------------------------------------------------------------------------
def dcprj(lang: str):
    T = {
        "en": dict(
            title="The .dcprj project container",
            z="project.dcprj  (ZIP)",
            rows=[
                ("mimetype", "first entry, stored: application/vnd.dentalcraft.project+zip"),
                ("manifest.json", "format_version, modules, BLAKE3 and size of every entry"),
                ("case.json", "pseudonymised patient code, scans, world frame"),
                ("modules/<id>/state.json", "module data, for example aligners"),
                ("history/steps.json", "processing step history (undo stack is not saved)"),
                ("blobs/<blake3>.dcm", "DCM1 mesh blobs, content addressed"),
                ("thumbnail.png", "preview for the Home screen"),
            ],
            n="Saving: write .tmp, fsync, rename; one .bak kept. Loading: BLAKE3 verified, a newer format opens read-only.",
        ),
        "it": dict(
            title="Il contenitore di progetto .dcprj",
            z="progetto.dcprj  (ZIP)",
            rows=[
                ("mimetype", "prima voce, non compressa: application/vnd.dentalcraft.project+zip"),
                ("manifest.json", "format_version, moduli, BLAKE3 e dimensione di ogni voce"),
                ("case.json", "codice paziente pseudonimizzato, scansioni, sistema di riferimento"),
                ("modules/<id>/state.json", "dati del modulo, per esempio aligners"),
                ("history/steps.json", "cronologia dei passi (lo stack annulla non si salva)"),
                ("blobs/<blake3>.dcm", "mesh DCM1, indirizzate dal contenuto"),
                ("thumbnail.png", "anteprima per la schermata Home"),
            ],
            n="Salvataggio: scrive .tmp, fsync, rinomina; si tiene un .bak. Apertura: BLAKE3 verificato, un formato più recente si apre in sola lettura.",
        ),
    }[lang]
    s = Svg(900, 400, T["title"])
    s.frame(20, 14, 860, 330, T["z"], "blue")
    for i, (a, b) in enumerate(T["rows"]):
        y = 40 + i * 42
        s.box(40, y, 270, 34, a, "blue", size=13, mono=True, bold_first=False)
        s.box(330, y, 530, 34, b, "white", size=12, bold_first=False)
    s.text(450, 372, T["n"], 11)
    return s


# --------------------------------------------------------------------------
# 8. User workflow
# --------------------------------------------------------------------------
def workflow(lang: str):
    T = {
        "en": dict(
            title="The workflow, step by step",
            groups=[
                ("Case", [("Import", "or scan")]),
                ("Teeth", [("Find the teeth", ""), ("Separate teeth\nand gum", ""), ("3D teeth", "")]),
                ("Diagnosis", [("Case analysis", "")]),
                ("Plan", [("Bite", ""), ("Final position", ""), ("Aligners", ""), ("Clinical review", "")]),
                ("Production", [("Export for\nprinting", ""), ("Print", "")]),
            ],
            auto="Run everything automatically does the nine steps in one job.",
        ),
        "it": dict(
            title="Il flusso di lavoro, passo per passo",
            groups=[
                ("Caso", [("Importa", "o scansiona")]),
                ("Denti", [("Trova i denti", ""), ("Separa denti\ne gengiva", ""), ("Denti 3D", "")]),
                ("Diagnosi", [("Analisi del caso", "")]),
                ("Piano", [("Morso", ""), ("Posizione\nfinale", ""), ("Allineatori", ""), ("Revisione\nclinica", "")]),
                ("Produzione", [("Esporta per\nla stampa", ""), ("Stampa", "")]),
            ],
            auto="Esegui tutto in automatico svolge i nove passi in un solo lavoro.",
        ),
    }[lang]
    s = Svg(900, 330, T["title"])
    # layout: two rows of groups
    rows = [[0, 1, 2], [3, 4]]
    y = 20
    for r in rows:
        x = 20
        for gi in r:
            name, items = T["groups"][gi]
            w = 40 + len(items) * 128
            s.frame(x, y, w, 120, name, "blue" if gi < 4 else "amber")
            for j, (t, d) in enumerate(items):
                ls = t.split("\n")
                if d:
                    ls = ls + [d]
                s.box(x + 14 + j * 128, y + 34, 116, 70, ls, "blue" if gi < 4 else "amber", size=12, bold_first=False)
            x += w + 20
        y += 150
    s.text(450, 322, T["auto"], 12)
    return s


ALL = {"layers": layers, "pipeline": pipeline, "print-pipeline": printpipe, "scanner": scanner,
       "agent-interface": agent, "dev-flow": devflow, "dcprj": dcprj, "workflow": workflow}


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, fn in ALL.items():
        for lang in ("en", "it"):
            save(name, lang, fn(lang))
    print("wrote", len(ALL) * 2, "diagrams in", os.path.normpath(OUT))


if __name__ == "__main__":
    main()
