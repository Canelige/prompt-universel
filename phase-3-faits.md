Qui le lit, et quand : `diapo-verificateur`, avec `principes.md`, en phase 1 (chiffres décisifs du ghost deck) et en phase 3 ; la discussion de projet, à l'entrée de la phase 3 (porte) et pour « Chef : la porte de la phase 3 ».

# Phase 3 · Faits et chiffres (`diapo-verificateur`)

**[RÈGLE P3.1]** L'agent continue `travail/03_verification.md`, ligne par ligne, sans refaire les lignes déjà verrouillées.

| # | Affirmation | Type | Poids | Verdict | Source (organisme, date, URL lue ; ou document et page ; ou fichier de collecte ; ou script) | Extrait (15 mots max, pour EXTERNE et CAS) | CONTRE (lignes A) |
|---|---|---|---|---|---|---|---|

## Les types de preuve

**[RÈGLE P3.2]** **EXTERNE** : un marché, une vraie entreprise, une loi ; source primaire datée.

**[IMPÉRATIF P3.3]** **CAS** : donnée fournie par le professeur (cas, annexe, appel d'offres). Elle fait foi : document et page cités, cohérence contrôlée seulement. Elle ne sort jamais du livrable faute de source web.

**[RÈGLE P3.4]** **PRIMAIRE** : donnée produite par le groupe, avec effectif, date, recrutement et limite ; réponses brutes dans `travail/collecte/`.

**[IMPÉRATIF P3.5]** **TÉMOIGNAGE** : exemple vécu ou observé, écrit « nous avons observé… ». Il illustre, mais ne prouve jamais un chiffre ni une tendance.

**[RÈGLE P3.6]** **CALCUL** : refait dans `travail/calculs.py`, sur les valeurs non arrondies.

**[RÈGLE P3.7]** **HYPOTHÈSE** : va au registre.

## Les sources

**[IMPÉRATIF P3.8]** **La source la plus récente d'abord.** Pour un fait ou un chiffre EXTERNE, cherche la source la plus récente, publiée il y a 2 ans au plus ; ne remonte plus loin que si rien de récent n'existe, ou pour une donnée qui ne vieillit pas (une loi en vigueur, une date de création, un score culturel de référence). L'année reste affichée à côté du chiffre et la colonne Source dit pourquoi : « aucune source depuis <année> ». Une donnée CAS garde la date du cas.

**[RÈGLE P3.9]** **L'équilibre des preuves.** Pour comparer des options (pays, scénarios, partenaires), chaque option reçoit au moins une preuve datée pour chaque critère décisif ; le plafond de pages se répartit entre elles. Une source non datée est admise avec sa date de lecture (« non datée, lue le <date> »).

**[IMPÉRATIF P3.10]** **Le poids.** **A** : s'il varie de 20 %, la décision change ; vérifié en premier, recoupé par deux sources, test de vraisemblance contre un repère indépendant. **B** : change un titre ou un graphique. **C** : un détail.

**[IMPÉRATIF P3.11]** **Ligne A : recherche contraire.** Cherche la donnée qui contredirait le chiffre ou le titre (colonne « Ce qui la rendrait fausse » du ghost deck, objections de l'expert) ; CONTRE note la source trouvée et sa valeur, ou « rien sur N pages lues ». Une donnée contraire trouvée apparaît dans le livrable, avec son traitement.

**[IMPÉRATIF P3.12]** **Extrait recopié, pas résumé** : la consigne passée à WebFetch demande la phrase exacte qui contient le chiffre, mot pour mot. `portes.py` télécharge chaque source A (urllib, ou PyMuPDF pour un PDF) et cherche le nombre, après avoir normalisé les espaces, les virgules et les points : trouvé, CONFIRMÉ tient ; page inaccessible, EXTRAIT SEUL ; absent, la ligne repart au vérificateur.

**[IMPÉRATIF P3.13]** **Texte juridique** : Légifrance, Judilibre ou EUR-Lex, version en vigueur à la date des faits ; un arrêt porte sa juridiction, sa chambre, sa date et son numéro. Une référence non retrouvée sort du livrable : jamais d'HYPOTHÈSE pour une règle de droit.

**[RÈGLE P3.14]** **Page lue** : page ouverte avec succès. Les échecs (403, 404, page illisible) ne comptent pas, dans la limite de 2 fois le plafond en tentatives ; les recherches non plus. Les données lues par script, API ou CSV (Banque mondiale, OCDE, Eurostat…) ne comptent pas non plus : pour un tableau de chiffres, passe par là, car WebFetch n'en rend qu'un résumé.

**[RÈGLE P3.15]** **Plafond de pages lues** : 6 en Express, 20 en Standard, 40 en Approfondi, en priorité pour les lignes A ; le compte (pages web seulement) est dans la ligne `PAGES WEB LUES` de `ETAT.md`. **Les pages de tarifs d'une proposition (budget de la phase 2) comptent à part : 4 au plus.**

## Les verdicts

**[IMPÉRATIF P3.16]** **EXTERNE** : CONFIRMÉ (page ouverte, extrait présent) ; SOURCE UNIQUE (chiffre A non recoupé : utilisable, signalé par « source unique » sous le chiffre ou dans l'annexe Sources) ; CORRIGÉ ; CONTRADICTOIRE (fourchette affichée, valeur retenue) ; EXTRAIT SEUL (page illisible ou qui bloque les robots, verdict valide) ; NON TROUVÉ (un chiffre A devient une HYPOTHÈSE, les autres sortent) ; NON VÉRIFIÉ (plafond atteint, étiquette « estimation », jamais FAIT).

**[RÈGLE P3.17]** **CAS** : CONFORME AU CAS ; une source web plus récente qui le contredit ne le remplace pas : note « [source] donne [valeur] en [année] ».

**[RÈGLE P3.18]** **PRIMAIRE** : CONFORME À LA COLLECTE. **CALCUL** : RECALCULÉ. **HYPOTHÈSE** et **TÉMOIGNAGE** : pas de verdict.

## Les règles

**[RÈGLE P3.19]** Source primaire (un blog est une « estimation sectorielle ») ; le cours donne la méthode, jamais un fait de marché ; chiffre de plus de 3 ans : année affichée ; ni années ni périmètres mélangés.

**[RÈGLE P3.20]** Statistiques justes (marge d'erreur, effectif, écart significatif), calculées par l'agent Agency `Statistician` s'il est installé, avec `model: sonnet`.

**[IMPÉRATIF P3.21]** **Un seul chiffre partout** : un chiffre corrigé l'est dans toutes ses occurrences, un `grep` le prouve.

**[IMPÉRATIF P3.22]** Une vraie entreprise citée comme partenaire est une candidate, jamais « a accepté ».

**[RÈGLE P3.23]** **Deux références savantes** (palier 17) : deux références académiques ou professionnelles reliées à un argument (Google Scholar, Cairn, HAL, revue professionnelle), vérifiées comme une ligne EXTERNE, avec auteur, année, titre.

**[RÈGLE P3.24]** **Les fichiers** : l'agent écrit `travail/calculs.py` et `travail/donnees.csv` sans rien exécuter ; c'est le chef qui lance les scripts.

**[RÈGLE P3.25]** `calculs.py` a deux commandes, `geler` et `verifier` ; `geler` relève, dans `02_contenu.yaml` et `donnees.csv`, les nombres qui portent une unité, un symbole (%, €, $) ou une année (pas gelés : les entiers de 1 à 10 sans unité, les numéros de page, les jours de date). `donnees.csv` : une ligne par valeur affichée dans un graphique (série, valeur, unité, année, identifiant de la ligne de vérification).

**[RÈGLE P3.26]** **Chef : la porte de la phase 3.** Aucune ligne A sans verdict ; relis l'extrait de 3 lignes A tirées par `portes.py` ; lance `python travail/calculs.py geler`, qui écrit `travail/chiffres_geles.txt`. Ensuite, **arrêt C**.
