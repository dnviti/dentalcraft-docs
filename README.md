# dentalcraft-docs

The documentation of **[DentalCraft](https://github.com/dnviti/dentalcraft)**, a desktop application for digital dentistry written in Rust, in **English** and **Italian**. Each document is kept as Markdown (the source), and as a Word (`.docx`) and a PDF edition built from it with WordCraft.

> **DentalCraft is not a certified medical device.** The documentation describes research and design software. Nothing in it is clinical advice.

La documentazione di DentalCraft è disponibile anche in italiano: vedi la colonna *Italiano* della tabella.

## The documents

| Document | English | Italiano |
| --- | --- | --- |
| **User manual**: install, sign in, Settings, the workflow from scan to printed aligner (Saturn 4 Ultra 16K), troubleshooting. *Manuale utente.* | [Markdown](src/en/user-manual.md) · [Word](dist/en/user-manual.docx) · [PDF](dist/en/user-manual.pdf) | [Markdown](src/it/user-manual.md) · [Word](dist/it/user-manual.docx) · [PDF](dist/it/user-manual.pdf) |
| **Developer guide**: repositories and crates, build and test, the local `[patch]`, local CI and release, the CLI and MCP agent interface, the `.dcprj` format, i18n, Kani laws, contributing. *Guida per sviluppatori.* | [Markdown](src/en/developer-guide.md) · [Word](dist/en/developer-guide.docx) · [PDF](dist/en/developer-guide.pdf) | [Markdown](src/it/developer-guide.md) · [Word](dist/it/developer-guide.docx) · [PDF](dist/it/developer-guide.pdf) |
| **Architecture**: layering, the aligner pipeline, the print pipeline, the scanner connector. *Architettura.* | [Markdown](src/en/architecture.md) · [Word](dist/en/architecture.docx) · [PDF](dist/en/architecture.pdf) | [Markdown](src/it/architecture.md) · [Word](dist/it/architecture.docx) · [PDF](dist/it/architecture.pdf) |
| **Sources**: the bibliography, grouped by area. *Fonti.* | [Markdown](src/en/sources.md) · [Word](dist/en/sources.docx) · [PDF](dist/en/sources.pdf) | [Markdown](src/it/sources.md) · [Word](dist/it/sources.docx) · [PDF](dist/it/sources.pdf) |

The pages are also published at <https://dnviti.github.io/dentalcraft-docs/> (GitHub Pages, from the `main` branch).

## Which version they describe

Each document carries its edition date and the versions it describes on its first page. The current edition (21 November 2026) describes DentalCraft **0.2.0-alpha.13** (application), with the Aligners module **0.2.0-alpha.12** and the engine (core) **0.3.0-alpha.8**. It includes the **Settings** (with the "Advanced options and parameters" switch, off by default) and the direct **printing** of aligners on the Elegoo Saturn 4 Ultra 16K (U-shaped raft, fitting side from the stage model, print tracking per aligner). Where something is not finished, the text says so.

## How this repository is updated

**The documentation is regenerated at every release.** A release of DentalCraft means all the project repositories are released together (core, aligners, app, web); the documentation is part of that work:

1. Update the Markdown in `src/en/` and `src/it/` for what changed in the release: the user manual for anything a user sees, the developer guide and the architecture for anything a developer sees, and the sources when a paper, standard or specification was added (`SOURCES.md` in the `dentalcraft` repository is the living list; the Sources document is regenerated from it, with the Italian headings).
2. Update the edition line (date, version) of each document and keep the English and Italian editions in step: same sections, same numbering.
3. Run `python3 tools/build.py`. It redraws the diagrams, asks WordCraft to convert and style every document, and writes `dist/<lang>/<doc>.docx` and `.pdf`.
4. Check every page of the PDFs for overflow, clipped tables, wrong fonts and broken figures.
5. Commit the sources and the rebuilt files together, with a conventional commit (`docs: ...`) and a `Signed-off-by` line, push to `main`, and let GitHub Pages publish.

A release is not complete until the documentation of that release is merged. A documentation change that is not tied to a release (a correction, a clearer sentence) can be made at any time by pull request.

## Layout

```text
src/en/*.md, src/it/*.md   the sources: user-manual, developer-guide, architecture, sources
src/img/*.svg              diagrams, one per language (name.en.svg, name.it.svg)
src/img/screenshots/       screenshots of the application (English interface)
dist/en/*.docx, *.pdf      the built editions
dist/it/*.docx, *.pdf
tools/diagrams.py          writes the SVG diagrams
tools/build.py             builds the Word and PDF editions
index.md, _config.yml      the GitHub Pages site (Jekyll, minimal theme, no Actions)
LICENSE.md                 CC BY-NC-SA 4.0
```

The diagrams are SVG, so GitHub shows them in the Markdown and they stay editable; `tools/diagrams.py` generates them, in both languages, from one description.

The PDFs embed their fonts. The Word files name the fonts *Inter* and *Liberation Mono*: install them for the same look, otherwise Word substitutes similar ones.

### Building the editions

Needs `wordcraft-cli` (WordCraft, of the ArtCraft suite), ImageMagick (`magick`) and the fonts *Inter* and *Liberation Mono*:

```sh
python3 tools/build.py                          # everything
python3 tools/build.py --lang it --doc user-manual
```

For each document the script prepares the Markdown (title block, heading levels, wide bibliography tables as lists), converts it with `wordcraft-cli convert`, then runs a WordCraft script that sets A4 and the styles, sizes the tables, inserts the diagrams and screenshots as pictures, builds the table of contents, adds the header and the page numbers, and saves both formats. Scratch files go to `.build/`, which is not committed.

## Screenshots

The screenshots are of an early version of the application (0.1.0) with the English interface, used in both languages; the captions say so. Screens that showed placeholder dates for future modules were left out on purpose.

## Contributing

Corrections and translations are welcome: open an issue or a pull request. Sign off your commits (`git commit -s`, the Developer Certificate of Origin 1.1), use conventional commits, keep the English and Italian editions in step, and never include patient data, real scans or details of private infrastructure. See `CONTRIBUTING.md` in the [`dentalcraft`](https://github.com/dnviti/dentalcraft) repository for the full rules, including the licence of a contribution.

## Licence

The documentation is licensed under **CC BY-NC-SA 4.0** (attribution, non-commercial, share alike): see [`LICENSE.md`](LICENSE.md). The software is under the PolyForm Noncommercial License 1.0.0 in its own repositories.
