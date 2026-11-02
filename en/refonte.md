Who reads it, and when: the project chat, when `ETAT.md` carries `TYPE : refonte complète` or `TYPE : refonte ciblée`, at opening and at each resume; `diapo-documentaliste` for point 2 only. When this module diverges from a phase, it takes precedence.

# Redesign mode

**[RULE RF.1]** **First the recipient's feedback** (the professor's grade and comments, the client's or manager's answer): first list of flaws.

**[RULE RF.2]** **Extraction**, by `diapo-documentaliste`: PPTX, `python -m markitdown ancien.pptx` (text, notes) then the images from `ppt/media`; PDF, PyMuPDF; render to images, `soffice --headless --convert-to pdf` if LibreOffice is installed (Windows: `C:\Program Files\LibreOffice\program\soffice.exe`). Without LibreOffice: diagnosis on the text, report "layout of the old deliverable not evaluated".

**[MUST RF.3]** A LibreOffice render does not have the original fonts: never report an overflow in the old work without confirmation.

**[RULE RF.4]** **Diagnosis**, after phase 1: the "destinataire" (recipient) auditor grades the old work.

**[MUST RF.5]** **Keep the substance**: correct facts, the person's decisions, requested analyses and imposed order stay; what is false is corrected and flagged, what is missing against the criteria is added and flagged. Answer "form only": the content changes only to correct an error.

**[RULE RF.6]** **Full redesign** (2 h 30 or more, in Express as in In-depth): all the phases; default output format is that of the original (original PPTX: an editable PPTX and a PDF).

**[RULE RF.7]** **Targeted redesign** (less than 2 h 30): in-place editing. Deliverable: copy of the original PPTX in `<sous-dossier>/livraison/`; the `pptx` skill unpacks it, the 5 weakest pages are modified based on the comments, plus those that cover the missing criteria, and it is repacked. The other pages do not move.

**[RULE RF.8]** The original's style charter is kept; no seed, no directions, no stop B, no `build.py`. Fix what the comments criticize (legibility, contrast, hierarchy, titles, figures). Modified text: phase 4; final check of phase 9 on the whole file, unmodified pages included.

**[MUST RF.9]** Check: `soffice` converts the copy to PDF, PyMuPDF pulls the PNGs of the modified pages only; without LibreOffice, "no page visually verified", never `ok`.

**[MUST RF.10]** Audit of a targeted redesign: the recipient, the decision-maker and the art director on the reworked pages (the three viewpoints of `phase-8-audit.md`).

**[RULE RF.11]** **The short path**: phase 1 reduced to the recipient's diagnosis of the old deliverable, to the list of pages to rework and to the expert on that diagnosis alone; no full ghost deck, no title test; web verification limited to the figures of the reworked pages. Then: phase 4 on the modified sentences, checks, audit, delivery.

**[RULE RF.12]** **At delivery**: a before/after contact sheet, the list of changes page by page, the estimated grade before and after.
