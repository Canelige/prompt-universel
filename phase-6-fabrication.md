Qui le lit, et quand : `diapo-fabricant`, en phase 6, avec `direction-artistique.md` (« Partie du fabricant ») ; la discussion de projet n'y cherche que la recette d'un format au besoin.

# Phase 6 · Fabrication (`diapo-fabricant`)

**[RÈGLE P6.1]** **Le système avant les pages.** `tokens.css` : les 9 couleurs (en Vivant, plus les teintes du tableau des rôles) ; l'échelle des tailles ; les espacements 8, 16, 24, 32, 48, 64, 96, 128 ; 3 épaisseurs de trait ; un seul rayon d'angle.

**[RÈGLE P6.2]** `travail/build.py` (la copie du gabarit du type, P6.24) produit chaque page et le livrable à partir de `02_contenu.yaml`. Une correction change une entrée YAML ou une règle CSS, puis `python travail/build.py --pages 7,12`. Toute valeur écrite en dur dans une page est une erreur. **Recette de `--pages`**, même pour un A4 en un seul HTML : `page.pdf(..., page_ranges="7,12")` n'imprime que ces pages, écrites dans `travail/rendus/pages-7-12.pdf`, puis converties en PNG ; ce rendu partiel ne compte pas dans `RENDUS COMPLETS` ; une liste qui couvre toutes les feuilles est refusée par `build.py` : c'est un rendu complet. **Recette de remplacement**, si un PDF livré existe dans `livraison/` : PyMuPDF remplace chaque page dans ce PDF, puis `livrable.txt` est régénéré page par page depuis le PDF obtenu.

```python
doc, part = pymupdf.open(livre), pymupdf.open(partiel)  # pages = [7, 12], dans l'ordre du rendu partiel
toc, meta = doc.get_toc(), doc.metadata
for i, n in enumerate(pages):
    doc.delete_page(n - 1)
    doc.insert_pdf(part, from_page=i, to_page=i, start_at=n - 1)
doc.set_toc(toc); doc.set_metadata(meta)
doc.save(livre + ".tmp", garbage=4, deflate=True); doc.close(); os.replace(livre + ".tmp", livre)
```

Le PDF assemblé ne compte pas dans `RENDUS COMPLETS` et ne va jamais dans `travail/rendus/`, où la porte compte les rendus complets. Une correction qui change le nombre de pages ne se remplace pas : elle demande un rendu complet. Sans `--pages`, `build.py` applique le compteur de `pilotage.md` (PI.31) et range le PDF complet, horodaté, dans `travail/rendus/`.

## La chaîne selon le format

**[RÈGLE P6.3]**

| Format | Chaîne |
|---|---|
| PDF (diaporama) | HTML et CSS → Playwright → PDF |
| Document A4 | HTML paginé (`@page`, en-tête, pied, numéros) → PDF |
| PPTX fidèle | une image 3840 × 2160 par page : PNG pour le texte, les graphiques et les aplats, JPEG qualité 85 pour une photo plein cadre ; notes conservées, texte alternatif = titre ; texte ni modifiable ni sélectionnable |
| PPTX modifiable, Google Slides, Keynote | skill `pptx`, vraies zones de texte ; polices de la charte si elles viennent de Google Fonts (Google Slides les propose toutes ; sur PowerPoint, la personne les installe depuis `travail/polices/`, et le rapport le dit), sinon repli ci-dessous ; couleurs, gabarits et rythme de la charte ; le PDF rendu avec les vraies polices est livré à côté |
| HTML | skill `frontend-slides`, fichier unique, polices en base64, aucune ressource distante |
| Word | skill `docx`, vrais styles, table des matières |

**[RÈGLE P6.4]** **Hors PDF**, le PDF rendu depuis le HTML est la référence : les autres formats en reprennent couleurs, tailles et rythme.

**[RÈGLE P6.5]** **Polices** : avant tout `soffice`, copie `travail/polices/` dans le dossier de polices de l'utilisateur (Mac : `~/Library/Fonts/` ; Windows : installation de la police), sans quoi le contrôle des débordements ne vaut rien.

**[RÈGLE P6.6]** Si la personne ne peut pas installer les polices d'un PPTX modifiable : repli Cambria pour les titres, Calibri pour le texte (jamais Georgia), 10 % de marge dans chaque zone de texte.

**[RÈGLE P6.7]** **Graphiques** : le SVG de `build.py` converti en PNG à 3 fois sa taille d'affichage (Playwright, `device_scale_factor=3`), inséré avec la conclusion du graphique en texte alternatif.

**[RÈGLE P6.8]** **PPTX modifiable** : les 10 gabarits sont de vraies dispositions du masque ; fond, pied (axe 7) et titre y sont réglés une fois ; la page de rupture est une disposition à part, avec son fond (clair ou en aplat, selon la charte).

**[RÈGLE P6.9]** **Word** : styles nommés (Titre 1, Titre 2, Corps, Légende, Source) réglés sur `tokens.css` ; couverture en section à part ; page de rupture = section claire, sans rectangle plein page, sauf en Vivant et en Affiche (`direction-artistique.md`, « La couleur », point 9 h) ; tableaux à filets fins ; pied selon l'axe 7 ; table des matières mise à jour avant la conversion.

**[RÈGLE P6.10]** **HTML** : `frontend-slides` reçoit `tokens.css` et `gabarits.css` ; ni découverte de style, ni aperçus, ni préréglages, aucun dégradé ni halo.

## Recette de rendu (Playwright et Chromium)

**[RÈGLE P6.11]** **Polices** : `@font-face`, chemins relatifs. Avant l'export, attends `document.fonts.ready` puis lis `[...document.fonts].map(f => f.family + ':' + f.status)` : un statut `error` arrête tout. Ne te fie pas à `document.fonts.check()`, vrai pour une police inexistante.

**[RÈGLE P6.12]** **Export** : `page.pdf(prefer_css_page_size=True, print_background=True, outline=True, tagged=True)` et `* { print-color-adjust: exact; -webkit-print-color-adjust: exact }`, sans quoi les aplats disparaissent.

**[RÈGLE P6.13]** **Diaporama** : `@page { size: 1920px 1080px; margin: 0 }`, une page HTML par page PDF (`break-after: page`) ; mesure `scrollHeight` et `scrollWidth` avant de masquer quoi que ce soit.

**[RÈGLE P6.14]** **A4** : couleur de fond aussi sur `@page` et `html` (sinon marges blanches) ; `break-inside: avoid` sur tableaux et figures ; `orphans: 3; widows: 3` sur les paragraphes.

**[RÈGLE P6.15]** **Métadonnées** : titre et auteurs par `doc.set_metadata(...)` de PyMuPDF ; langue de `<html lang>` avec `tagged=True`.

**[RÈGLE P6.16]** **Chromium** : Chromium absent, relance `python -m playwright install chromium` avec le lanceur du `.venv`. Repli si `playwright install` est refusé ou si la version attendue manque : un Chromium du cache, lancé par `p.chromium.launch(executable_path="<chemin>")`, chemin donné par `find ~/Library/Caches/ms-playwright ~/.cache/ms-playwright -type f \( -name "Chromium*" -o -name "chrome" -o -name "chrome-headless-shell" \) 2>/dev/null`. `chrome-headless-shell` suffit pour `page.pdf` ; passe toujours son chemin à `executable_path`. Windows : cache `%USERPROFILE%\AppData\Local\ms-playwright`.

**[RÈGLE P6.17]** **Poids** mesuré avant de déclarer le livrable prêt ; s'il est lourd, `doc.save(..., garbage=4, deflate=True)`.

**[RÈGLE P6.18]** **Noms de fichier** : `Sujet_Livrable_Auteur.pdf` (l'auteur : la personne, son équipe ou son entreprise), sans espaces ni accents, suivi de `_version-a-completer` si le livrable a encore des trous (phase 9).

**[RÈGLE P6.19]** **Livraison** : le livrable final (PDF, plus PPTX ou Word) va dans `<sous-dossier>/livraison/`, que `build.py` crée par chemin absolu ; `travail/` garde le reste. `build.py` écrit aussi `travail/livrable.txt`, le texte du PDF final page par page, et `travail/rendus/planche.png`, la planche de miniatures (P6.28).

**[RÈGLE P6.20]** En phase 6, `travail/controles.py` est la copie du gabarit (P6.24) : il porte déjà P6.21, P6.22, P6.23, les débordements, les éléments hors marges, les polices et les tirets, l'origine de l'accent, la surface colorée par feuille et d'ensemble, les aplats vifs et les aplats hors du tableau des rôles (DA.5b, DA.54, P7.10, P7.11) et le compteur de rendus (PI.31), et il écrit `07_controles.md` (P7.3). `diapo-fabricant` y ajoute les contrôles de charte dans `travail/controles_charte.py` (fonction `verifier(S, pdf, rep)` qui rend la liste des défauts), pour ce que le gabarit ne mesure pas (tailles hors échelle, familles, blocs encadrés, rythme), d'après « La couleur », « La typographie », « Le rythme et les gabarits », « Les images » (`direction-artistique.md`) et la liste de `phase-7-controles.md`.

## Les images

**[IMPÉRATIF P6.21]** **Au moins 3 vraies images pertinentes dans tout livrable**, sauf consigne contraire du destinataire ou de la personne : libres de droits et sourcées (Unsplash, Pexels, Wikimedia Commons, ou site officiel de la marque, cité), téléchargées par script dans `travail/images/` et créditées dans `travail/credits.md` et sous l'image (`direction-artistique.md`, « Les images »). **Une page à grand blanc** (une bande vide de plus de 35 % de la hauteur, mesurée par script sur l'image de la page) reçoit une image ou un visuel (schéma, carte, chiffre en grand), jamais du texte étiré. `controles.py` compte les images et mesure les blancs : moins de 3 images, ou une page à grand blanc, fait échouer la porte de la phase 6.

## Les nombres et les feuilles

**[IMPÉRATIF P6.22]** **Aucun nombre imprimé n'est écrit dans `build.py` ni dans un gabarit.** Tout nombre qui s'imprime (montants, totaux, pourcentages, années, durées, chiffres des tuiles et des frises) vient de `02_contenu.yaml` ou d'une valeur calculée par `calculs.py`, jamais d'un littéral du code : corriger le YAML doit suffire à tout changer. Seuls les numéros de page et les nombres de mise en page (tailles, espacements) s'écrivent dans le code. `controles.py` le vérifie, par script (il lit aussi les littéraux de `build.py` et de `blocs.py`) : il extrait du PDF rendu, comme `livrable.txt`, les nombres de la forme que gèle `calculs.py` (P3.25 : unité, symbole ou année), et tout nombre absent de `02_contenu.yaml` et des sorties de `calculs.py` fait échouer la porte de la phase 6.

**[RÈGLE P6.23]** **Plafond de feuilles.** `controles.py`, que `build.py` lance après chaque rendu complet, compte les pages du PDF rendu et les compare au maximum de `PAGES PROMISES` dans `ETAT.md` (DE.27) : au-delà, la porte de la phase 6 échoue. Le fabricant condense (pages fusionnées ou texte coupé, par le rédacteur) au lieu de livrer des feuilles en plus ; seul un accord de la personne, écrit dans DÉCISIONS DE LA PERSONNE, relève le plafond. Le message d'échec nomme les feuilles de suite à supprimer et les feuilles les plus chargées ; la porte ne livre rien dans `livraison/` tant qu'elle échoue.

## Les gabarits de fabrication

**[IMPÉRATIF P6.24]** **Le fabricant part du gabarit de son type et ne recompose jamais le sien** (l'essai n°6 a dépensé 27 millions de tokens à recomposer un gabarit à la main). Les gabarits sont dans `universel/outils/gabarits/` : `document_a4.py` (document A4, PDF), `diaporama.py` (diaporama 16:9, PDF et PPTX fidèle), `synthese_a4.py` (une page de synthèse A4, avec `document_a4.py`), plus `commun.py`, `controles.py` et `reglages.yaml` (modèle annoté). Il copie dans `travail/` : `commun.py`, `controles.py`, `reglages.yaml` et le gabarit du type **sous le nom `build.py`** (pour la synthèse, aussi `document_a4.py`). Il n'écrit que `reglages.yaml` (couleurs et `couleurs.origine`, énergie, polices, densité, `frise`, plan des feuilles : la direction artistique de la phase 5), les champs de mise en forme du YAML (`gabarit`, `etape`, `tuiles`, `images`, `points`) et, au besoin, `blocs.py` (P6.26). Il ne modifie ni `build.py`, ni `commun.py`, ni `controles.py` : un défaut d'un gabarit se signale au chef dans son statut. Les formats sans gabarit (Word, PPTX modifiable, HTML) suivent P6.3.

**[RÈGLE P6.25]** Ce que fait chaque gabarit, sans qu'on le réécrive : il lit tout le texte dans `02_contenu.yaml` et les nombres dans le YAML, `donnees.csv` ou `calculs.py` (P6.22) ; il prend couleurs, polices et densité dans `reglages.yaml` (les 9 rôles, `accent-fonce` compris, sont calculés par script, DA.44) ; il mesure chaque feuille (débordement, éléments hors marges, polices) et dit combien de lignes couper ; il tient le compteur de rendus (PI.31 : réserve du troisième rendu, `--pages` sur toutes les feuilles refusé, rendu qui plante non compté, PDF numérotés) ; il mesure l'accent et la surface colorée (P6.20) ; il lance `controles.py` et ne livre qu'une fois la porte passée (P6.23) ; il gère `--pages` et la recette de remplacement (P6.2, PDF et PPTX) ; il écrit `livrable.txt` et la planche (P6.19). Le gabarit `diaporama.py` écrit le PPTX fidèle de P6.3 (image 3840 × 2160 par diapositive, notes du YAML, texte alternatif = titre) et exige `points` ou un corps court (`mots_max`). Pièces prévues : totaux de tableau à plusieurs valeurs (`totaux: [[libellé, v1, v2]]`), `points: plus` (la liste suit le corps), seconde famille de polices pour les titres (`polices.titres`), frise des parties en pied (`frise`, `partie`, axe 7).

**[RÈGLE P6.26]** `travail/blocs.py` (facultatif) porte ce qui est propre au travail : `PIECES = {champ: fonction(piece, Y, D, S)}` rend une pièce du YAML qui porte ce champ, `CSS` ajoute des règles. Aucun nombre imprimé n'y est écrit (P6.22).

**[IMPÉRATIF P6.27]** **Missions et appels du fabricant.** Une seule mission de fabrication (charte dans `reglages.yaml`, premier rendu complet, contrôles), puis, en phase 8, une seule mission de corrections ciblées, rendues page par page avec `--pages` ; jamais de troisième. **La mission de fabrication prend 2 rendus complets au plus : le troisième est réservé à la phase 8** (`build.py` le refuse sans `--audit`, PI.31 ; l'essai n°7 avait pris les 3 dans la première mission et n'avait plus que `--pages` pour l'audit). En Express, **25 appels d'outil au plus par mission**, écrits dans l'ordre de mission (PI.35) ; à 25 il s'arrête, écrit `FIN: PARTIEL` et le chef reprend (PI.43). Mesure de l'essai n°6 : 2 missions, 119 appels, 27 millions de tokens traités.

**[RÈGLE P6.28]** **En Express, on lit les planches, pas les pages.** Le fabricant et le chef ne lisent que `rendus/planche.png` (ou `rendus/pages-<n>/` pour une correction) ; une page ne s'ouvre en grand que si `controles.py` l'a écrite sur sa ligne « A OUVRIR EN GRAND » (`pilotage.md`, PI.52). `python outils/gabarits/autotest.py` rejoue les trois gabarits et les cas d'échec de P6.22 et P6.23 : l'auteur du prompt le lance après toute modification du dossier.
