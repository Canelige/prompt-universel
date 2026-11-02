Qui le lit, et quand : `diapo-fabricant`, en entier, pour la planche des directions (fin de la phase 1) puis pour la charte (phase 5) et pour écrire `controles.py` ; la discussion de projet, seulement la « Partie du chef », du titre `# Partie du chef` au titre `# Partie du fabricant` exclu (`grep -n "^#" universel/direction-artistique.md`), plus `annexe-palettes.md` et `annexe-polices.md` pour les tirages, à la fin de la phase 1 ; l'auditeur « direction artistique » par `interdits.txt`, extrait par script de « Ce qui trahit l'IA ».

# Phase 5 · Direction artistique (`diapo-fabricant`, ordre de mission par le chef)

**[RÈGLE DA.1]** L'agent lit directement `reference/craft-floor.md` de la skill `impeccable` et la seule section « Commit the world » de `reference/new-work.md` (`grep -n '^## '`), sans lancer le flux complet de la skill ; `apple-design` n'est chargée que pour un HTML animé.

**[IMPÉRATIF DA.1b]** **Préséance : ce module l'emporte sur `craft-floor.md` d'`impeccable`.** Là où ils divergent (étiquette d'étape au-dessus du titre, chiffre géant de couverture, rangée de tuiles en Vivant), ce module tranche ; `craft-floor.md` ne sert que pour ce que ce module ne dit pas.

**[RÈGLE DA.2]** Il écrit `travail/05_charte.md`, `travail/tokens.css` et `travail/gabarits.css`, puis ajoute le champ `gabarit` à chaque page de `02_contenu.yaml`.

**[IMPÉRATIF DA.3]** Une **charte imposée** (école, entreprise, client) l'emporte, sur le goût de la personne comme sur les tirages : rythme, gabarits, graphiques et images se travaillent à l'intérieur.

# Partie du chef (et du fabricant)

## Le niveau visé : beau d'abord, différent ensuite

**[IMPÉRATIF DA.4]** Un rendu **beau, propre et pensé**, puis propre à la personne. La variété ne justifie jamais un rendu laid : tirage laid ou lourd, on le refait ; le veto de la planche vaut aussi en Express (sur l'unique direction, à la première planche de contrôle).

**[IMPÉRATIF DA.5]** **Couleur qui porte un sens**, expliquée, jamais tirée au hasard, et qui se voit : une page à peine teintée se lit comme une note de cabinet (plancher : « La couleur », point 9 e).

**[RÈGLE DA.6]** **Fond clair et respirant** en pages de contenu : au moins 30 % de blanc. Aplats pleins : « La couleur », point 9 h. Une page en couleur pleine porte peu de mots (un titre ou un chiffre en grand, une phrase, trois repères au plus), de préférence une vraie photo sur une moitié : une pleine page de couleur chargée de texte est le défaut le plus visible.

**[RÈGLE DA.7]** **De vraies images choisies**, des tableaux et graphiques nets, une hiérarchie évidente.

**[IMPÉRATIF DA.8]** **Peu de mots, pas peu de contenu** : toute la substance (chiffres, preuves, raisonnement, nuances) passe par la forme (`phase-2-contenu.md`, « La densité d'une page ») ; ce qui ne tient pas va en notes ou en annexe, jamais supprimé. Aéré mais creux : défaut GRAVE pour le destinataire.

## Le sujet donne le ton

**[IMPÉRATIF DA.9]** **Quand le sujet a une identité, elle donne le ton avant tout tirage.** Priorité 1, **marque ou entreprise réelle** (étudiée, cliente du cas, ou l'entreprise de la personne) : logo officiel et couleurs de marque, pris sur son site, son kit presse ou sa charte publique (Wikimedia Commons a souvent le logo), avec crédit. Sa palette devient le tableau des rôles (« La couleur », point 12). La marque du client va sur la couverture et dans le bandeau, en petit, jamais ailleurs ; logo jamais déformé, recoloré ni redessiné. L'axe 2 tiré décide du reste.

**[RÈGLE DA.10]** **La voix de la marque se reprend partout** : signature graphique (bandeau, motif, coins arrondis) sur chaque page, rayon d'angle de la marque = rayon unique de la charte. La typographie vient de l'axe 2 tiré, jamais de celle de la marque, pour qu'un livrable sur une marque ne se lise pas comme un document de la marque.

**[RÈGLE DA.11]** **Contrôle** (phase 8, directeur artistique et décideur) : le logo masqué, la page doit encore se reconnaître comme celle de la marque.

**[RÈGLE DA.12]** Priorité 2, **pays, ville, lieu** : couleur emblématique qui porte un sens, expliquée en une phrase ; pas le drapeau en entier ni le folklore, sauf demande.

**[RÈGLE DA.13]** Priorité 3, **secteur ou produit sans marque** : couleur tirée d'une matière, d'un produit ou de la photo de couverture.

**[RÈGLE DA.14]** Priorité 4, **rien de tout cela** : structure de palette de `annexe-palettes.md`, filtrée par le goût.

**[RÈGLE DA.15]** **Entreprise fictive** : logo créé pour le livrable, simple (logotype, monogramme ou pictogramme SVG dessiné par script), aux couleurs de la charte, sans ressemblance avec une marque réelle ; sa couleur devient l'accent (point 1) ; nom du cas, ou choisi par la personne.

**[RÈGLE DA.16]** Les couleurs de marque prennent le rôle de l'accent et de l'accent 2 parmi les 9 rôles ; en Vivant, toutes (5 au plus) entrent dans le tableau des rôles (point 9).

**[RÈGLE DA.17]** Contrastes obligatoires : une couleur de marque trop claire pour du texte sert aux aplats, sa version foncée au texte.

**[RÈGLE DA.18]** Le tirage ne décide que de ce que l'identité laisse libre : polices (axe 2), grille, couverture, graphiques.

## Anti-générique : chaque personne a un style à elle

**[RÈGLE DA.19]** **Les modules ne fixent aucune police, aucune couleur, aucune couverture** : tout vient du sujet, du goût de la personne et des tirages de `travail/tirer.py` dans les catalogues de `annexe-polices.md` et `annexe-palettes.md`. Commande : `python travail/tirer.py <étiquette> <k> "<option>" ...`, étiquette unique par tirage (`axes/2`, `d1/palette`, `d2/police-titre`…) ; le script rend k options distinctes et note tout dans `travail/tirages.log`.

**[RÈGLE DA.20]** **L'identité éditoriale avant la couleur.** En fin de phase 1, écris en tête de `05_charte.md` : thèse éditoriale en une phrase (« ce document se lit comme… »), objet ou métaphore visuelle tirés du sujet, grammaire des titres, grammaire des graphiques, langage des photos, 3 choix distinctifs et 3 choix à éviter. Deux personnes sur le même sujet doivent différer par cette identité (architecture, grille, titres, données, images), pas seulement par la palette.

**[RÈGLE DA.21]** **Le goût prime sur le tirage** : tire parmi les options compatibles avec le sujet et le goût, même s'il n'en reste qu'une ou deux. L'énergie de l'étape C fixe l'axe 1 et n'est jamais tirée. Goût « sobre » : pas de fond sombre. Sans goût : tout le catalogue de l'énergie.

**[RÈGLE DA.22]** **Express (pas de planche)** : pas de tirage de direction ; pars de l'énergie choisie, choisis par raisonnement la direction qui sert le mieux le sujet et le goût, écris pourquoi dans `05_charte.md` ; le tirage ne départage que les polices et la structure de palette.

**[IMPÉRATIF DA.23]** **Une série garde sa charte, et sa planche est comparée au meilleur rendu** : tokens, gabarits, polices et script de contrôle du livrable précédent repris, seules les teintes de partie changent ; écris « suite de <livrable précédent>, charte reprise ». La référence est l'épisode que la personne a le plus aimé (`profil.md`), pas le dernier : pose la planche du nouvel épisode à côté de la sienne ; plus dense, plus bigarré ou moins illustré, corrige avant de livrer.

**[RÈGLE DA.24]** **Pas deux fois le même style pour la même personne** entre matières, clients ou sujets différents (jamais entre volets d'une même série) : directions, palettes et polices de l'historique de `profil.md` retirées avant le tirage.

**[RÈGLE DA.25]** **Écarte la première idée qui vient** : note le choix « évident » écarté dans `05_charte.md`.

**[CONSEIL DA.26]** **Sortir du catalogue est permis** si c'est plus intéressant (une ligne de justification).

**[RÈGLE DA.27]** Polices-réflexes de `annexe-polices.md` : interdites, sauf justification écrite.

## Les 3 directions (fin de la phase 1, arrêt B)

**[RÈGLE DA.28]** Les 3 directions diffèrent **obligatoirement** sur les axes 2 et 3 et sur au moins un autre axe ; A4 destiné à l'impression : axes 2, 3 et 4. Un seul appel par axe donne une valeur distincte par direction (`tirer.py axes/2 3 <valeurs>`). L'axe 1 est l'énergie choisie à l'étape C, gardée par les 3 directions ; sur « je ne sais pas », le tirage ne décide que de l'ordre.

**[RÈGLE DA.29]**

| # | Axe | Valeurs possibles |
|---|---|---|
| 1 | Énergie (stratégie de couleur), choisie à l'étape C | **Sobre** : fond clair teinté ; surface colorée (mesure du point 9 e de « La couleur ») de 8 % ou plus du livrable (sauf Sobre typographique, si la personne le choisit). **Vivant** : fond clair, 3 à 5 couleurs vives en rôles fixes (point 9), bandeau ou signature, cartes à liseré, chevrons d'étapes, tuiles de chiffres en aplat, couverture en aplat ; surface colorée de 10 à 30 %. **Affiche** : une couleur saturée ; surface colorée de 30 à 60 % (colonne pleine hauteur, demi-page, fonds de rupture). **Sombre** (seulement si la personne demande un rendu sombre ou immersif) : fond sombre teinté, ou fond de couleur sur 60 % des pages au moins ; encre et accent contrastent avec ce fond. |
| 2 | Voix d'affichage (couverture, chiffres clés, mots de section) | serif de lecture ; serif d'affichage ; grotesque grasse ; condensée ; une seule famille en 2 graisses ; serif à empattements carrés |
| 3 | Couverture | typographique avec grand blanc ; aplat sur 60 % avec titre en négatif ; image ou carte plein cadre ; chiffre géant ; reproduction d'un document du cas |
| 4 | Grille | 12 colonnes ; colonne pleine hauteur qui porte le titre ; asymétrique un tiers, deux tiers ; modulaire |
| 5 | Graphiques | filets fins et une barre d'accent ; barres épaisses et très grands chiffres ; points et lignes lumineux sur fond sombre |
| 6 | Images (3 au moins, toujours : DA.94) | noir et blanc ; duotone encre et accent ; couleur naturelle, plein cadre ; vignettes cadrées dans la grille |
| 7 | Repère de navigation | numéro de page seul en pied ; frise des parties en pied, avec la partie courante en accent ; titre courant vertical dans la marge ; une teinte de l'accent par partie |
| 8 | Titre de page | sous un filet, en haut à gauche ; dans la colonne de gauche ; au-dessus du graphique, aligné sur lui ; en capitales dans la marge |
| 9 | Tableaux | filets horizontaux seuls ; ligne de tête en aplat d'accent ; bandes alternées claires ; total en gras et colonne de chiffres à droite |

**[RÈGLE DA.30]** **Compatibilités** : un tirage qui enfreint une ligne ci-dessous est refait avec l'étiquette suffixée `/bis`.

**[RÈGLE DA.31]** Axe 5 « lumineux sur fond sombre » : exige l'axe 1 Sombre et une structure dont le fond a une luminosité inférieure à 0,35 (`annexe-palettes.md` : 3, 4, 6, 15, 21, 26, 30, 39) ; « lumineux » = clair et saturé, jamais un halo.

**[RÈGLE DA.32]** Axe 6 « vignettes cadrées » exclut l'axe 3 « image plein cadre » ; axe 3 « document du cas » exige un document fourni par le cas.

**[RÈGLE DA.33]** A4 destiné à l'impression : Sobre, Vivant ou Affiche, sans « lumineux sur fond sombre » ; fond sombre (luminosité inférieure à 0,35) en pleine page interdit ; Sombre ne s'applique pas à un A4.

**[RÈGLE DA.34]** Vivant et Affiche : couverture avec aplat d'au moins un quart de la page ; axe 3 « typographique avec grand blanc » permis seulement avec cet aplat (bandeau large, colonne).

**[RÈGLE DA.35]** **Le nom de chaque direction** : un objet du sujet ou un référent réel, jamais « moderne » ni « élégant » ; plus 3 mots d'ambiance et l'objet d'où vient l'accent.

**[RÈGLE DA.36]** **Chef : la planche.**
1. Tirages des 3 directions : axes 2 à 9 (l'axe 1 vient de l'étape C), palette, polices de titre et de texte, décalage de teinte.
2. Un seul ordre à `diapo-fabricant` : il lit « La couleur », « La typographie », `annexe-polices.md`, `annexe-palettes.md` et `tirages.log`, produit pour chaque direction `travail/directions/d<n>/` (`tokens.css`, une couverture, une page de graphique commenté sur le vrai sujet), puis assemble `travail/directions/planche.png`, en 3 colonnes.
3. Tu ne lis que la planche.

**[IMPÉRATIF DA.37]** **Veto de la planche** : avant de la montrer, cherche 5 défauts par direction : titre de couverture sur plus de 3 lignes ; texte sur aplat illisible à 960 px de large ; palette ternie par la gamme ; deux familles de polices voisines (une grotesque avec une sans humaniste) ; élément dominant de couverture illisible en vignette. Direction fautive : refaite une fois, étiquette `/bis`.

**[RÈGLE DA.38]** Après l'arrêt B, `diapo-fabricant` construit la charte complète de la direction choisie.

## La couleur : d'où elle vient (points 1 et 2)

**[RÈGLE DA.39]** **1. Structure tirée de `annexe-palettes.md`, teinte remplacée.** Tirage `d<n>/palette` parmi les lignes de l'énergie choisie (Vivant : lignes de Sobre et d'Affiche à fond clair). Une ligne donne une structure (luminosités, chromas, relations entre teintes), pas des couleurs à garder.

**[RÈGLE DA.40]** **2. Teinte cible** : celle d'un objet du sujet (matière, produit, emballage, logo du client, document du cas), décalée de -30, -15, 0, +15 ou +30 degrés par tirage (`d<n>/decalage`). Une couleur emblématique est bienvenue si elle porte un sens expliqué en une phrase (pas le drapeau en entier ni du folklore, sauf demande) ; jamais la couleur par défaut du secteur sans raison. La charte écrit l'objet d'où vient la teinte.

## Ce qui trahit l'IA (interdit)

**[IMPÉRATIF DA.41]** Interdit, vérifié par le directeur artistique et en partie par `controles.py` :
- un fond crème, avec un titre en serif contrasté, un mot en italique et un accent terracotta ;
- un sur-titre décoratif qui répète le titre (une étiquette d'étape utile à la navigation, comme le nom de l'étape de la référence, reste permise) ;
- des « 01, 02, 03 » décoratifs ;
- une rangée de 3 cartes identiques, ou de 3 grands chiffres (en Vivant, les tuiles de chiffres clés en aplat sont permises, chacune dans la couleur de son rôle) ;
- une barre épaisse sur le bord gauche d'un encadré (en Vivant, la carte à liseré coloré fin est permise), des pastilles décoratives (pas la pastille de statut du point 9 f), des cartes arrondies partout (le rayon d'angle de la marque, repris tel quel, est permis) ;
- des icônes de remplissage, des émojis ;
- des dégradés, du flou, du verre dépoli, des filtres CSS, des ombres portées (sauf l'ombre douce d'un produit détouré, en couverture, incluse dans l'image par script) ;
- un paragraphe centré, une puce de 3 lignes ;
- les titres « Introduction », « Conclusion », « Merci » ;
- 4 polices sur un livrable, une teinte hors du tableau des rôles, plus de teintes sur une page que l'énergie n'en permet, plus de blocs encadrés que le point 9 g ne le permet, une page sous le plancher de couleur (point 9 e) ;
- un camembert, un graphique en 3D ;
- du « Lorem », des valeurs fictives oubliées.

# Partie du fabricant

## La couleur : la construction (points 3 à 12)

**[RÈGLE DA.42]** **3. Rotation** : on ajoute à la teinte des 4 colonnes l'écart entre la teinte cible et la teinte d'accent de la ligne.

**[RÈGLE DA.43]** **4. Gamme** : un script ramène chaque couleur dans la gamme sRGB en baissant le chroma ; autre ligne si l'accent perd plus de 0,04 de chroma, ou si le fond d'une Affiche ou d'une Sombre en perd plus de 0,05.

**[RÈGLE DA.44]** **5. Les 9 rôles**, calculés par script dans `tokens.css` :
- `fond`, `encre`, `accent`, `accent-2` : les 4 colonnes après rotation ; `accent-2` ne couvre jamais plus de 10 % d'une page ;
- `fond-rupture` : l'accent en Affiche et en Vivant ; en Sobre et en Sombre, échange du fond et de l'encre ; réservé aux aplats de rupture (point 9 h ; A4 : seulement Vivant et Affiche) ;
- `accent-fonce` : teinte de l'accent, luminosité déplacée par pas de 0,02 jusqu'à 4,5:1 sur le fond ; textes en couleur, filets, série principale ;
- `accent-clair` : luminosité à mi-chemin entre le fond et l'accent, chroma réduit de moitié ;
- `encre-secondaire` : l'encre rapprochée du fond d'un quart de l'écart de luminosité entre les deux ;
- `filet` : le fond, écarté de 0,10 en luminosité.

**[IMPÉRATIF DA.45]** **6. Contrastes**, mesurés par script : encre sur fond 7:1 ; encre secondaire 4,5:1 ; texte sur un aplat d'accent 4,5:1 ; `accent-fonce` sur fond 4,5:1 ; très grands titres 3:1.

**[RÈGLE DA.46]** Avant d'écarter une ligne sur « texte sur un aplat d'accent », le script déplace la luminosité de l'accent par pas de 0,02, sur 0,10 au plus, et garde la première valeur qui passe 4,5:1 avec le fond ou avec l'encre ; si un contraste échoue encore, on tire une autre ligne.

**[RÈGLE DA.47]** **7. Neutres** teintés vers l'accent : fond clair au chroma le plus élevé que permet la gamme sRGB, jusqu'à 0,04 (à luminosité 0,97, souvent 0,013 à 0,02) ; encre de chroma 0,02 à 0,04. Ni blanc pur, ni noir pur, ni gris pur.

**[RÈGLE DA.48]** **8. Fond crème** permis seulement avec un accent saturé qui porte un sens ; crème avec terracotta ou brique choisi par défaut : cliché de l'IA, interdit. Neutres alors chauds, plus pâles que la teinte de l'accent, chroma de fond sous 0,015.

**[RÈGLE DA.49]** **9. La couleur en deux étages** (elle remplace le plafond unique de teintes par page). a) **La signature de marque est exemptée du plafond** (bandeau multicolore, logo, couleurs officielles d'une marque réelle).

**[RÈGLE DA.50]** b) **Le contenu suit l'énergie choisie.** Sobre : 2 teintes non neutres au plus par page. Vivant : toutes les couleurs de la palette déclarée, 5 au plus (`accent`, `accent-2`, puis 1 à 3 teintes écartées d'au moins 40°, ou la palette officielle de la marque). Affiche : une couleur dominante et un accent.

**[IMPÉRATIF DA.51]** c) **La couleur par rôle : le tableau des rôles** (rôle / couleur), écrit une fois dans `05_charte.md` ; chaque couleur est un jeton de `tokens.css`, il ne remplace pas les 9 rôles du point 5. Toute teinte hors de ce tableau est interdite, chaque teinte garde le même sens sur toutes les pages : c'est la parade à l'arc-en-ciel. Sobre : 2 teintes, rôles répartis.

**[RÈGLE DA.52]** d) **La donnée porte la couleur** : toute variable à catégories (pays, critère, phase, nature de coût) reçoit sa couleur du tableau des rôles et la garde partout (en-têtes, barres, Gantt, tuiles, puces) ; Sobre et Affiche : teintes de l'accent ordonnées par luminosité.

**[IMPÉRATIF DA.53]** e) **Plancher, pas seulement plafond** : Vivant et Affiche, au moins 3 moments de couleur par page (signature, aplat ou carte à liseré, graphique ou chiffres en couleur) et couverture avec aplat d'au moins un quart de la page ; Sobre, au moins un moment de couleur franche par page, chiffres clés dans la couleur de leur rôle. Moins de 3 % de surface colorée sur une page : défaut, sauf Sobre typographique choisi et écrit dans `05_charte.md`.

**[RÈGLE DA.54]** **Mesure** du point 9 e, par script, sur le PNG de chaque page rendue (110 dpi, phase 7) : part des pixels de chroma OKLCH supérieur à 0,04, photos exclues (numérateur et dénominateur). Plancher de 3 % page par page ; plage de l'énergie (axe 1) sur l'ensemble des pages. En Vivant, moins de 10 % sur l'ensemble bloque la porte de la phase 7 (`phase-7-controles.md`, P7.10b) : prévois dès la charte le bandeau, les tuiles en aplat et les fonds de section.

**[RÈGLE DA.55]** f) **Pastilles de statut** (FAIT, HYPOTHÈSE, À VÉRIFIER) permises en Vivant, couleurs du tableau des rôles uniquement, une par bloc au plus ; les autres tags d'incertitude restent du texte. Jamais de vert, de jaune ou de rouge ajoutés hors palette.

**[RÈGLE DA.56]** g) **Blocs encadrés** : 6 au plus par page, 8 en Vivant.

**[RÈGLE DA.57]** h) **Aplats pleins.** En Sobre et en Vivant, l'aplat plein va à la couverture, à la page de décision et aux pages de rupture, 25 % des pages au plus (sauf rendu sombre ou immersif demandé expressément) ; en Affiche, s'y ajoutent les demi-pages ; en Vivant, la couleur prend aussi le bandeau, les cartes, les tuiles et des aplats clairs. Une rupture peut être claire (grand filet d'accent, grand titre ou grand chiffre) : l'aplat n'est jamais obligatoire.

**[RÈGLE DA.58]** Exception de format : un A4 Sobre, imprimé ou non, n'a de page en couleur pleine que la couverture ; rupture et décision restent claires, sans couleur au bord de la page.

**[RÈGLE DA.59]** Les bandeaux de titre suivent leur propre règle : bandeau plein derrière le titre d'une page de contenu, 10 % au plus de la hauteur ; sinon le titre se met en couleur sur le fond, avec un filet court.

**[RÈGLE DA.60]** **10. Couleurs de sens** (vert = favorable, rouge = défavorable, jaune = à surveiller) : réservées, jamais ajoutées à la palette ; elles ne servent que si le tableau des rôles les contient, avec ce sens et aucun autre. Si le tableau n'en contient pas une, ou si une teinte de la palette est à moins de 40° d'elle : signe et mot à la place. Le sens ne repose jamais sur la couleur seule ; elles servent aux données, en petites surfaces.

**[RÈGLE DA.61]** Niveaux et statuts (risque, priorité, étape) : intensité de l'accent ou mot, jamais une pastille verte, jaune ou rouge à côté de chaque ligne (sauf la pastille du point 9 f) : une page en pastilles multicolores est le défaut que la personne remarque d'abord.

**[RÈGLE DA.62]** **11. Grammaire de la couleur** : une famille de teinte par partie de l'argument, gardée du début à la fin du livrable et d'un livrable à l'autre dans une série ; la charte l'écrit en une ligne (« teinte A pour l'analyse, teinte B pour les choix, teinte C pour la décision »). Variable à catégories du point 9 d : jamais de teinte hors du tableau des rôles, limite de teintes par page maintenue.

**[IMPÉRATIF DA.63]** **12. Marque imposée** (palette de marque, ou charte de l'entreprise, du client ou de l'école fournie) : cette palette est le tableau des rôles ; pas de tirage dans `annexe-palettes.md`, pas de décalage de teinte (points 1 à 4), pas de couleur ajoutée.

**[RÈGLE DA.64]** Chaque rôle prend une couleur de la palette imposée ; s'il y a moins de couleurs que de rôles, des rôles partagent une couleur et se distinguent par un mot, un signe ou l'intensité. Les exigences contraires tombent : une teinte par partie (point 11, axe 7) n'existe que si la palette l'offre ; la limite de 10 % d'`accent-2` ne joue pas entre couleurs de marque.

## La typographie

**[RÈGLE DA.65]** **1 à 3 familles**, chacune avec son rôle ; la classe de la police d'affichage vient de l'axe 2, correspondance avec le catalogue dans `annexe-polices.md`.

**[RÈGLE DA.66]** **Téléchargement**, par script Python, sans clé d'accès ; fichiers dans `travail/polices/` (rien n'est chargé depuis un site au rendu).
- Google Fonts : `https://fonts.googleapis.com/css2?family=<Nom+avec+des+plus>:wght@400;600;700`, appelé sans en-tête de navigateur, renvoie un CSS avec des TTF complets, seulement pour les graisses qui existent ; télécharge chaque URL `fonts.gstatic.com` du CSS. Ces TTF servent au PDF et s'installent pour PowerPoint et LibreOffice.
- Fontshare [FS] : `https://api.fontshare.com/v2/css?f[]=<id>@400,700&display=swap` renvoie le CSS avec les adresses à télécharger.

**[RÈGLE DA.67]** **Vérification** par script, avec `fontTools` : la police couvre les caractères de la langue du livrable. Français : `àâçéèêëîïôœùûüÿÀÂÇÉÈÊËÎÏÔŒÙÛÜ«»€%’` et l'espace insécable (le `Ÿ` majuscule n'est pas testé : absent du sous-ensemble `latin`, aucun mot français courant ne l'emploie). Anglais : `“”‘’€%`.

**[RÈGLE DA.68]** **Tableaux chiffrés** : police avec la fonction `tnum` (table GSUB, lue avec fontTools) ou chiffres de même chasse ; sinon les colonnes de chiffres passent dans la mono de la charte.

**[RÈGLE DA.69]** **Graisses** : police de titres, seulement la graisse employée (Gloock, Young Serif, Rozha One, Gambarino et Tanker n'existent qu'en 400 : la charte les met en 400) ; police de texte, 400 et une graisse de 600 à 700 (Cardo et Libre Caslon Text n'ont que le 700 : il suffit). Fontshare ne renvoie pas de 404 pour une graisse absente : le script compte les `@font-face` du CSS reçu et les compare aux graisses demandées. Seul l'échec de la graisse 400 écarte une police (on en tire une autre de la même catégorie). `html { font-synthesis: none }` dans `tokens.css`, pour qu'aucun faux gras ne soit fabriqué.

**[RÈGLE DA.70]** **Trois rôles au plus** : police d'affichage, police de texte lisible, police d'étiquettes, de tags et de sources (chasse fixe ou capitales espacées). Un mot du titre de couverture peut passer en italique et en couleur.

**[RÈGLE DA.71]** **Police d'affichage expressive ou ronde, emploi borné** : titre de couverture, chiffres clés de grande taille, mots de section courts. Titres-phrases des pages dans la famille du texte, en gras : 70 caractères et 2 lignes au plus.

**[RÈGLE DA.72]** **Lisibilité des chiffres d'affichage** : rends « 1 I 0 O € 5 » en 48 px dans cette police et compare les glyphes de chaque paire (1 et I, 0 et O, € et 5), par différence d'image ou sur la planche ; s'ils se confondent, tous les chiffres passent dans la police du texte.

**[RÈGLE DA.73]** **Trois niveaux par page de contenu** : étiquette courte au-dessus (nom de l'étape ou de la partie) ; titre = conclusion de la page ; objet visuel, ligne « et alors ? », ligne de sources.

**[RÈGLE DA.74]** **Aucune police de repli du système** : le contrôle vérifie avec `pdffonts` que les polices incorporées sont celles de la charte.

**[RÈGLE DA.75]** **Échelle des tailles :**

| Élément | Diaporama 1920 × 1080 px | A4 |
|---|---|---|
| Titre | 64 à 80 px, 2 lignes au plus | 22 à 26 pt |
| Sous-titre | 40 px | 14 pt |
| Texte | 32 px | 10,5 à 11 pt |
| Cellules de tableau | 28 px | 9,5 pt |
| Étiquettes de graphique | 24 px | 9 pt |
| Sources et notes | 22 px | 8,5 pt |
| Numéro de page | 20 px | 8 pt |
| Couverture et séparateurs | 120 à 160 px | 40 à 56 pt |
| Chiffre unique | 200 px | 72 pt |
| Chiffre géant de couverture (axe 3) | 360 à 480 px | 140 à 200 pt |

**[RÈGLE DA.76]** Les contrôles de taille comparent des px lus dans le DOM, jamais des pt lus dans le PDF : dans le PDF de Chromium, 1 px vaut 0,75 pt.

**[RÈGLE DA.77]** **Interlignage** 1,15 à 1,25 pour les titres, 1,4 à 1,5 pour le texte ; lignes de 45 à 75 caractères.

**[RÈGLE DA.78]** **CSS** : `text-wrap: balance` sur les titres, `text-wrap: pretty` sur les paragraphes, `font-variant-numeric: tabular-nums` dans les tableaux, `white-space: nowrap` sur les nombres et les étiquettes de 3 mots ou moins, `<html lang>` dans la langue du livrable.

## Le rythme et les gabarits

**[RÈGLE DA.79]** **Les 10 gabarits** (un par page) : 1. **Couverture**, un seul élément dominant ; 2. **Synthèse** ; 3. **Séparateur de partie** ; 4. **Graphique commenté** (graphique sur 60 % de la largeur, lecture à côté) ; 5. **Tableau de la référence**, pleine largeur ; 6. **Comparaison** (2 ou 3 colonnes séparées par des filets, jamais des cartes, sauf les cartes à liseré du Vivant) ; 7. **Chiffre unique** ; 8. **Image ou carte** ; 9. **Cheminement** (frise, étapes, flux) ; 10. **Décision**, 2 pages au plus : page 1, la décision, les conditions, le coût et le gain, le critère d'arrêt ; page 2, les actions, les indicateurs, la première étape à 30 jours.

**[RÈGLE DA.80]** **Couverture** (gabarit 1) : image de produit jamais sur un fond de sa propre couleur dominante (un script mesure le contraste entre les deux, 3:1 au moins) ; image d'environ 55 % de la largeur, ombre douce si elle est détourée ; 3 chiffres au plus.

**[RÈGLE DA.81]** **Rythme** : jamais 3 pages de suite sur le même gabarit ; après 2 pages denses, une page aérée.

**[RÈGLE DA.82]** Une page de rupture (séparateur, chiffre unique, image, décision) au plus tard après 6 pages sans rupture, et 2 au moins par livrable (1 sous 8 pages) ; elle peut être claire, le fond de rupture en aplat n'est jamais obligatoire (point 9 h) et n'existe qu'en diaporama et en A4 Vivant ou Affiche.

**[RÈGLE DA.83]** Au-delà de 12 pages, un séparateur ouvre chaque partie.

**[RÈGLE DA.84]** Les dernières pages sont la décision, jamais « Merci » ni « Questions ? » ; les annexes suivent.

## Les graphiques

**[RÈGLE DA.85]**

| Question | Forme |
|---|---|
| Comparer des éléments | barres horizontales triées ; points alignés au-delà de 10 |
| Montrer une évolution | courbe, étiquette en bout de ligne |
| Montrer la part d'un tout | barre 100 %, ou le chiffre en grand |
| Comparer à un objectif | graphique à puces |
| Décomposer un total | cascade |
| Classer sur 2 critères | matrice 2 × 2, axes gradués |
| Montrer taille et composition | Marimekko, ou barres empilées |
| Situer un lieu | carte plate d'une seule région colorée |
| Phaser | frise ou Gantt, jalons datés, un responsable par ligne |
| Montrer un lien entre deux variables | nuage de points, points clés nommés |
| Chiffrer un projet | tableau de projection, filets fins, total en gras |

**[RÈGLE DA.86]** Titre = conclusion, point qui la prouve **annoté sur le graphique**.

**[RÈGLE DA.87]** Série du message en `accent-fonce`, les autres en encre secondaire ; 3 à 5 séries : teintes de l'accent ordonnées par luminosité ; Vivant : variable à catégories aux couleurs du tableau des rôles (point 9 d).

**[RÈGLE DA.88]** Étiquettes posées sur les données ; barres depuis zéro ; pas de double axe, pas de cadre ; graphique sur 55 % de la zone utile au moins.

**[IMPÉRATIF DA.89]** **Chaque graphique est un SVG généré par script à partir de `travail/donnees.csv`** : une valeur absente du fichier ne s'affiche pas ; pas de matplotlib, pas de canvas.

**[RÈGLE DA.90]** Unité, année et source dessous ; un graphique sans message est remplacé par un chiffre unique.

## Les images

**[RÈGLE DA.91]** **Au moins 2 pages sur 3** portent un graphique, un schéma, une carte ou une image.

**[RÈGLE DA.92]** **La photo d'abord, la teinte ensuite** : choisis d'abord, quand c'est possible, l'image de couverture (objet, matière ou lieu du sujet), puis prends l'accent dans cette photo : la couleur s'explique alors en une phrase.

**[CONSEIL DA.93]** Légère texture de grain sur les grands aplats, contre l'effet gabarit.

**[IMPÉRATIF DA.94]** **Au moins 3 vraies images pertinentes dans tout livrable**, sauf consigne contraire : libres de droits et sourcées (Unsplash, Pexels, Wikimedia Commons, ou site officiel de la marque, cité) ; preuve ou repère, jamais décor (lieux, produits, documents du cas, personnes au travail), dont une sur la couverture si la direction le permet ; au sujet, récentes si possible ; pour comparer des options, un diptyque de même hauteur et de même format. Zéro image : défaut GRAVE pour le directeur artistique ; un livrable fait surtout de tableaux : MOYEN. **Une page à grand blanc** reçoit une image ou un visuel (schéma, carte, chiffre en grand), jamais du texte étiré (`phase-6-fabrication.md`, P6.21).

**[RÈGLE DA.95]** **Sources**, téléchargées par script Python : fichiers fournis par la personne ; Wikimedia Commons, API sans clé (`https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrnamespace=6&prop=imageinfo&iiprop=url|extmetadata&format=json`), qui donne l'auteur et la licence, avec une pause d'une seconde entre deux requêtes (sinon erreur 429) ; visuels officiels de produit d'une marque réelle, pris sur son site, crédit « © marque » ; Natural Earth pour les cartes (`https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip`), dessinées en SVG ; Unsplash et Pexels (licence libre), avec l'auteur et l'adresse de la page de la photo ; une seule famille de pictogrammes (Lucide ou Phosphor), pour une catégorie qui revient.

**[RÈGLE DA.96]** **Crédit** dans `travail/credits.md`, et sous l'image.

**[IMPÉRATIF DA.97]** **Interdit** : image générée imitant une photo ; photo de stock générique (poignée de main, ampoule, fusée) ; folklore national, sauf demande.

**[RÈGLE DA.98]** **Un seul traitement d'image** pour tout le livrable, appliqué par script, jamais par un filtre CSS. **Texte sur image** : voile uni de la couleur d'encre, à 55 à 70 %, ou zone calme ; contraste mesuré sur le résultat. **Chaque image ne sert qu'une fois** et prouve une idée de sa page.
