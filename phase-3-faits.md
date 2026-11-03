Qui le lit, et quand : `diapo-verificateur`, avec `principes.md`, en phase 1 (chiffres décisifs du ghost deck) et en phase 3 ; la discussion de projet, à l'entrée de la phase 3 (porte) et pour « Chef : la porte de la phase 3 ».

# Phase 3 · Faits et chiffres (`diapo-verificateur`)

**[RÈGLE P3.1]** L'agent continue `travail/03_verification.md`, ligne par ligne, sans refaire les lignes déjà verrouillées. La colonne « Citation (langue du livrable) » donne la mention de source telle qu'elle s'imprimera (sous le chiffre et dans l'annexe Sources, au format de `phase-9-livraison.md`, P9.6), écrite dans la `LANGUE DU LIVRABLE` de `ETAT.md`, quelle que soit la langue du reste du tableau : `build.py` l'imprime telle quelle, sans la traduire ni la recomposer depuis les autres colonnes. Une source ne s'imprime jamais dans une autre langue que celle du livrable.

| # | Affirmation | Type | Poids | Verdict | Source (organisme, date, URL lue ; ou document et page ; ou fichier de collecte ; ou script) | Extrait (15 mots max, pour EXTERNE et CAS) | Citation (langue du livrable) | CONTRE (lignes A) |
|---|---|---|---|---|---|---|---|---|

## Les types de preuve

**[RÈGLE P3.2]** **EXTERNE** : un marché, une vraie entreprise, une loi ; source primaire datée.

**[IMPÉRATIF P3.3]** **CAS** : donnée fournie par le destinataire (cas du professeur, données du client ou de l'entreprise, annexe, appel d'offres). Elle fait foi : document et page cités, cohérence contrôlée seulement. Elle ne sort jamais du livrable faute de source web.

**[RÈGLE P3.4]** **PRIMAIRE** : donnée produite par la personne, avec effectif, date, recrutement et limite ; réponses brutes dans `travail/collecte/`.

**[IMPÉRATIF P3.5]** **TÉMOIGNAGE** : exemple vécu ou observé, écrit « nous avons observé… ». Il illustre, mais ne prouve jamais un chiffre ni une tendance.

**[RÈGLE P3.6]** **CALCUL** : refait dans `travail/calculs.py`, sur les valeurs non arrondies.

**[RÈGLE P3.7]** **HYPOTHÈSE** : va au registre.

## Les sources

**[IMPÉRATIF P3.8]** **La source la plus récente d'abord.** Pour un fait ou un chiffre EXTERNE, cherche la source la plus récente, publiée il y a 2 ans au plus ; ne remonte plus loin que si rien de récent n'existe, ou pour une donnée qui ne vieillit pas (une loi en vigueur, une date de création, un score culturel de référence). L'année reste affichée à côté du chiffre et la colonne Source dit pourquoi : « aucune source depuis <année> ». Une donnée CAS garde la date du cas.

**[RÈGLE P3.9]** **L'équilibre des preuves.** Pour comparer des options (pays, scénarios, partenaires), chaque option reçoit au moins une preuve datée pour chaque critère décisif ; le plafond de pages se répartit entre elles, et la réserve des outils (P3.15) garantit une source par outil et par option. Une source non datée est admise avec sa date de lecture (« non datée, lue le <date> »).

**[IMPÉRATIF P3.10]** **Le poids.** **A** : s'il varie de 20 %, la décision change ; vérifié en premier, recoupé par deux sources, test de vraisemblance contre un repère indépendant. **B** : change un titre ou un graphique. **C** : un détail.

**[IMPÉRATIF P3.11]** **Ligne A : recherche contraire.** Cherche la donnée qui contredirait le chiffre ou le titre (colonne « Ce qui la rendrait fausse » du ghost deck, objections de l'expert) ; CONTRE note la source trouvée et sa valeur, ou « rien sur N pages lues ». Une donnée contraire trouvée apparaît dans le livrable, avec son traitement.

**[IMPÉRATIF P3.12]** **Extrait recopié, pas résumé** : la consigne passée à WebFetch demande la phrase exacte qui contient le chiffre, mot pour mot. `portes.py` télécharge chaque source A (urllib, ou PyMuPDF pour un PDF) et cherche le nombre, après avoir normalisé les espaces, les virgules et les points : trouvé, CONFIRMÉ tient ; page inaccessible, EXTRAIT SEUL ; absent, la ligne repart au vérificateur.

**[IMPÉRATIF P3.13]** **Texte juridique** : Légifrance, Judilibre ou EUR-Lex, version en vigueur à la date des faits ; un arrêt porte sa juridiction, sa chambre, sa date et son numéro. Une référence non retrouvée sort du livrable : jamais d'HYPOTHÈSE pour une règle de droit.

**[RÈGLE P3.14]** **Page lue** : page ouverte avec succès. Les échecs (403, 404, page illisible) ne comptent pas, dans la limite de 2 fois le plafond en tentatives ; les recherches non plus. Les données lues par script, API ou CSV (Banque mondiale, OCDE, Eurostat…) ne comptent pas non plus : pour un tableau de chiffres, passe par là, car WebFetch n'en rend qu'un résumé.

**[RÈGLE P3.15]** **Plafond de pages lues : un plafond par outil exigé, jamais 10 fixes** (l'essai n°7 a vidé l'analyse de marché avec 10 pages : PESTEL à 2 facteurs, Porter sans donnée, culture non sourcée ; note 14,25 sur 20 au lieu de 17). Le chef le calcule avant la phase 1 et l'écrit dans `PAGES WEB LUES : n / plafond` de `ETAT.md`. **Express : 6 pages pour les lignes A, plus 2 pages par outil exigé par la référence** (`00_materiel.md` : PESTEL, Porter, culture, etc.), ou autant de pages que d'options comparées s'il y en a plus de 2 : `6 + outils × max(2, options)`, de 10 au moins à 30 au plus. **Approfondi : 40, ou ce calcul s'il est plus grand, 60 au plus.** **La réserve des outils** (`outils × max(2, options)` pages) ne se dépense jamais sur les lignes A : chaque outil exigé a au moins une source datée par option (P3.9). Un outil dont les faits sont dans le cas (CAS, P3.3) ne reçoit pas de page. Chaque ligne tirée d'un outil commence par `[OUTIL : nom]` dans la colonne Affirmation, et la porte de la phase 3 refuse un outil ou une option sans source. Le compte (pages web seulement) est dans la ligne `PAGES WEB LUES` de `ETAT.md`. **Les pages de tarifs d'une proposition (budget de la phase 2) comptent à part : 4 au plus.**

**[IMPÉRATIF P3.15b]** **Appels d'outil du vérificateur, en Express.** L'ordre de mission fixe un plafond d'appels d'outil par mission, affiché comme celui du fabricant (P6.27) : **10 appels plus 2 par page que la mission peut lire** (6 pages en phase 1 : 22 ; les 22 pages restantes d'un plafond de 28 en phase 3 : 54). À ce nombre il s'arrête et écrit `FIN: PARTIEL` ; les lignes non examinées deviennent NON VÉRIFIÉ (P3.16). Le chef ne relance qu'une fois, pour les seules lignes A restantes, avec 10 appels de plus. Les lectures par script comptent comme tout appel. Mesure de l'essai n°7, sans plafond : 2 missions, 106 appels, 14,8 millions de tokens traités, le premier poste du rendu.

## Les verdicts

**[IMPÉRATIF P3.16]** **EXTERNE** : CONFIRMÉ (page ouverte, extrait présent) ; SOURCE UNIQUE (chiffre A non recoupé : utilisable, signalé par « source unique » sous le chiffre ou dans l'annexe Sources) ; CORRIGÉ ; CONTRADICTOIRE (fourchette affichée, valeur retenue) ; EXTRAIT SEUL (page illisible ou qui bloque les robots, verdict valide) ; NON TROUVÉ (un chiffre A devient une HYPOTHÈSE, les autres sortent) ; NON VÉRIFIÉ (plafond atteint, étiquette « estimation », jamais FAIT).

**[RÈGLE P3.17]** **CAS** : CONFORME AU CAS ; une source web plus récente qui le contredit ne le remplace pas : note « [source] donne [valeur] en [année] ».

**[RÈGLE P3.18]** **PRIMAIRE** : CONFORME À LA COLLECTE. **CALCUL** : RECALCULÉ. **HYPOTHÈSE** et **TÉMOIGNAGE** : pas de verdict.

## Les règles

**[RÈGLE P3.19]** Source primaire (un blog est une « estimation sectorielle ») ; la référence donne la méthode, jamais un fait de marché ; chiffre de plus de 3 ans : année affichée ; ni années ni périmètres mélangés.

**[RÈGLE P3.20]** Statistiques justes (marge d'erreur, effectif, écart significatif), calculées par l'agent Agency `Statistician` s'il est installé, avec `model: sonnet`.

**[IMPÉRATIF P3.21]** **Un seul chiffre partout** : un chiffre corrigé l'est dans toutes ses occurrences, un `grep` le prouve.

**[IMPÉRATIF P3.22]** Une vraie entreprise citée comme partenaire est une candidate, jamais « a accepté ».

**[RÈGLE P3.23]** **Deux références savantes** (palier 17) : deux références académiques ou professionnelles reliées à un argument (Google Scholar, Cairn, HAL, revue professionnelle), vérifiées comme une ligne EXTERNE, avec auteur, année, titre.

**[RÈGLE P3.24]** **Les fichiers** : l'agent écrit `travail/calculs.py` et `travail/donnees.csv` sans rien exécuter ; c'est le chef qui lance les scripts (`calculs.py`, `portes.py`, `geler`, `verifier`) : ni le rédacteur ni le vérificateur n'en lance un, ni ne retouche un fichier de la porte (`objections.md`) pour la passer.

**[RÈGLE P3.25]** `calculs.py` a deux commandes, `geler` et `verifier` ; `geler`, lancé par le chef à la porte de la phase 4 (P4.11) et jamais avant, relève, **dans `02_contenu.yaml` seulement** (jamais dans `donnees.csv`, dont les valeurs ne sont pas du texte et donneraient de faux écarts à la porte de la phase 4), les nombres qui portent une unité, un symbole (%, €, $) ou une année (pas gelés : les entiers de 1 à 10 sans unité, les numéros de page, les jours de date). `donnees.csv` : une ligne par valeur affichée dans un graphique (série, valeur, unité, année, identifiant de la ligne de vérification). Avant le gel, `verifier` compare chaque nombre de ce type du YAML à `03_verification.md`, à `donnees.csv` et aux sorties de `calculs.py` ; après le gel, il compare aussi à `chiffres_geles.txt`.

**[RÈGLE P3.26]** **Chef : la porte de la phase 3.** Aucune ligne A sans verdict ; aucune ligne affichée sans « Citation (langue du livrable) » ; relis l'extrait de 3 lignes A tirées par `portes.py` ; compte, par outil et par option, les lignes `[OUTIL : nom]` (P3.15). **Ne gèle rien** : les verdicts CORRIGÉ et CONTRADICTOIRE changent des chiffres du YAML en phase 4, le gel vient après (P4.11). Ensuite, **arrêt C**.
