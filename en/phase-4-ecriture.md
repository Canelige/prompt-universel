Who reads it, and when: `diapo-redacteur`, with `principes.md`, in phase 4 and for any later text correction (audit, redesign, mastery sheet); the project chat, at the entry of phase 4 (gate) and for "Lead: the phase 4 gate"; the phase 9 anti-AI script takes up its lists.

# Phase 4 · Writing (`diapo-redacteur`, in targeted review)

**[RULE P4.1]** The text is **final before layout**: `02_contenu.yaml` (titles, body, bottom lines, notes), `travail/oral.md`, the appendices and, later, `fiche_maitrise.md`.

**[MUST P4.2]** Any later text correction (audit, redesign) goes back through points 1 to 5, on the modified sentences only.

**[MUST P4.3]** **1. `humanizer` on every text, before any delivery.** The agent runs the `humanizer` skill on these texts, and `stop-slop` in In-depth; it lists the faulty sentences with their line number and corrects only those, never the whole. It writes in its status, for each file, "humanizer passed"; the gate refuses a text delivered without this line.

**[RULE P4.4]** **2. These two skills are written for English**: apply their principles without translating anything. The list below takes precedence; `stop-slop` does not remove the adverbs of a French text with figures.

**[MUST P4.5]** **3. Forbidden, checked by script: em dashes and en dashes** (aside: commas or parentheses; explanation: colon; range: « de 2020 à 2025 »).

**[MUST P4.6]** **French tics** (for a French deliverable): crucial, essentiel, incontournable, véritable, « clé » en adjectif, « enjeu » à chaque phrase, levier, synergie, au cœur de, s'inscrire dans, dans un contexte de, dans un monde où, il convient de, force est de constater, en outre, il est important de noter, « permettre de » en série, de manière significative, robuste, holistique, révolutionnaire, plonger.

**[MUST P4.7]** **In English, even in a French text**: delve, leverage, seamless, robust, crucial, landscape, tapestry, "in today's world".

**[RULE P4.8]** **Structures**: the forced triad, the repeated "not X but Y", the punchline sentence at the end of a paragraph.

**[RULE P4.9]** **4. Tone**: active verbs, concrete subjects ("the distributor imports", not "importation is ensured"), that of serious professionals (at school, of a group of serious students), not of a sales brochure.

**[RULE P4.10]** **5. French typography** (for a French deliverable): non-breaking space before ": ; ! ? %", inside the « » quotation marks, between a number and its unit, in thousands; typographic apostrophe.

**[MUST P4.11]** **6. Lead: the phase 4 gate.** You run the scripts; the writer runs none. In order: `python travail/calculs.py verifier` (a number of the YAML absent from `03_verification.md`, `donnees.csv` and `calculs.py`, or the figure of an A line vanished from the YAML, fails the phase, 2 passes at most), then, once the gate has passed and the phase 3 corrections are applied, `python travail/calculs.py geler`, which writes `travail/chiffres_geles.txt`: the freeze comes here and never at phase 3 (P3.26). `portes.py 4` also extracts the titles of `02_contenu.yaml` and compares them to `titres_seuls.txt`: each title added, removed or changed goes into `PREUVES.md`, then `titres_seuls.txt` is rewritten from the YAML.

**[MUST P4.12]** A later correction that changes a figure: first correct its line in `03_verification.md`, rerun `geler`, rerun the gate.

## Deliverable language

**[RULE P4.13]** Everything that is printed is in the language of the DELIVERABLE LANGUAGE rubric of `ETAT.md`: titles, footers, labels (FACT, ASSUMPTION and GAP in an English deliverable; FAIT, HYPOTHÈSE and LACUNE in a French one), fixed mentions of the modules ("single source", "not found", title of the Sources appendix), and the sources themselves: `build.py` prints the "Citation (deliverable language)" column of `03_verification.md` (`phase-3-faits.md`, P3.1), never the Source or Excerpt columns. A source is never printed in a language other than that of the deliverable. The HTML `lang` attribute, the glyph set tested (phase 5) and the typography checks (phase 7) follow the same language.

**[RULE P4.14]** **English deliverable**: what follows replaces the French tics of point 3 and the typography of point 5.

**[RULE P4.15]** **English punctuation**: no space before `:`, `;`, `?`, `!`; quotation marks “ ” and ‘ ’; comma for thousands, period for decimals.

**[MUST P4.16]** **Em dash and en dash forbidden in English too**: a range is written "from 60k to 91k"; the hyphen of a compound word (12-week) remains allowed.

**[RULE P4.17]** **`humanizer` and `stop-slop` apply directly**, without the adaptation of point 2 (`stop-slop` only in In-depth).

**[MUST P4.18]** **English tics**, checked by script, including at the final check of phase 9: delve, tapestry, landscape, pivotal, crucial, robust (except in the technical sense), leverage, seamless, holistic, synergy, game-changer, navigate the complexities, in today's fast-paced world, it is worth noting, moreover, furthermore, testament to, underscore, foster, unlock, elevate, embark, realm, ever-evolving, "not only... but also", and one-line conclusions that repeat the paragraph.

**[RULE P4.19]** The script checks words, not structures: reading catches "not X but Y".
