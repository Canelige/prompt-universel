Who reads it, and when: the project chat, in phase 9, for the checklist and the final report; `diapo-redacteur` for the "mastery sheet" only; the lead, to relay the report and to maintain `profil.md` and `ETAT_COURANT.md`.

# Phase 9 · Delivery

## Checklist

**[MUST P9.1]** Every judging criterion is covered, its page is indicated.

**[MUST P9.2]** Every displayed figure appears in `03_verification.md`, with its verdict.

**[MUST P9.3]** Assumptions in the register. **Zero brackets in the final deliverable**: the `[to complete]` markers live only in the working files. Before delivery, ask the person, through the lead and in a single question (stop E), for the missing elements (names of the team or the author, the school's or company's rule on AI). If some are still missing: "version to complete" in the file name (`_version-to-complete`), the area concerned left empty or the sentence reworded without it, gaps listed in the final report.

**[RULE P9.4]** `07_controles.md` shows `ok` everywhere, or each defect appears under REMAINDER.

**[MUST P9.5]** The audit is done, its SEVERE and MEDIUM points are corrected.

**[RULE P9.6]** The Sources appendix follows the format requested by the recipient (APA by default); image credits given. Pages and ranges: the keyboard hyphen (12-15) replaces the APA en dash.

**[MUST P9.7]** The AI usage statement is attached, if the school or company requires it.

**[MUST P9.8]** **Singularity test**: mentally replace the name of the company or the country with another one; if almost everything remains true, the page is generic and goes back to phase 2. Write in one line, in `PREUVES.md`, the 3 things that make this work identifiable as that of this person.

**[RULE P9.9]** `travail/fiche_maitrise.md` exists (in Express, last section of `03_verification.md`), written by `diapo-redacteur` from `02_contenu.yaml` and `03_verification.md`, then run through `humanizer`: per page, the idea to remember, the origin of each figure, the question the recipient would ask (professor, client, jury). The person reads it before the oral presentation.

**[MUST P9.10]** **`humanizer`, then final anti-AI check**, on everything that is delivered: deliverable text, PPTX notes (read with `python-pptx`), `oral.md`, `fiche_maitrise.md`, appendices, AI usage statement. Each file carries "humanizer passed" in a status; then the script runs.

**[MUST P9.11]** Expected result of **zero**: U+2014, U+2013, emojis, "Lorem", "TODO", bracket `[to complete]`, unconditional tics from phase 4 (crucial, incontournable, synergie, holistique...).

**[RULE P9.12]** Conditional tics (« clé », « enjeu », « permettre de »): counted per page; beyond one per page, the sentence goes back through phase 4. « Enjeu chiffré » in the summary and « sans clé d'accès » remain allowed.

**[RULE P9.13]** Targeted redesign, unmodified pages: the script only replaces the dashes (comma, colon or "from ... to"), with no other rewriting.

**[RULE P9.14]** Result pasted into `PREUVES.md`. 2 passes at most; what remains is corrected by hand, because a single hit fails the delivery (`principes.md`, principle 8).

**[RULE P9.15]** The final deliverable is in `<subfolder>/livraison/`, opened and verified in the requested format.

**[RULE P9.16]** Write to the lead, in the report, the history line for `profil.md` (delivery date, subject, deliverable, direction, palette, fonts, usage consumed), your observations and the feedback question to ask (grade, comments, follow-up given); the lead updates `profil.md`.

**[RULE P9.17]** `ETAT.md` of the work: PHASE = delivered, NEXT ACTION = "ask for the recipient's feedback (grade, comments, follow-up given)". The lead sets the project's line in `ETAT_COURANT.md` to "delivered on <date>: ask for feedback", marks the chat as finished if the application allows it, then proposes `/compact` for the project chat: everything is in `profil.md`, `ETAT_COURANT.md` and the subfolder.

## The final report

**[RULE P9.18]** The project chat writes `<subfolder>/livraison/rapport.md`, 10 lines at most:
1. Files delivered, with full path, in `<subfolder>/livraison/`.
2. Criteria grade and total of the 10 tests, before and after corrections, with the main corrections (reviewer's opinion; a non-independent audit is called a self-review); decision-maker's verdict: signs or not, and why.
3. Mode actually applied, lightenings made; the 3 strongest objections of the experts, and what you did with them.
4. Assumptions that remain, figures not found, skills absent.
5. What the person must complete (exact list of gaps if the file carries "version to complete"), fonts to install if any.
6. Contact sheet of thumbnails; in a redesign, before/after contact sheet.
7. What is to be noted in `profil.md`, usage consumed by this work.
8. For each check announced: VERIFIED, PARTIALLY VERIFIED, UNVERIFIED or UNAVAILABLE.

**[MUST P9.19]** Never "verified" for a check that did not run.

**[RULE P9.20]** The lead relays in 3 to 6 lines: the deliverable, the estimated grade, the decision-maker's verdict, what remains to be completed; they open the contact sheet (`open` or `start`) and the path of `rapport.md`; they say in one line what they noted ("I noted that...").
