Qui le lit, et quand : `diapo-fabricant`, en phase 6, avec `direction-artistique.md` (« Partie du fabricant ») ; la discussion de projet n'y cherche que la recette d'un format au besoin.

# Phase 6 · Fabrication (`diapo-fabricant`)

**[RÈGLE P6.1]** **Le système avant les pages.** `tokens.css` : les 9 couleurs (en Vivant, plus les teintes du tableau des rôles) ; l'échelle des tailles ; les espacements 8, 16, 24, 32, 48, 64, 96, 128 ; 3 épaisseurs de trait ; un seul rayon d'angle.

**[RÈGLE P6.2]** `travail/build.py` produit chaque page et le livrable à partir de `02_contenu.yaml`. Une correction change une entrée YAML ou une règle CSS, puis `python travail/build.py --pages 7,12`. Toute valeur écrite en dur dans une page est une erreur.

## La chaîne selon le format

**[RÈGLE P6.3]**

| Format | Chaîne |
|---|---|
| PDF (diaporama) | HTML et CSS → Playwright → PDF |
| Document A4 | HTML paginé (`@page`, en-tête, pied, numéros) → PDF |
| PPTX fidèle | une image 3840 × 2160 par page : PNG pour le texte, les graphiques et les aplats, JPEG qualité 85 pour une photo plein cadre ; notes conservées, texte alternatif = titre ; texte ni modifiable ni sélectionnable |
| PPTX modifiable, Google Slides, Keynote | skill `pptx`, vraies zones de texte ; polices de la charte si elles viennent de Google Fonts (Google Slides les propose toutes ; sur PowerPoint, le groupe les installe depuis `travail/polices/`, et le rapport le dit), sinon repli ci-dessous ; couleurs, gabarits et rythme de la charte ; le PDF rendu avec les vraies polices est livré à côté |
| HTML | skill `frontend-slides`, fichier unique, polices en base64, aucune ressource distante |
| Word | skill `docx`, vrais styles, table des matières |

**[RÈGLE P6.4]** **Hors PDF**, le PDF rendu depuis le HTML est la référence : les autres formats en reprennent couleurs, tailles et rythme.

**[RÈGLE P6.5]** **Polices** : avant tout `soffice`, copie `travail/polices/` dans le dossier de polices de l'utilisateur (Mac : `~/Library/Fonts/` ; Windows : installation de la police), sans quoi le contrôle des débordements ne vaut rien.

**[RÈGLE P6.6]** Si le groupe ne peut pas installer les polices d'un PPTX modifiable : repli Cambria pour les titres, Calibri pour le texte (jamais Georgia), 10 % de marge dans chaque zone de texte.

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

**[RÈGLE P6.18]** **Noms de fichier** : `Sujet_Livrable_Groupe.pdf`, sans espaces ni accents, suivi de `_version-a-completer` si le livrable a encore des trous (phase 9).

**[RÈGLE P6.19]** **Livraison** : le livrable final (PDF, plus PPTX ou Word) va dans `<sous-dossier>/livraison/`, que `build.py` crée par chemin absolu ; `travail/` garde le reste. `build.py` écrit aussi `travail/livrable.txt`, le texte du PDF final page par page.

**[RÈGLE P6.20]** En phase 6, `diapo-fabricant` écrit aussi `travail/controles.py`, d'après « La couleur », « La typographie », « Le rythme et les gabarits » (`direction-artistique.md`) et la liste de `phase-7-controles.md`.
