Who reads it, and when: `diapo-verificateur`, with `principes.md`, in phase 1 (decisive figures of the ghost deck) and in phase 3; the project chat, at the entry of phase 3 (gate) and for "Lead: the phase 3 gate".

# Phase 3 · Facts and figures (`diapo-verificateur`)

**[RULE P3.1]** The agent continues `travail/03_verification.md`, line by line, without redoing lines that are already locked. The "Citation (deliverable language)" column gives the source mention exactly as it will be printed (under the figure and in the Sources appendix, in the format of `phase-9-livraison.md`, P9.6), written in the `DELIVERABLE LANGUAGE` of `ETAT.md`, whatever the language of the rest of the table: `build.py` prints it as is, without translating it or recomposing it from the other columns. A source is never printed in a language other than that of the deliverable.

| # | Claim | Type | Weight | Verdict | Source (organization, date, URL read; or document and page; or collection file; or script) | Excerpt (15 words max, for EXTERNAL and CASE) | Citation (deliverable language) | AGAINST (A lines) |
|---|---|---|---|---|---|---|---|---|

## Types of evidence

**[RULE P3.2]** **EXTERNAL**: a market, a real company, a law; dated primary source.

**[MUST P3.3]** **CASE**: data supplied by the recipient (the professor's case, the client's or company's data, appendix, call for tenders). It is authoritative: document and page cited, consistency checked only. It never leaves the deliverable for lack of a web source.

**[RULE P3.4]** **PRIMARY**: data produced by the person, with sample size, date, recruitment and limitation; raw answers in `travail/collecte/`.

**[MUST P3.5]** **TESTIMONY**: a lived or observed example, written "we observed...". It illustrates, but never proves a figure or a trend.

**[RULE P3.6]** **CALCULATION**: redone in `travail/calculs.py`, on unrounded values.

**[RULE P3.7]** **ASSUMPTION**: goes to the register.

## Sources

**[MUST P3.8]** **Most recent source first.** For an EXTERNAL fact or figure, look for the most recent source, published at most 2 years ago; go further back only if nothing recent exists, or for data that does not age (a law in force, a founding date, a reference cultural score). The year stays displayed next to the figure and the Source column says why: "no source since <year>". CASE data keeps the date of the case.

**[RULE P3.9]** **Balance of evidence.** To compare options (countries, scenarios, partners), each option gets at least one dated piece of evidence for each decisive criterion; the page ceiling is shared among them, and the tools reserve (P3.15) guarantees a source per tool and per option. An undated source is accepted with its reading date ("undated, read on <date>").

**[MUST P3.10]** **Weight.** **A**: if it varies by 20%, the decision changes; verified first, cross-checked by two sources, plausibility test against an independent benchmark. **B**: changes a title or a chart. **C**: a detail.

**[MUST P3.11]** **A line: contrary search.** Look for the data that would contradict the figure or the title (the "What would make it false" column of the ghost deck, the expert's objections); AGAINST notes the source found and its value, or "nothing on N pages read". A contrary datum that is found appears in the deliverable, with its treatment.

**[MUST P3.12]** **Excerpt copied, not summarized**: the instruction passed to WebFetch asks for the exact sentence that contains the figure, word for word. `portes.py` downloads each A source (urllib, or PyMuPDF for a PDF) and looks for the number, after normalizing spaces, commas and periods: found, CONFIRMED stands; page inaccessible, EXCERPT ONLY; absent, the line goes back to the fact-checker.

**[MUST P3.13]** **Legal text**: Légifrance, Judilibre or EUR-Lex, the version in force at the date of the facts; a ruling carries its court, its chamber, its date and its number. A reference that is not found leaves the deliverable: never an ASSUMPTION for a rule of law.

**[RULE P3.14]** **Page read**: a page opened successfully. Failures (403, 404, unreadable page) do not count, within a limit of 2 times the ceiling in attempts; searches do not count either. Data read by script, API or CSV (World Bank, OECD, Eurostat...) do not count either: for a table of figures, go that way, because WebFetch only returns a summary of it.

**[RULE P3.15]** **Ceiling of pages read: one ceiling per required tool, never a fixed 10** (trial no. 7 emptied the market analysis with 10 pages: a 2-factor PESTEL, a Porter with no data, culture without sources; grade 14.25 out of 20 instead of 17). The lead computes it before phase 1 and writes it in `WEB PAGES READ : n / ceiling` of `ETAT.md`. **Express: 6 pages for the A lines, plus 2 pages per tool required by the reference** (`00_materiel.md`: PESTEL, Porter, culture, etc.), or as many pages as there are compared options if there are more than 2: `6 + tools × max(2, options)`, from 10 at least to 30 at most. **In-depth: 40, or this computation if larger, 60 at most.** **The tools reserve** (`tools × max(2, options)` pages) is never spent on the A lines: each required tool has at least one dated source per option (P3.9). A tool whose facts are in the case (CASE, P3.3) gets no page. Each line drawn from a tool starts with `[TOOL: name]` in the Claim column, and the phase 3 gate refuses a tool or an option without a source. The count (web pages only) is in the `WEB PAGES READ` line of `ETAT.md`. **The pricing pages of a proposal (phase 2 budget) count separately: 4 at most.**

**[MUST P3.15b]** **Tool calls of the fact-checker, in Express.** The mission brief sets a ceiling of tool calls per mission, shown like the builder's (P6.27): **10 calls plus 2 per page the mission may read** (6 pages in phase 1: 22; the 22 remaining pages of a ceiling of 28 in phase 3: 54). At that number he stops and writes `FIN: PARTIEL`; the lines not examined become NOT VERIFIED (P3.16). The lead relaunches only once, for the remaining A lines alone, with 10 more calls. Reads by script count like any call. Measure of trial no. 7, with no ceiling: 2 missions, 106 calls, 14.8 million tokens processed, the first item of the render.

## Verdicts

**[MUST P3.16]** **EXTERNAL**: CONFIRMED (page opened, excerpt present); SINGLE SOURCE (A figure not cross-checked: usable, flagged by "single source" under the figure or in the Sources appendix); CORRECTED; CONTRADICTED (range displayed, retained value); EXCERPT ONLY (page unreadable or blocking robots, valid verdict); NOT FOUND (an A figure becomes an ASSUMPTION, the others leave); UNVERIFIED (ceiling reached, label "estimate", never FACT).

**[RULE P3.17]** **CASE**: MATCHES THE CASE; a more recent web source that contradicts it does not replace it: note "[source] gives [value] in [year]".

**[RULE P3.18]** **PRIMARY**: MATCHES THE COLLECTION. **CALCULATION**: RECALCULATED. **ASSUMPTION** and **TESTIMONY**: no verdict.

## The rules

**[RULE P3.19]** Primary source (a blog is a "sector estimate"); the reference gives the method, never a market fact; a figure more than 3 years old: year displayed; no mixed years or scopes.

**[RULE P3.20]** Sound statistics (margin of error, sample size, significant gap), computed by the Agency agent `Statistician` if it is installed, with `model: sonnet`.

**[MUST P3.21]** **One figure everywhere**: a corrected figure is corrected in all its occurrences, a `grep` proves it.

**[MUST P3.22]** A real company cited as a partner is a candidate, never "has accepted".

**[RULE P3.23]** **Two scholarly references** (tier 17): two academic or professional references tied to an argument (Google Scholar, Cairn, HAL, professional journal), verified like an EXTERNAL line, with author, year, title.

**[RULE P3.24]** **The files**: the agent writes `travail/calculs.py` and `travail/donnees.csv` without running anything; the lead runs the scripts (`calculs.py`, `portes.py`, `geler`, `verifier`): neither the writer nor the fact-checker runs one, nor edits a gate file (`objections.md`) to pass it.

**[RULE P3.25]** `calculs.py` has two commands, `geler` and `verifier`; `geler`, run by the lead at the phase 4 gate (P4.11) and never before, collects, **in `02_contenu.yaml` only** (never in `donnees.csv`, whose values are not text and would give false gaps at the phase 4 gate), the numbers that carry a unit, a symbol (%, €, $) or a year (not frozen: integers from 1 to 10 without a unit, page numbers, days of a date). `donnees.csv`: one line per value displayed in a chart (series, value, unit, year, identifier of the verification line). Before the freeze, `verifier` compares each number of this kind in the YAML with `03_verification.md`, `donnees.csv` and the outputs of `calculs.py`; after the freeze, it also compares with `chiffres_geles.txt`.

**[RULE P3.26]** **Lead: the phase 3 gate.** No A line without a verdict; no displayed line without "Citation (deliverable language)"; reread the excerpt of 3 A lines drawn by `portes.py`; count, per tool and per option, the `[TOOL: name]` lines (P3.15). **Freeze nothing**: the CORRECTED and CONTRADICTORY verdicts change figures of the YAML in phase 4, the freeze comes after (P4.11). Then, **stop C**.
