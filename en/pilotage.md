Who reads it, and when: the project chat, when it opens and at each resume; the lead, when relaying a stop or advising on usage. Never an agent.

# Steering: when you move on, when you stop

"You" here means the project chat; when the lead runs the project themselves (`demarrage.md`, "No separate chat possible"), it means them. Every message "to the person" goes through `travail/POUR_LE_CHEF.md` and the lead (`demarrage.md`, "The project chats").

## The stops

**[RULE PI.1]** **The phases:** 1 Framing; 2 Content; 3 Facts and figures; 4 Writing; 5 Art direction; 6 Production; 7 Checks; 8 Self-audit and corrections; 9 Delivery. You chain them without asking anything and you stop only in the five cases below (the installation and step 0 have their own stops).

**[RULE PI.2]** **A. Questions**, at startup: step C (`demarrage.md`), asked by the lead.

**[RULE PI.3]** **B. Preview**, end of phase 1. Write `travail/arret_B.md` with: the question and the answer, one sentence each; if your answer differs from the person's view, the gap and the figure that explains it; the list of titles; the expert's 3 strongest objections and what you did about them; the choices made in place of the person; the full path of the contact sheet of the 3 directions. Then, in `POUR_LE_CHEF.md`, in 6 lines at most: the essentials and two questions. The lead opens the contact sheet (`open` on Mac, `start` on Windows) and relays.
- Question 1: "I'm going with direction 1 with these titles?" a) yes; b) direction 2; c) direction 3; d) I'll correct the titles.
- Question 2, with the two first-hand collections, one line each (what, from whom, how many, how long), protocol ready in `travail/collecte/protocole.md`: "e) we do collection 1; f) collection 2; g) neither".
- Add: "Also read your usage and give me the two percentages."

**[MUST PI.4]** **The collection.** If the person does one, they drop the raw answers in `travail/collecte/` and write "collection dropped" to the lead before phase 7; you integrate it at the next stop C. You never write a collection result yourself.

**[RULE PI.5]** **Stop B in Express**: no contact sheet, you apply the energy from step C and the single retained direction; if the usage read at stop A is above 60%, stop B is kept, reduced to the titles and the usage reading; otherwise you send the titles to the lead and carry on without waiting.

**[RULE PI.6]** **C. Compaction**, at the end of phases 3 and 7, or after 8 mission briefs since the last compaction, or at delivery (phase 9), once no agent is running (all their statuses read): update `ETAT.md`, write stop C in `POUR_LE_CHEF.md`, then **end your turn**. The lead, for their part, proposes `/compact` in their own conversation at "New work" if their context exceeds 50%.

**[RULE PI.7]** **Stop C message**, which the lead passes on word for word: "Economy pause. Open the chat <title>, type `/compact keep the current phase, the person's decisions and the orders in progress`, then write 'continue' in it. Then read your usage and give me the two percentages."

**[RULE PI.8]** **D. Plan**: a gauge read exceeds 90%, or Claude Code announces a session or week limit. Update `ETAT.md`, write stop D to the lead, then end your turn. The lead writes: "I'm stopping to keep a margin. When the ring or `/usage` shows your plan has reset, come back and write: continue. We will resume at the NEXT ACTION."

**[RULE PI.9]** **An Opus-specific limit is not a stop D**, and it is the only exception to "the lead stays on Opus": the lead proposes to wait until the limit ends or to continue on Sonnet until then; note "lead on Sonnet" in `ETAT.md`; as soon as it passes, the lead asks to choose Opus again in the model selector.

**[RULE PI.10]** **E. Real block**: contradictory instructions, unreadable file, tool not found after installation; before phase 9, items that only the person knows (names of the team or the author, the school's or company's rule on AI). A short question to the lead, with choices or a list to fill in. Agents not found are not a stop: "Without agents", in one line.

**[RULE PI.11]** **Missing criteria are not a block**: write assumed criteria (`phase-1-cadrage.md`) and carry on.

**[RULE PI.12]** **Limit mid-turn**: nothing gets written, `ETAT.md` is authoritative at resume. An agent whose status is not `END: OK` is relaunched fresh, with "resume after the lines already written in <file>" (its identifier does not survive a new session).

## The usage thresholds

**[RULE PI.13]** Usage is a percentage already consumed, on the fullest gauge. If the app gives it to you, read it yourself and remove the request for percentages from messages A, B and C; otherwise the person gives it to the lead at those stops.

**[MUST PI.14]** Without a reading, never guess usage.

**[RULE PI.15]**
- **At startup**: the table of modes (`demarrage.md`, D).
- **Above 50%**: never a model change; you advise.
- **Above 70%**: lighten what follows in this order, stopping as soon as it is enough, and say so in one line: 1. phase 8 with the recipient, the decision-maker and the art director only (these three viewpoints stay in every mode: visual quality takes precedence over economy); 2. no second audit round; 3. web verification limited to weight A figures, decided from stop B (phase 3 is finished before the first stop C).
- **Above 90%**: stop D.

## Watching usage, and advising

**[RULE PI.16]** **Read the gauges yourself if you can** (a tool of the desktop app: 5 hours, week, per model, reset time, paid usage): at the opening of each session, at the start of each phase (before phase 8, the costliest, above all) and at each end of phase. Otherwise, the person's readings at stops A, B and C. Several project chats share the same gauges: the lead watches them for all of them.

**[RULE PI.17]** **The lead advises right away**, in one or two lines:
- **50%**: does what remains to do fit? Keep the mode or lighten it.
- **70%**: the lightening above.
- **85%**: propose a pause until the reset time (give the time), or finishing only the current phase.
- **Week above 80%**: keep the end of the week for urgent deliverables; big jobs and installations after the weekly reset (give the date).
- **A session's context window above 50%**: propose `/compact` at the next end of phase.

**[MUST PI.18]** **Paid usage enabled**: warn that anything beyond the plan is billed; never launch a phase that would trigger it without the person's explicit agreement.

**[RULE PI.19]** **At delivery**, give the lead the usage consumed by this work; they note it in the history of `profil.md`: it calibrates the mode of the next job.

## The project memory: `travail/ETAT.md`

**[RULE PI.20]** 40 lines at most, fixed rubrics: PHASE and TYPE (creation, full redesign, targeted redesign); MODE (Express or In-depth, and its basis: "time and usage" or "time only"); `DELIVERABLE LANGUAGE : <language>` (read from `00_materiel.md`, French by default: everything printed in the deliverable is in this language, `phase-4-ecriture.md`); PYTHON (path of the launcher); `WORKSHOP : <absolute path>` (root of the workshop); CHAT (title and group); USAGE (at each reading); `WEB PAGES READ : n / ceiling` (updated at each return of the fact-checker); PERSON'S DECISIONS (word for word, 6 lines at most); FILES (only those whose status is not `END: OK`); ORDERS IN PROGRESS (agent, identifier returned by the tool, expected file); MISSIONS SINCE LAST COMPACTION and MISSIONS TOTAL (numbers); `FULL RENDERS : n / 3` (PI.31); `PAGES PROMISED : <min> to <max>` (DE.27, checked by P6.23); PASSES (loop counters); TIME (start and end of each phase, read with the `date` command, never estimated); REMAINDER (accepted defects); NEXT ACTION (one exact sentence).

**[RULE PI.21]** Update it **before** launching an agent, **after** each end of phase and **after each deliverable file produced** (build, PDF, PPTX, Word).

**[RULE PI.22]** Scripts and agents write by absolute path: every shell command starts with `cd <WORKSHOP>` or uses only absolute paths.

**[RULE PI.23]** The `CLAUDE.md` imports the core, `profil.md` and `ETAT_COURANT.md`: they come back after a `/compact`, a `/clear` or a resume; a project chat finds its subfolder again through its compaction summary.

## Economy: the person has a Pro plan

**[RULE PI.24]** **This is the only place for the usage rules; they apply to all modes** (thresholds and advice above).

**[RULE PI.25]** **Two modes, Express and In-depth** (table of step D). In-depth: more than 6 h and the fullest gauge at 60% at most. Express: all other cases. Usage not read (PI.14 forbids guessing it): time alone decides, more than 6 h giving In-depth, written in `ETAT.md` ("MODE: In-depth, on time alone"). With more than 6 h, Express is never the default, even on a Pro plan: only a usage read above 60% imposes it.

**[MUST PI.26]** **Express cuts time and files, never quality.** It keeps the verification of decisive figures, the contact sheet looked at, the recipient, the decision-maker, the art director on the contact sheet and all the script checks; the economy comes from intermediate files, renders redone for nothing and rereads of big files. It never removes: the judging criteria, "nothing invented", the calculations by script, the overflow check, `humanizer` and the anti-tic list of phase 4.

**[RULE PI.27]** **The lead reads the minimum.** Never a big file: only `00_materiel.md`, script outputs, statuses, contact sheets, the sections drawn at random by the gate, and the short files they sign (`principes.md`, "The lead's posture").

**[RULE PI.28]** **The lead stays on Opus**, whatever the usage: they think, distribute, verify, decide (only exception: an Opus-specific limit, stop D). If the plan does not offer Opus, say so and continue on Sonnet. The same goes for each project chat.

**[RULE PI.29]** **The agents do the volume**: `diapo-*` on Sonnet, except `diapo-lecteur` (Haiku) and `diapo-expert` (the lead's model, Opus). Model fixed in their file: never pass them a `model` parameter, never launch an agent as a fork.

**[RULE PI.30]** **Mechanical work goes to Haiku** (`diapo-lecteur`): copies, readings, reading tests. What a script does is done by script, never by hand: sums, counts, dashes, page numbers, overflows, draws, choice of pages.

**[MUST PI.31]** **3 full renders of the deliverable at most**, first render and audit corrections included, **counted in `ETAT.md`** (`FULL RENDERS : n / 3`). `build.py` called without `--pages` reads this counter, refuses a fourth render ("full render ceiling reached") and increments it before rendering; the gate of each phase compares the counter with the full PDFs of `travail/rendus/`, timestamped, and a mismatch fails the gate. After that, only the faulty pages are rendered ("Loop ceilings") and replace their pages in the delivered PDF with PyMuPDF (`insert_pdf`), outside the counter, then `livrable.txt` is regenerated (recipe: `phase-6-fabrication.md`, P6.2). Images are looked at in contact sheets of 6 pages; a page is opened full size only if a script or a contact sheet flags it; after a correction, only the modified pages are rendered.

**[RULE PI.32]** **Before launching a render, announce the usage you estimate** (in % of session and of week).

**[TIP PI.33]** Measured cost of an Express render (trial no. 6, A4 of 10 pages, 13 sheets): 1 h 17; 17 agents; 2 full renders; 10 web pages; 68 million tokens processed of which 21 in Opus, 46 in Sonnet, 1.4 in Haiku (4.4 million excluding cache reads); the builder weighs more than half of the agents, the lead nearly a third. **The measure is tokens processed** (input, cache write and read, output), read in the `subagents/agent-<id>.jsonl` logs (calls deduplicated by message identifier) and in your own, **not the context size given by the end-of-agent notification**, which only gives the size of the last call. **A subagent costs about 100,000 tokens from its first call** (starting context loaded by the tool): in Express, a single Haiku reader for the whole screen test (P7.19), never one per batch. This render moved the 5-hour gauge of a Team plan from 53% to 72% and the week from 16% to 19%, other chats running in parallel (upper bound: the render alone cost less).

**[RULE PI.34]** **A long conversation costs at every resume** (all the context is reread in Opus): as soon as a job is delivered, the lead proposes `/compact` of the project chat; the state is in `profil.md`, `ETAT_COURANT.md` and the subfolder. Outside a job (advice, discussion), the lead answers briefly.

**[RULE PI.35]** **Mission brief, 8 lines at most**: the role; the module to read (absolute path in `universel/`) and its useful `###` subsection rather than a whole module; the files to read and to write, by path; the path of the status; the path of the Python launcher; the prohibitions; the answer ceiling, 6 lines. Never your reasoning.

**[RULE PI.36]** **Heavy skills** (`impeccable`, `pptx`, `frontend-slides`, `ui-ux-pro-max`, `marketing-skills`) are loaded in the agent that uses them, never in your context.

**[RULE PI.37]** `marketing-skills`: `diapo-expert` and `diapo-redacteur`, when the field touches marketing, strategy or sales. They load the one or two useful methods (`marketing-plan`, `pricing`, `competitor-profiling`, `customer-research`, `product-marketing`, `launch`) as a rigor grid, never as a source of figures. The tools of the reference come before them.

**[RULE PI.38]** `ui-ux-pro-max`: `diapo-fabricant`, in phase 5, as an extra catalog for palettes, font pairings and chart types. It never comes before the subject, the brand, taste and "beautiful first".

## What Express changes, in one place

**[RULE PI.39]** Target: 1 h to 1 h 30.

| Phase | In Express |
|---|---|
| 1 | Short ghost deck; only the 2 most decisive figures are cross-checked by two sources; the title test and the expert counter-review stay. |
| 2 | 5 rigor pieces at most (plus the pieces required by the case). |
| 3 | 10 web pages read at most (P3.15), A lines only (pricing pages of a proposal: `phase-3-faits.md`). |
| 4 | `humanizer` alone, without `stop-slop`. |
| 5 | No contact sheet of directions: the energy chosen at step C takes its place, the rest of the direction is chosen by reasoning ("Anti-generic"). 5 layout templates at most, 2 font families. |
| 6 | PDF only, plus the PPTX if the instructions require it. |
| 7 | Script checks and screen test, within the render ceiling. A check contact sheet is allowed right after the first PDF, in addition to the one after the corrections. |
| 8 | The recipient and the decision-maker, plus the art director in a single pass (the fresh look at the contact sheet, without `05_charte.md`). |
| 9 | Full checklist. |

**[RULE PI.40]** **Express files**: six, `ETAT.md`, `01_cadrage.md` (with the titles and the counter-review), `02_contenu.yaml`, `03_verification.md`, `build.py` and the deliverable. `build.py` also carries the style charter (editorial thesis and roles table as a header comment, tokens, layout templates) and the phase 7 checks, as functions: in Express, "`05_charte.md`", "`tokens.css`" and "`gabarits.css`" mean this comment and these functions, and the art direction chosen without a contact sheet (table above, phase 5) is also written there: no `direction_express.md`. No separate `controles.py` or `fiche_maitrise.md`: the sheet is the last section of `03_verification.md`, your hostile review (`revue_chef.md`, always written) a section of `01_cadrage.md`.

**[RULE PI.41]** Still allowed in Express, because a rule has a script, an agent or a fresh reader read them: `statuts/`, `portes.py`, `calculs.py`, `chiffres_geles.txt`, `donnees.csv`, `credits.md`, `titres_seuls.txt`, `objections.md` (your answers to the objections, required by P1.25 and read by the gate, PI.44), `prep_audit.py` (copies by script what the auditors receive, P8.9), `PREUVES.md`, `POUR_LE_CHEF.md`, `REPONSES.md`, `audit/`, and `tirer.py` with its seed if a draw remains.

## Verifying without rereading

**[RULE PI.42]** **The statuses.** Each agent keeps `travail/statuts/<phase>_<nom>.txt`, on 3 lines: AGENT, READ, END. Without `END: OK`, a piece of work is not delivered, but the lines written remain: resume after them.

**[RULE PI.43]** A cut-off agent is resumed, not relaunched from zero: SendMessage with the identifier noted in ORDERS IN PROGRESS, "continue from what exists". Identifier missing or new session: fresh agent with "files already exist; read them, complete them, do not rewrite what is done".

**[RULE PI.44]** **The gate.** `python travail/portes.py <phase>` is a script that grows with the work. Phase 1, you write it with only the phase 1 checks: each criterion has its page, each title fits within its word limit, each objection has its answer in `objections.md`. At the entry of phases 2, 3 and 4, after reading their module, add their numbered rules to it. The rules of phases 5 and 6 live in `travail/controles.py`, written by `diapo-fabricant`.

**[RULE PI.45]** Test each check on a deliberately faulty file before using it.

**[RULE PI.46]** **The spot check.** `portes.py` draws 3 sections of the rendered file at random and displays them; you read them in full (the draw is not done by you).

**[RULE PI.47]** Gate and spot check go in `travail/PREUVES.md`, one line per section: "read, nothing to report" or "read, defect X".

## Loop ceilings

**[RULE PI.48]**

| Where | Ceiling | Then |
|---|---|---|
| Gate failing, any phase | 1 return to the agent, with the exact list of defects | defect under REMAINDER, carry on |
| Title test (phase 1) | 2 passes | keep the best version |
| Phase 4 gate | 2 passes | REMAINDER |
| Full renders of the deliverable (first render and audit corrections included, all modes) | 3 ("Economy"); after that, only the faulty pages are rendered, in 3 check passes at most; stop if the defects do not go down | REMAINDER |
| Auditor report refused (phase 8) | 1 relaunch | REMAINDER |
| Gap found by the fact-checker (phase 8) | 1 gap: fix the line and reopen 5 lines of the same type. 2 gaps: a single relaunch of phase 3, limited to the A lines | REMAINDER |
| Agent cut off or status PARTIAL | 2 resumes, each with the list of what is missing | the missing part under REMAINDER |
| Total missions of the job (`MISSIONS TOTAL` of its `ETAT.md`) | 45; beyond that, only phases 8 and 9 still launch an agent | REMAINDER, announced to the lead |
| Phase 8 corrections | 1 round, then a targeted re-check; a second full round only in In-depth, once | REMAINDER, with its effect on the grade |

**[TIP PI.49]** A deliverable with its defects announced beats an endless loop.

## Without agents

**[RULE PI.50]** **Tool without agents, or `diapo-*` agents not found after the installation**: do each mission yourself, in order, with the same files; each role file carries "simulated role, not independent" at the top, repeated in its status; between two roles, reread only the previous role's file and the module of this role.

**[MUST PI.51]** **Simulated roles are not independent.** Title test, counter-review and audit, in this order:
1. a generic subagent of the tool, with only the file to read (`audit/` for the audit);
2. otherwise a new chat in the same folder, which the person opens with: "Read only audit/ and apply audit/consignes_audit.md, angle <angle>. Write audit/rapport_<angle>.md and audit/statut_<angle>.txt. End with the list of files read.";
3. otherwise yourself: the report states "non-independent audit", the grade is a self-review, never a reliable estimate.
