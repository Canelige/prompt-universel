Qui le lit, et quand : `diapo-redacteur`, avec `principes.md`, en phase 4 et pour toute correction de texte ultérieure (audit, refonte, fiche de maîtrise) ; la discussion de projet, à l'entrée de la phase 4 (porte) et pour « Chef : la porte de la phase 4 » ; le script anti-IA de la phase 9 reprend ses listes.

# Phase 4 · Écriture (`diapo-redacteur`, en relecture ciblée)

**[RÈGLE P4.1]** Le texte est **final avant la mise en page** : `02_contenu.yaml` (titres, corps, lignes du bas, notes), `travail/oral.md`, les annexes et, plus tard, `fiche_maitrise.md`.

**[IMPÉRATIF P4.2]** Toute correction de texte ultérieure (audit, refonte) repasse par les points 1 à 5, sur les seules phrases modifiées.

**[IMPÉRATIF P4.3]** **1. `humanizer` sur chaque texte, avant toute livraison.** L'agent passe la compétence `humanizer` sur ces textes, et `stop-slop` en Approfondi ; il liste les phrases fautives avec leur numéro de ligne et ne corrige que celles-là, jamais l'ensemble. Il écrit dans son statut, pour chaque fichier, « humanizer passé » ; la porte refuse un texte livré sans cette ligne.

**[RÈGLE P4.4]** **2. Ces deux skills sont écrites pour l'anglais** : applique leurs principes sans rien traduire. La liste ci-dessous prime ; `stop-slop` ne supprime pas les adverbes d'un texte français chiffré.

**[IMPÉRATIF P4.5]** **3. Interdit, contrôlé par script : les tirets longs et demi-tirets** (incise : virgules ou parenthèses ; explication : deux-points ; intervalle : « de 2020 à 2025 »).

**[IMPÉRATIF P4.6]** **Les tics français** : crucial, essentiel, incontournable, véritable, « clé » en adjectif, « enjeu » à chaque phrase, levier, synergie, au cœur de, s'inscrire dans, dans un contexte de, dans un monde où, il convient de, force est de constater, en outre, il est important de noter, « permettre de » en série, de manière significative, robuste, holistique, révolutionnaire, plonger.

**[IMPÉRATIF P4.7]** **En anglais, même dans un texte français** : delve, leverage, seamless, robust, crucial, landscape, tapestry, « in today's world ».

**[RÈGLE P4.8]** **Les structures** : la triade forcée, le « pas X mais Y » à répétition, la phrase-chute en fin de paragraphe.

**[RÈGLE P4.9]** **4. Le ton** : verbes actifs, sujets concrets (« le distributeur importe », pas « l'importation est assurée »), celui de professionnels sérieux (à l'école, d'un groupe d'étudiants sérieux), pas d'une plaquette commerciale.

**[RÈGLE P4.10]** **5. La typographie française** : espace insécable avant « : ; ! ? % », à l'intérieur des guillemets « », entre un nombre et son unité, dans les milliers ; apostrophe typographique.

**[IMPÉRATIF P4.11]** **6. Chef : la porte de la phase 4.** `python travail/calculs.py verifier` : un nombre nouveau ou disparu fait échouer la phase, 2 passes au plus. `portes.py 4` extrait aussi les titres de `02_contenu.yaml` et les compare à `titres_seuls.txt` : chaque titre ajouté, retiré ou changé va dans `PREUVES.md`, puis `titres_seuls.txt` est réécrit depuis le YAML.

**[IMPÉRATIF P4.12]** Une correction ultérieure qui change un chiffre : on corrige d'abord sa ligne dans `03_verification.md`, on relance `geler`, on relance la porte.

## Langue du livrable

**[RÈGLE P4.13]** Tout ce qui s'imprime est dans la langue de la rubrique LANGUE de `ETAT.md` : titres, pieds de page, étiquettes (en anglais, FAIT, HYPOTHÈSE et LACUNE deviennent FACT, ASSUMPTION et GAP), mentions fixes des modules (« source unique », « non trouvé », titre de l'annexe Sources), et les sources elles-mêmes : `build.py` imprime la colonne « Citation (langue du livrable) » de `03_verification.md` (`phase-3-faits.md`, P3.1), jamais les colonnes Source ou Extrait. Une source ne s'imprime jamais dans une autre langue que celle du livrable. L'attribut `lang` du HTML, le jeu de glyphes testé (phase 5) et les contrôles de typographie (phase 7) suivent la même langue.

**[RÈGLE P4.14]** **Livrable en anglais** : ce qui suit remplace les tics français du point 3 et la typographie du point 5.

**[RÈGLE P4.15]** **Ponctuation anglaise** : pas d'espace avant `:`, `;`, `?`, `!` ; guillemets “ ” et ‘ ’ ; virgule pour les milliers, point pour les décimales.

**[IMPÉRATIF P4.16]** **Tiret long et demi-tiret interdits aussi en anglais** : un intervalle s'écrit « from 60k to 91k » ; le trait d'union d'un mot composé (12-week) reste permis.

**[RÈGLE P4.17]** **`humanizer` et `stop-slop` s'appliquent directement**, sans l'adaptation du point 2 (`stop-slop` seulement en Approfondi).

**[IMPÉRATIF P4.18]** **Tics anglais**, contrôlés par script, y compris au contrôle final de la phase 9 : delve, tapestry, landscape, pivotal, crucial, robust (sauf sens technique), leverage, seamless, holistic, synergy, game-changer, navigate the complexities, in today's fast-paced world, it is worth noting, moreover, furthermore, testament to, underscore, foster, unlock, elevate, embark, realm, ever-evolving, « not only… but also », et les conclusions d'une ligne qui répètent le paragraphe.

**[RÈGLE P4.19]** Le script contrôle les mots, pas les structures : la lecture attrape « not X but Y ».
