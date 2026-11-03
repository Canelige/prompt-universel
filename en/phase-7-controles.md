Who reads it, and when: `diapo-fabricant`, in phase 6, to write `controles.py`; the project chat, in phase 7, to run the checks and the tests; `diapo-lecteur` only receives its batch of pages, never this module.

# Phase 7 · Checks (scripts, then the lead)

**[RULE P7.1]** Check PNGs drawn from the final PDF, with PyMuPDF at 110 dpi. Editable PPTX or Word: this PDF comes from `soffice --headless --convert-to pdf`.

**[MUST P7.2]** Without LibreOffice, the overflow check is impossible, and the report says so.

**[RULE P7.3]** The lead runs `travail/controles.py` and reads only `travail/07_controles.md`, which `controles.py` writes itself (P6.20): the check lines, the overall `COLORED AREA: n %` and a table per sheet with `ok` or the measured value.

## 1. Charter checks (thresholds from `direction-artistique.md`)

**[RULE P7.4]** Size outside the scale, family outside the charter; insufficient contrast.

**[RULE P7.5]** Hue outside the roles table, more hues on a page than the energy allows (point 9 b, brand signature exempt), status pills outside point 9 f.

**[RULE P7.6]** More framed text blocks than point 9 g allows (cards, callouts, pills of more than 3 words): the page reads like a dashboard, group into a table with thin rules or refer the detail to the notes.

**[RULE P7.7]** Stroke or angle outside the tokens, block outside the grid, spacing that is not a multiple of 8.

**[RULE P7.8]** Rhythm: same layout template 3 times in a row, more than 6 pages without a break, fewer than 2 breaks (fewer than 1 under 8 pages).

**[RULE P7.9]** Figure without `tabular-nums`, missing non-breaking space (in French).

**[RULE P7.10]** **Colored area** (measure of point 9 e) outside the range of the chosen energy, over the whole deliverable, or above the maximum per sheet, or a loud vivid flat (OKLCH chroma above 0.14 on too much area): `direction-artistique.md`, DA.54, measured by `controles.py`.

**[MUST P7.10b]** **Vivid: the range is blocking.** `portes.py 7` reads the overall colored area in `07_controles.md`: under 10%, the phase 7 gate fails. To raise it, in this order: number tiles in solid flat fill rather than outlined; table headers in flat fill; a tinted section background (color of the section's role) on the break pages and summary blocks; last, a title banner in a flat fill of the structure color on content pages (10% of the height at most, P7.12). Never by tinting the whole page background, nor with a hue outside the roles table, nor with a derived intermediate tone (the pale pink of trial no. 7, judged "from nowhere and not very clean": DA.44). Then render only the modified pages (P6.2) and measure again.

**[RULE P7.11]** **Color floor**: page under 3% colored area (unless Typographic Sober was chosen), or under the number of color moments of the energy (point 9 e), or Vivid or Poster cover without a flat fill of a quarter of the page.

**[RULE P7.12]** **Flat fills, titles and cover**: title banner of more than 10% of the page height, sentence-title of more than 70 characters or more than 2 lines, cover product under the 3:1 contrast with its background, more than 3 figures on the cover.

**[RULE P7.13]** Real brand: logo missing from the cover or the banner. Fewer than 3 real images, or a page with a large blank (`phase-6-fabrication.md`, P6.21).

**[RULE P7.14]** PPTX or Word: sizes, fonts and colors read with `python-pptx` or `python-docx`.

**[TIP P7.15]** If `impeccable` is installed, also run its detector: `find ~/.claude .claude -path "*impeccable/scripts/impeccable" 2>/dev/null | head -1` gives its path, then `<path> detect --json <files.html>`.

## 2. Text checks

**[MUST P7.16]** BUDGET; OVERFLOW; OVERLAP (`getBoundingClientRect` in Playwright: two text boxes that overlap by more than 2 px, or text that leaves the frame of its chart); SPLIT (label of 3 words or fewer on two lines); WIDOW; font not loaded, image missing, wrong number; em dash, "Lorem", "TODO", bracket `[to complete]`.

## 3. Variants for the audit

**[RULE P7.17]** Slide deck, each page at 960 × 540; A4, each page at 794 × 1123; the same in grayscale; contact sheets of 6 pages and an overall contact sheet.

**[RULE P7.18]** Correct, then rerun, within the render ceiling (`pilotage.md`, "Economy").

## Reading tests

**[RULE P7.19]** **Screen** (`diapo-lecteur`, Haiku, one reader per batch of 6 pages in In-depth; in Express, **a single reader** for the whole deliverable, because a subagent costs about 100,000 tokens from its first call, `pilotage.md` PI.33): it copies into `travail/tests/ecran.txt` the titles, the text, the chart labels and, for the sources, at least the organization and the year; a script compares its copy to `livrable.txt` and lists the missing words. Render at 1280 × 720 (slide deck) or 150 dpi (A4); sources, notes and page numbers excluded. What is missing goes up one notch on the scale, only once. In Express, this is the only test.

**[RULE P7.20]** **Rhythm**, by script, on the layout templates of `02_contenu.yaml`: at least 4 different layout templates, breaks at the right cadence.

**[RULE P7.21]** The other readings are done in phase 8: the answer first and the titles alone (tests 1 and 2) by the recipient; black and white and personality by the art director.

**[RULE P7.22]** **Drop-off**, by script: size under the platform limit, file that opens, fonts embedded (`pdffonts`). Then, **stop C**.
