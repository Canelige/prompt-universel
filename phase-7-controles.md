Qui le lit, et quand : `diapo-fabricant`, en phase 6, pour écrire `controles.py` ; la discussion de projet, en phase 7, pour lancer les contrôles et les tests ; `diapo-lecteur` reçoit seulement son lot de pages, jamais ce module.

# Phase 7 · Contrôles (scripts, puis le chef)

**[RÈGLE P7.1]** PNG de contrôle tirés du PDF final, avec PyMuPDF à 110 dpi. PPTX modifiable ou Word : ce PDF vient de `soffice --headless --convert-to pdf`.

**[IMPÉRATIF P7.2]** Sans LibreOffice, contrôle des débordements impossible, et le rapport le dit.

**[RÈGLE P7.3]** Le chef lance `travail/controles.py` et ne lit que `travail/07_controles.md` : un tableau page par contrôle, avec `ok` ou la valeur mesurée.

## 1. Contrôles de charte (seuils de `direction-artistique.md`)

**[RÈGLE P7.4]** Taille hors de l'échelle, famille hors de la charte ; contraste insuffisant.

**[RÈGLE P7.5]** Teinte hors du tableau des rôles, plus de teintes sur une page que l'énergie n'en permet (point 9 b, signature de marque exemptée), pastilles de statut hors du point 9 f.

**[RÈGLE P7.6]** Plus de blocs de texte encadrés que le point 9 g ne le permet (cartes, encadrés, pastilles de plus de 3 mots) : la page se lit comme un tableau de bord, regroupe en tableau à filets ou renvoie le détail aux notes.

**[RÈGLE P7.7]** Trait ou angle hors des tokens, bloc hors de la grille, espacement qui n'est pas un multiple de 8.

**[RÈGLE P7.8]** Rythme : même gabarit 3 fois de suite, plus de 6 pages sans rupture, moins de 2 ruptures (moins de 1 sous 8 pages).

**[RÈGLE P7.9]** Chiffre sans `tabular-nums`, espace insécable manquante (en français).

**[RÈGLE P7.10]** **Surface colorée** (mesure du point 9 e) hors de la plage de l'énergie choisie, sur l'ensemble du livrable.

**[RÈGLE P7.11]** **Plancher de couleur** : page sous 3 % de surface colorée (sauf Sobre typographique choisi), ou sous le nombre de moments de couleur de l'énergie (point 9 e), ou couverture Vivant ou Affiche sans aplat d'un quart de la page.

**[RÈGLE P7.12]** **Aplats, titres et couverture** : bandeau de titre de plus de 10 % de la hauteur de la page, titre-phrase de plus de 70 caractères ou de plus de 2 lignes, produit de couverture sous le contraste de 3:1 avec son fond, plus de 3 chiffres en couverture.

**[RÈGLE P7.13]** Marque réelle : logo absent de la couverture ou du bandeau. Moins de 3 vraies images, ou une page à grand blanc (`phase-6-fabrication.md`, P6.21).

**[RÈGLE P7.14]** PPTX ou Word : tailles, polices et couleurs lues avec `python-pptx` ou `python-docx`.

**[CONSEIL P7.15]** Si `impeccable` est installée, lance aussi son détecteur : `find ~/.claude .claude -path "*impeccable/scripts/impeccable" 2>/dev/null | head -1` donne son chemin, puis `<chemin> detect --json <fichiers.html>`.

## 2. Contrôles de texte

**[IMPÉRATIF P7.16]** BUDGET ; DÉBORDEMENT ; CHEVAUCHEMENT (`getBoundingClientRect` dans Playwright : deux boîtes de texte qui se recouvrent de plus de 2 px, ou texte qui sort du cadre de son graphique) ; COUPURE (étiquette de 3 mots ou moins sur deux lignes) ; VEUVE ; police non chargée, image manquante, numéro faux ; tiret long, « Lorem », « TODO », crochet `[à compléter]`.

## 3. Variantes pour l'audit

**[RÈGLE P7.17]** Diaporama, chaque page en 960 × 540 ; A4, chaque page en 794 × 1123 ; les mêmes en niveaux de gris ; planches de 6 pages et planche d'ensemble.

**[RÈGLE P7.18]** Corrige, puis relance, dans le plafond de rendus (`pilotage.md`, « Économie »).

## Tests de lecture

**[RÈGLE P7.19]** **Écran** (`diapo-lecteur`, Haiku, un lecteur par lot de 6 pages) : il recopie dans `travail/tests/ecran.txt` les titres, le texte, les étiquettes de graphique et, pour les sources, au moins l'organisme et l'année ; un script compare sa copie à `livrable.txt` et liste les mots absents. Rendu à 1280 × 720 (diaporama) ou 150 dpi (A4) ; sources, notes et numéros de page exclus. Ce qui manque monte d'un cran dans l'échelle, une seule fois. En Express, c'est le seul test.

**[RÈGLE P7.20]** **Rythme**, par script, sur les gabarits de `02_contenu.yaml` : au moins 4 gabarits différents, ruptures à la bonne cadence.

**[RÈGLE P7.21]** Les autres lectures se font en phase 8 : la réponse d'abord et les titres seuls (tests 1 et 2) par le destinataire ; le noir et blanc et la personnalité par le directeur artistique.

**[RÈGLE P7.22]** **Dépôt**, par script : poids sous la limite de la plateforme, fichier qui s'ouvre, polices incorporées (`pdffonts`). Ensuite, **arrêt C**.
