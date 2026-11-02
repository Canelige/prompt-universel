Qui le lit, et quand : la discussion de projet, quand `ETAT.md` porte `TYPE : refonte complète` ou `TYPE : refonte ciblée`, à l'ouverture et à chaque reprise ; `diapo-documentaliste` pour le seul point 2. Quand ce module diverge d'une phase, il l'emporte.

# Mode refonte

**[RÈGLE RF.1]** **D'abord la note et les commentaires du professeur** : première liste de défauts.

**[RÈGLE RF.2]** **Extraction**, par `diapo-documentaliste` : PPTX, `python -m markitdown ancien.pptx` (texte, notes) puis les images de `ppt/media` ; PDF, PyMuPDF ; rendu en images, `soffice --headless --convert-to pdf` si LibreOffice est installé (Windows : `C:\Program Files\LibreOffice\program\soffice.exe`). Sans LibreOffice : diagnostic sur le texte, rapport « mise en page de l'ancien rendu non évaluée ».

**[IMPÉRATIF RF.3]** Un rendu LibreOffice n'a pas les polices d'origine : jamais de débordement de l'ancien travail signalé sans confirmation.

**[RÈGLE RF.4]** **Diagnostic**, après la phase 1 : l'auditeur « professeur » note l'ancien travail.

**[IMPÉRATIF RF.5]** **Garder la substance** : faits justes, décisions du groupe, analyses demandées et ordre imposé restent ; le faux est corrigé et signalé, ce qui manque à la grille ajouté et signalé. Réponse « forme seulement » : le fond ne change que pour corriger une erreur.

**[RÈGLE RF.6]** **Refonte complète** (Standard, Approfondi) : toutes les phases ; format de sortie par défaut celui de l'original (PPTX d'origine : un PPTX modifiable et un PDF).

**[RÈGLE RF.7]** **Refonte ciblée** (Express, ou moins de 2 h 30) : édition en place. Livrable : copie du PPTX d'origine dans `<sous-dossier>/livraison/` ; la skill `pptx` la déballe, on modifie les 5 pages les plus faibles d'après les commentaires et celles qui couvrent les critères manquants, on la remballe. Les autres pages ne bougent pas.

**[RÈGLE RF.8]** Charte de l'original gardée ; pas de graine, pas de directions, pas d'arrêt B, pas de `build.py`. On corrige ce que les commentaires reprochent (lisibilité, contraste, hiérarchie, titres, chiffres). Texte modifié : phase 4 ; contrôle final de la phase 9 sur tout le fichier, pages non modifiées comprises.

**[IMPÉRATIF RF.9]** Contrôle : `soffice` convertit la copie en PDF, PyMuPDF tire les PNG des seules pages modifiées ; sans LibreOffice, « aucune page vérifiée visuellement », jamais `ok`.

**[IMPÉRATIF RF.10]** Audit d'une refonte ciblée : le professeur, le client et le directeur artistique sur les pages reprises (les trois regards de `phase-8-audit.md`).

**[RÈGLE RF.11]** **Le parcours court** : phase 1 réduite au diagnostic du professeur sur l'ancien rendu, à la liste des pages à reprendre et à l'expert sur ce seul diagnostic ; pas de ghost deck complet, pas de test des titres ; vérification web limitée aux chiffres des pages reprises. Ensuite : phase 4 sur les phrases modifiées, contrôle, audit, livraison.

**[RÈGLE RF.12]** **À la livraison** : une planche avant/après, la liste des changements page par page, la note estimée avant et après.
