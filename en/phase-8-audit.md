Who reads it, and when: the project chat, in phase 8, to prepare `audit/`, launch the auditors and arbitrate; the auditors never read it directly: a script copies "What each one does" (without the "Lead:" blocks) and `principes.md` into `audit/consignes_audit.md`.

# Phase 8 · Self-audit, then corrections (`diapo-auditeur`, Sonnet)

**[TIP P8.1]** **Limits**: the auditor is the same model as the writer, with the same blind spots; the gain comes from isolation and from the obligation to provide proof.

**[MUST P8.2]** The grade is a reviewer's opinion, never a forecast.

## Preparation, by script

**[RULE P8.3]** `audit/` contains only: the PDF and `livrable.txt`; `titres.txt` (the titles alone, in order, extracted by script from `02_contenu.yaml` at the time of the audit, never copied from `titres_seuls.txt`); `consignes_originales.txt` (brief, question, constraints, excerpts of the original document); `criteres_originaux.txt`, extracted from the original document and not from your copy (assumed criteria: `criteres_presumes.txt`, label at the top, total announced "on assumed criteria"); the pages of the reference and of the case cited in `01_cadrage.md` and the CASE lines; the contact sheet of thumbnails; `objections_phase1.txt` (the 5 objections of `01_contre_expertise.md`, **without your answers**); `reference_plan.txt` (outline of the reference, tools expected from `00_materiel.md`); `consignes_audit.md` (copy of `principes.md` and of "What each one does", without the "Lead:" blocks).

**[RULE P8.4]** **In addition, depending on the auditor.** **Fact-checker**: `03_verification.md`, `donnees.csv`.

**[RULE P8.5]** **Art director**: 6 pages in large size chosen by script (cover, summary, 2 charts, 1 break, decision); reduced and gray versions; `interdits.txt` ("What gives away AI" from `direction-artistique.md` and reflex fonts from `annexe-polices.md`, extracted by script); `05_charte.md`, only in a second step.

**[RULE P8.6]** **Jury or devil's advocate**: the case brief and the role the instructions give them.

**[RULE P8.7]** **Decision-maker**: `decideur.txt` (copied by script from the reader in `01_cadrage.md`) and, if there is a brand, its logo and official colors. Never the deliverable's charter.

## Launch

**[RULE P8.8]** The auditors start **in a single message**, in parallel, each with its angle (`destinataire`, `verificateur`, `direction-artistique`, `contradicteur`, `decideur`), the expert (`diapo-expert`) in the same message. Without agents: `pilotage.md`, "Without agents".

**[MUST P8.9]** Everything an auditor receives is copied by script into `audit/`, never cited by its path in `travail/`.

**[RULE P8.10]** Order: "Read only `<subfolder>/audit/`, plus the web pages you must reopen. Write `<subfolder>/audit/rapport_<angle>.md` and `<subfolder>/audit/statut_<angle>.txt`. End with the list of files read."

**[MUST P8.11]** **Isolation check**: before reading a report, `python <subfolder>/travail/portes.py isolement <id>` opens the agent's log (`~/.claude/projects/*/*/subagents/agent-<id>.jsonl`) and lists every tool call whose input contains a path outside `<subfolder>/audit/`: `travail`, `profil`, `ETAT_COURANT`, `universel`, `UNIVERSAL_PROMPT` or the name of another subfolder. **The script reads only the paths accessed**: the `file_path`, `path` and `notebook_path` fields of the tool inputs, and, for a `Bash` command, the tokens that are paths (starting with `/`, `~` or `./`, or following `cd`); **never the written content** (`content`, `new_string`, text of a report or of a script), where a word like "profil" is not an access. A name counts only as a whole path component. Call listed: report refused (a single rerun; refused twice, set aside and flagged under REMAINDER).

**[RULE P8.12]** Log not found: "isolation not verified" in the report. The list of files read declared by the agent proves nothing: only the log counts.

## What each one does

**[MUST P8.13]** **The recipient** (professor, client, manager or jury, from the reader in `01_cadrage.md`) grades severely, out of 20 in all contexts. Starting point: 12/20, the class average or a correct deliverable that nobody remembers; a criterion goes up only on cited proof (page and figure). Ceilings: question not addressed 8/20; recommendation missing or contradicted by the figures 10/20; invented figure 12/20. Per criterion: grade, proof, what is missing for the next tier.

**[RULE P8.14]** Then **10 tests**, graded 0 (absent), 1 (present but unproven) or 2 (present, with the page that proves it):
1. **Answer first**: the first page gives the answer, 3 reasons and its key proof.
2. **Titles alone**: from `titres.txt`, the argument in 5 lines, and the place where it breaks.
3. **"So what?"**: pages whose bottom line repeats the title or has no consequence.
4. **Alternatives**: at least two, plus the status quo, with the quantified reason for the choice.
5. **Decisive figures**: they identify for themselves the 3 to 5 that carry the decision; dated, right scope, cross-checked?
6. **Assumptions, sensitivity and unknowns.**
7. **Objection**: written, with a quantified answer.
8. **Risks**: probability, quantified impact, signal, countermeasure.
9. **Executable**: owner, deadline, deliverable, indicators, stopping criterion.
10. **Consistency**: same figure, same vocabulary, same decision everywhere, no unfavorable data set aside.

**[RULE P8.15]** Test at 0: SEVERE point; test at 1: MEDIUM point; test that the criteria and the field do not call for: "not applicable". Total of the tests scaled to 20, reported separately from the criteria grade.

**[RULE P8.16]** **Tier 17**: above 15/20 on a criterion, three proofs, each with its page, otherwise ceiling at 15. 1. **Mastered reference**: useful notions from `reference_plan.txt` used with their exact definition, missing ones listed. 2. **Reference surpassed**: limit of a tool of the reference discussed for this case. 3. **Scholarly support**: two references (author, year), each tied to an argument.

**[RULE P8.17]** **Refutation**: in 5 lines, the best reason to reject the recommendation; without an answer in the deliverable: SEVERE. **The 3 most dangerous questions**: a question without an answer in the deliverable is a MEDIUM point.

**[MUST P8.18]** **The fact-checker** redoes every calculation; reopens the URL of the A figures and of 3 lines drawn by script (a gap triggers the loop ceilings rule); lists the displayed figures absent from the table and everything presented as a FACT without being one; makes **a pass for contradictions between pages** (a rule or figure stated twice differently, for example a threshold in points on one page and in percent on another), with both pages.

**[MUST P8.19]** **The art director** (skill `impeccable`), in two steps; they write the first before opening `05_charte.md`.
1. **Fresh eye**: 3 mood words and what the deliverable recalls; each forbidden item encountered, with page and excerpt; focal point of each page in large size; legibility on reduced and gray versions (no information on color alone); first element read in one second on each page in large size, and pages where two elements fight for that rank; cover and divider without their text (what remains of identity); blanks that are endured rather than intended, edges offset for no reason; the 3 weakest pages.
2. **Gaps against the charter**, after reading `05_charte.md`, and whether its 3 words match those of the direction.

**[RULE P8.20]** A forbidden item from `interdits.txt`, or a fresh eye that says "clean, neutral, generic": SEVERE.

**[MUST P8.21]** **The field expert** (`diapo-expert`, role drawn from the table of the field profile, `phase-1-cadrage.md`) reads as that professional: what is wrong, naive or unprofessional (vocabulary, orders of magnitude, practices, regulation); what they would do differently, and why; is the strongest objection of the expert counter-review properly handled? A point that is wrong in the trade: SEVERE.

**[RULE P8.22]** **The devil's advocate, or the jury** (if the instructions have them play this role, and always in In-depth): what they would refuse to sign, the worst assumption, a pre-mortem.

**[MUST P8.23]** **The decision-maker** (`diapo-auditeur`, angle `decideur`, in all modes, Express included) plays the decision-maker of the case: the marketing director of the brand concerned if there is a brand, otherwise the decision-maker that the framing named. They see the deliverable as the one who must sign, the client choosing the agency; they review it discreetly, never interrupting the person, and the lead applies their corrections like those of the others. They return: the impression of the first 30 seconds (color, energy, "do I recognize myself?"); what builds trust and what raises doubt; "do I sign?"; the 3 changes that would convince them.

**[RULE P8.24]** With a brand, "I don't recognize myself" or "it doesn't look like us" is SEVERE; the decision-maker also checks the brand voice (logo masked).

**[MUST P8.25]** Every finding cites the page, an excerpt and the criterion affected; a finding without a citation is deleted.

## Lead: who audits depending on the mode

**[MUST P8.26]** **The three views, in all modes**: the recipient, the art director and the decision-maker. Express: these three, the art director in a single step (the fresh eye); the phase 1 expert remains mandatory, the phase 8 one is skipped. In-depth: all six.

## Lead: arbitration

**[MUST P8.27]** Accuracy first: a wrong figure or a source that cannot be found is corrected or leaves, whatever the criteria. Then the criteria, then the charter: a criterion that the correction leaves without a page is covered otherwise (qualitative proof, quantified ASSUMPTION) and flagged. Each arbitration fits on one line.

## Lead: corrections

**[MUST P8.28]** Every SEVERE or MEDIUM point is handled; a MINOR point that is set aside gets a line of reason.

**[RULE P8.29]** Rerun the gates of phases 4 and 7 on the modified pages only; any modified text goes back through `humanizer` (`phase-4-ecriture.md`).

**[RULE P8.30]** Render the modified pages again (full render only if any remain within the ceiling) and `grep` each old figure in the whole text of the deliverable. The auditor concerned rechecks only the corrected points; the "after" grade is theirs, re-estimated on those points, announced as such.

**[RULE P8.31]** The rest follows the loop ceilings (`pilotage.md`).
