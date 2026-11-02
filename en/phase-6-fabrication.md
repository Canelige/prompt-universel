Who reads it, and when: `diapo-fabricant`, in phase 6, with `direction-artistique.md` ("Builder's part"); the project chat only looks here for the recipe of a format when needed.

# Phase 6 · Production (`diapo-fabricant`)

**[RULE P6.1]** **The system before the pages.** `tokens.css`: the 9 colors (in Vivid, plus the hues of the roles table); the size scale; the spacings 8, 16, 24, 32, 48, 64, 96, 128; 3 stroke weights; a single corner radius.

**[RULE P6.2]** `travail/build.py` produces each page and the deliverable from `02_contenu.yaml`. A correction changes a YAML entry or a CSS rule, then `python travail/build.py --pages 7,12`. Any value written hard-coded in a page is an error. **`--pages` recipe**, even for an A4 in a single HTML: `page.pdf(..., page_ranges="7,12")` prints only those pages, written to `travail/rendus/pages-7-12.pdf`, then converted to PNG; this partial render does not count in `FULL RENDERS`. **Replacement recipe**, if a delivered PDF exists in `livraison/`: PyMuPDF replaces each page in that PDF, then `livrable.txt` is regenerated page by page from the resulting PDF.

```python
doc, part = pymupdf.open(livre), pymupdf.open(partiel)  # pages = [7, 12], in the order of the partial render
toc, meta = doc.get_toc(), doc.metadata
for i, n in enumerate(pages):
    doc.delete_page(n - 1)
    doc.insert_pdf(part, from_page=i, to_page=i, start_at=n - 1)
doc.set_toc(toc); doc.set_metadata(meta)
doc.save(livre + ".tmp", garbage=4, deflate=True); doc.close(); os.replace(livre + ".tmp", livre)
```

The assembled PDF does not count in `FULL RENDERS` and never goes into `travail/rendus/`, where the gate counts the full renders. A correction that changes the number of pages is not replaced: it requires a full render. Without `--pages`, `build.py` applies the counter of `pilotage.md` (PI.31) and stores the full PDF, timestamped, in `travail/rendus/`.

## The chain by format

**[RULE P6.3]**

| Format | Chain |
|---|---|
| PDF (slide deck) | HTML and CSS → Playwright → PDF |
| A4 document | Paginated HTML (`@page`, header, footer, numbers) → PDF |
| Faithful PPTX | one 3840 × 2160 image per page: PNG for text, charts and flat fills, JPEG quality 85 for a full-bleed photo; notes kept, alt text = title; text neither editable nor selectable |
| Editable PPTX, Google Slides, Keynote | skill `pptx`, real text boxes; charter fonts if they come from Google Fonts (Google Slides offers them all; on PowerPoint, the person installs them from `travail/polices/`, and the report says so), otherwise the fallback below; charter colors, layout templates and rhythm; the PDF rendered with the real fonts is delivered alongside |
| HTML | skill `frontend-slides`, single file, fonts in base64, no remote resource |
| Word | skill `docx`, real styles, table of contents |

**[RULE P6.4]** **Outside PDF**, the PDF rendered from the HTML is the reference: the other formats take up its colors, sizes and rhythm.

**[RULE P6.5]** **Fonts**: before any `soffice`, copy `travail/polices/` into the user's font folder (Mac: `~/Library/Fonts/`; Windows: font installation), otherwise the overflow check is worthless.

**[RULE P6.6]** If the person cannot install the fonts of an editable PPTX: fallback Cambria for titles, Calibri for text (never Georgia), 10% margin in each text box.

**[RULE P6.7]** **Charts**: the SVG from `build.py` converted to PNG at 3 times its display size (Playwright, `device_scale_factor=3`), inserted with the chart's conclusion as alt text.

**[RULE P6.8]** **Editable PPTX**: the 10 layout templates are real master layouts; background, footer (axis 7) and title are set there once; the break page is a separate layout, with its own background (light or flat fill, depending on the charter).

**[RULE P6.9]** **Word**: named styles (Heading 1, Heading 2, Body, Caption, Source) set from `tokens.css`; cover in a separate section; break page = light section, without a full-page rectangle, except in Vivid and in Poster (`direction-artistique.md`, "Color", point 9 h); tables with thin rules; footer according to axis 7; table of contents updated before conversion.

**[RULE P6.10]** **HTML**: `frontend-slides` receives `tokens.css` and `gabarits.css`; no style discovery, no previews, no presets, no gradient or glow.

## Render recipe (Playwright and Chromium)

**[RULE P6.11]** **Fonts**: `@font-face`, relative paths. Before export, wait for `document.fonts.ready` then read `[...document.fonts].map(f => f.family + ':' + f.status)`: an `error` status stops everything. Do not rely on `document.fonts.check()`, which is true for a nonexistent font.

**[RULE P6.12]** **Export**: `page.pdf(prefer_css_page_size=True, print_background=True, outline=True, tagged=True)` and `* { print-color-adjust: exact; -webkit-print-color-adjust: exact }`, otherwise the flat fills disappear.

**[RULE P6.13]** **Slide deck**: `@page { size: 1920px 1080px; margin: 0 }`, one HTML page per PDF page (`break-after: page`); measure `scrollHeight` and `scrollWidth` before hiding anything.

**[RULE P6.14]** **A4**: background color also on `@page` and `html` (otherwise white margins); `break-inside: avoid` on tables and figures; `orphans: 3; widows: 3` on paragraphs.

**[RULE P6.15]** **Metadata**: title and authors via PyMuPDF's `doc.set_metadata(...)`; language from `<html lang>` with `tagged=True`.

**[RULE P6.16]** **Chromium**: if Chromium is missing, rerun `python -m playwright install chromium` with the `.venv` launcher. Fallback if `playwright install` is refused or the expected version is missing: a Chromium from the cache, launched by `p.chromium.launch(executable_path="<path>")`, path given by `find ~/Library/Caches/ms-playwright ~/.cache/ms-playwright -type f \( -name "Chromium*" -o -name "chrome" -o -name "chrome-headless-shell" \) 2>/dev/null`. `chrome-headless-shell` is enough for `page.pdf`; always pass its path to `executable_path`. Windows: cache `%USERPROFILE%\AppData\Local\ms-playwright`.

**[RULE P6.17]** **File size** measured before declaring the deliverable ready; if it is heavy, `doc.save(..., garbage=4, deflate=True)`.

**[RULE P6.18]** **File names**: `Subject_Deliverable_Author.pdf` (the author: the person, their team or their company), without spaces or accents, followed by `_version-to-complete` if the deliverable still has gaps (phase 9).

**[RULE P6.19]** **Delivery**: the final deliverable (PDF, plus PPTX or Word) goes into `<subfolder>/livraison/`, which `build.py` creates by absolute path; `travail/` keeps the rest. `build.py` also writes `travail/livrable.txt`, the text of the final PDF page by page.

**[RULE P6.20]** In phase 6, `diapo-fabricant` also writes `travail/controles.py`, based on "Color", "Typography", "Rhythm and layout templates", "Images" (`direction-artistique.md`) and the list in `phase-7-controles.md`.

## Images

**[MUST P6.21]** **At least 3 real, relevant images in every deliverable**, unless the recipient or the person instructs otherwise: royalty-free and sourced (Unsplash, Pexels, Wikimedia Commons, or the brand's official site, cited), downloaded by script into `travail/images/` and credited in `travail/credits.md` and under the image (`direction-artistique.md`, "Images"). **A page with a large blank** (an empty band of more than 35% of the height, measured by script on the page image) gets an image or a visual (diagram, map, big figure), never stretched text. `controles.py` counts the images and measures the blanks: fewer than 3 images, or a page with a large blank, fails the phase 6 gate.

## Numbers and sheets

**[MUST P6.22]** **No printed number is written in `build.py` or in a layout template.** Every number that is printed (amounts, totals, percentages, years, durations, figures of tiles and timeline strips) comes from `02_contenu.yaml` or from a value computed by `calculs.py`, never from a literal in the code: correcting the YAML must be enough to change everything. Only page numbers and layout numbers (sizes, spacings) are written in the code. `controles.py` checks it: it extracts from `livrable.txt` the numbers of the form that `calculs.py` freezes (P3.25: unit, symbol or year), and any number absent from `02_contenu.yaml` and from the outputs of `calculs.py` fails the phase 6 gate.

**[RULE P6.23]** **Sheet ceiling.** `controles.py` counts the pages of the rendered PDF and compares them to the maximum of `PAGES PROMISED` in `ETAT.md` (DE.27): beyond it, the phase 6 gate fails. The builder condenses (pages merged or text cut, by the writer) instead of delivering extra sheets; only the person's agreement, written in PERSON'S DECISIONS, raises the ceiling.
