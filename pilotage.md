Qui le lit, et quand : la discussion de projet, à son ouverture et à chaque reprise ; le chef, quand il relaie un arrêt ou conseille sur l'usage. Jamais un agent.

# Pilotage : quand tu avances, quand tu t'arrêtes

« Tu » désigne ici la discussion de projet ; quand le chef mène lui-même le projet (`demarrage.md`, « Sans discussion séparée possible »), c'est lui. Tout message « à la personne » passe par `travail/POUR_LE_CHEF.md` et le chef (`demarrage.md`, « Les discussions de projet »).

## Les arrêts

**[RÈGLE PI.1]** **Les phases :** 1 Cadrage ; 2 Contenu ; 3 Faits et chiffres ; 4 Écriture ; 5 Direction artistique ; 6 Fabrication ; 7 Contrôles ; 8 Auto-audit et corrections ; 9 Livraison. Tu les enchaînes sans rien demander et tu ne t'arrêtes que dans les cinq cas ci-dessous (l'installation et l'étape 0 ont leurs propres arrêts).

**[RÈGLE PI.2]** **A. Questions**, au démarrage : l'étape C (`demarrage.md`), posée par le chef.

**[RÈGLE PI.3]** **B. Aperçu**, fin de la phase 1. Écris `travail/arret_B.md` avec : la question et la réponse, une phrase chacune ; si ta réponse diffère de l'avis de la personne, l'écart et le chiffre qui l'explique ; la liste des titres ; les 3 objections les plus fortes de l'expert et ce que tu en as fait ; les choix faits à la place de la personne ; le chemin complet de la planche des 3 directions. Puis, dans `POUR_LE_CHEF.md`, en 6 lignes au plus : l'essentiel et deux questions. Le chef ouvre la planche (`open` sur Mac, `start` sous Windows) et relaie.
- Question 1 : « Je pars sur la direction 1 avec ces titres ? » a) oui ; b) direction 2 ; c) direction 3 ; d) je corrige les titres.
- Question 2, avec les deux collectes de première main, une ligne chacune (quoi, auprès de qui, combien, durée), protocole prêt dans `travail/collecte/protocole.md` : « e) on fait la collecte 1 ; f) la 2 ; g) aucune ».
- Ajoute : « Lis aussi ton usage et donne-moi les deux pourcentages. »

**[IMPÉRATIF PI.4]** **La collecte.** Si la personne en fait une, elle dépose les réponses brutes dans `travail/collecte/` et écrit « collecte déposée » au chef avant la phase 7 ; tu l'intègres au prochain arrêt C. Tu n'écris jamais toi-même un résultat de collecte.

**[RÈGLE PI.5]** **L'arrêt B en Express** : pas de planche, tu appliques l'énergie de l'étape C et l'unique direction retenue ; si l'usage relevé à l'arrêt A dépasse 60 %, l'arrêt B est maintenu, réduit aux titres et au relevé d'usage ; sinon tu envoies les titres au chef et tu continues sans attendre.

**[RÈGLE PI.6]** **C. Compactage**, à la fin des phases 3 et 7, ou après 8 ordres de mission depuis le dernier compactage, ou à la livraison (phase 9), une fois qu'aucun agent ne tourne (tous leurs statuts lus) : mets `ETAT.md` à jour, écris l'arrêt C dans `POUR_LE_CHEF.md`, puis **termine ton tour**. Le chef, lui, propose `/compact` dans sa propre conversation à « Nouveau travail » si son contexte dépasse 50 %.

**[RÈGLE PI.7]** **Message de l'arrêt C**, que le chef transmet mot pour mot : « Pause d'économie. Ouvre la discussion <titre>, tape `/compact garde la phase en cours, les décisions de la personne et les ordres en cours`, puis écris-y « continue ». Ensuite, lis ton usage et donne-moi les deux pourcentages. »

**[RÈGLE PI.8]** **D. Forfait** : une jauge relevée dépasse 90 %, ou Claude Code annonce une limite de session ou de semaine. Mets `ETAT.md` à jour, écris l'arrêt D au chef, puis termine ton tour. Le chef écrit : « Je m'arrête pour garder une marge. Quand l'anneau ou `/usage` montre que ton forfait est réinitialisé, reviens me voir et écris : continue. On reprendra au PROCHAIN GESTE. »

**[RÈGLE PI.9]** **Une limite propre à Opus n'est pas un arrêt D**, et c'est la seule exception à « le chef reste en Opus » : le chef propose d'attendre l'heure de fin de la limite ou de continuer en Sonnet jusqu'à elle ; note « chef en Sonnet » dans `ETAT.md` ; dès qu'elle passe, le chef demande de rechoisir Opus dans le sélecteur de modèle.

**[RÈGLE PI.10]** **E. Blocage réel** : consignes contradictoires, fichier illisible, outil introuvable après installation ; avant la phase 9, des éléments que seule la personne connaît (noms de l'équipe ou de l'auteur, règle de l'école ou de l'entreprise sur l'IA). Une question courte au chef, avec des choix ou une liste à remplir. Des agents introuvables ne sont pas un arrêt : « Sans agents », en une ligne.

**[RÈGLE PI.11]** **Des critères introuvables ne sont pas un blocage** : écris des critères présumés (`phase-1-cadrage.md`) et continue.

**[RÈGLE PI.12]** **Limite en plein tour** : rien ne s'écrit, `ETAT.md` fait foi à la reprise. Un agent dont le statut n'est pas `FIN: OK` est relancé neuf, avec « reprends après les lignes déjà écrites dans <fichier> » (son identifiant ne survit pas à une nouvelle session).

## Les seuils d'usage

**[RÈGLE PI.13]** L'usage est un pourcentage déjà consommé, sur la jauge la plus remplie. Si l'application te le donne, lis-le toi-même et retire la demande des pourcentages des messages A, B et C ; sinon la personne le donne au chef à ces arrêts.

**[IMPÉRATIF PI.14]** Sans lecture, ne devine jamais l'usage.

**[RÈGLE PI.15]**
- **Au démarrage** : la table des modes (`demarrage.md`, D).
- **Au-dessus de 50 %** : jamais de changement de modèle ; tu conseilles.
- **Au-dessus de 70 %** : allège la suite dans cet ordre, en t'arrêtant dès que c'est suffisant, et dis-le en une ligne : 1. phase 8 avec le destinataire, le décideur et le directeur artistique seulement (ces trois regards restent dans tous les modes : la qualité visuelle prime l'économie) ; 2. pas de second tour d'audit ; 3. vérification web limitée aux chiffres de poids A, décidée dès l'arrêt B (la phase 3 est finie avant le premier arrêt C).
- **Au-dessus de 90 %** : l'arrêt D.

## Surveiller l'usage, et conseiller

**[RÈGLE PI.16]** **Lis les jauges toi-même si tu le peux** (un outil de l'application de bureau : 5 heures, semaine, par modèle, heure de remise à zéro, usage payant) : à l'ouverture de chaque session, au début de chaque phase (avant la phase 8, la plus coûteuse, surtout) et à chaque fin de phase. Sinon, relevés de la personne aux arrêts A, B et C. Plusieurs discussions de projet partagent les mêmes jauges : le chef les surveille pour toutes.

**[RÈGLE PI.17]** **Le chef conseille tout de suite**, en une ou deux lignes :
- **50 %** : ce qui reste à faire tient-il ? Garde le mode ou allège-le.
- **70 %** : l'allègement ci-dessus.
- **85 %** : propose une pause jusqu'à l'heure de remise à zéro (donne l'heure), ou de finir seulement la phase en cours.
- **Semaine au-delà de 80 %** : garde la fin de semaine pour les rendus urgents ; gros travaux et installations après la remise à zéro hebdomadaire (donne la date).
- **Fenêtre de contexte d'une session au-delà de 50 %** : propose `/compact` à la prochaine fin de phase.

**[IMPÉRATIF PI.18]** **Usage payant activé** : préviens que l'au-delà du forfait est facturé ; ne lance jamais une phase qui le déclencherait sans l'accord explicite de la personne.

**[RÈGLE PI.19]** **À la livraison**, donne au chef l'usage consommé par ce travail ; il le note dans l'historique de `profil.md` : il calibre le mode du travail suivant.

## La mémoire du projet : `travail/ETAT.md`

**[RÈGLE PI.20]** 40 lignes au plus, rubriques fixes : PHASE et TYPE (création, refonte complète, refonte ciblée) ; MODE (Express ou Approfondi, et sa base : « temps et usage » ou « temps seul ») ; `LANGUE DU LIVRABLE : <langue>` (relevée dans `00_materiel.md`, français par défaut : tout ce qui s'imprime dans le livrable est dans cette langue, `phase-4-ecriture.md`) ; PYTHON (chemin du lanceur) ; `ATELIER : <chemin absolu>` (racine de l'atelier) ; DISCUSSION (titre et groupe) ; USAGE (à chaque relevé) ; `PAGES WEB LUES : n / plafond` (à jour à chaque retour du vérificateur) ; DÉCISIONS DE LA PERSONNE (mot pour mot, 6 lignes au plus) ; FICHIERS (seulement ceux dont le statut n'est pas `FIN: OK`) ; ORDRES EN COURS (agent, identifiant rendu par l'outil, fichier attendu) ; MISSIONS DEPUIS LE DERNIER COMPACTAGE et MISSIONS TOTAL (des nombres) ; `RENDUS COMPLETS : n / 3` (PI.31) ; `PAGES PROMISES : <min> à <max>` (DE.27, contrôlé par P6.23) ; PASSES (compteurs de boucle) ; TEMPS (début et fin de chaque phase, relevés avec la commande `date`, jamais estimés) ; RESTE (défauts acceptés) ; PROCHAIN GESTE (une phrase exacte).

**[RÈGLE PI.21]** Mets-le à jour **avant** de lancer un agent, **après** chaque fin de phase et **après chaque fichier livrable produit** (build, PDF, PPTX, Word).

**[RÈGLE PI.22]** Scripts et agents écrivent par chemin absolu : chaque commande du shell commence par `cd <ATELIER>` ou n'emploie que des chemins absolus.

**[RÈGLE PI.23]** Le `CLAUDE.md` importe le noyau, `profil.md` et `ETAT_COURANT.md` : ils reviennent après un `/compact`, un `/clear` ou une reprise ; une discussion de projet retrouve son sous-dossier par son résumé de compactage.

## Économie : la personne a un forfait Pro

**[RÈGLE PI.24]** **C'est le seul endroit des règles d'usage ; elles valent pour tous les modes** (seuils et conseils ci-dessus).

**[RÈGLE PI.25]** **Deux modes, Express et Approfondi** (table de l'étape D). Approfondi : plus de 6 h et la jauge la plus remplie à 60 % au plus. Express : tous les autres cas. Usage non lu (PI.14 interdit de le deviner) : le temps seul décide, plus de 6 h donnant Approfondi, écrit dans `ETAT.md` (« MODE : Approfondi, sur le temps seul »). Avec plus de 6 h, l'Express n'est jamais le défaut, même sur un forfait Pro : seul un usage lu au-delà de 60 % l'impose.

**[IMPÉRATIF PI.26]** **L'Express coupe le temps et les fichiers, jamais la qualité.** Il garde la vérification des chiffres décisifs, la planche regardée, le destinataire, le décideur, le directeur artistique sur la planche et tous les contrôles par script ; l'économie vient des fichiers intermédiaires, des rendus refaits pour rien et des relectures de gros fichiers. Il ne retire jamais : les critères de jugement, « rien d'inventé », les calculs par script, le contrôle des débordements, `humanizer` et la liste anti-tics de la phase 4.

**[RÈGLE PI.27]** **Le chef lit le minimum.** Jamais un gros fichier : seulement `00_materiel.md`, les sorties de script, les statuts, les planches de miniatures, les sections tirées au sort par la porte, et les fichiers courts qu'il signe (`principes.md`, « La posture du chef »).

**[RÈGLE PI.28]** **Le chef reste en Opus**, quel que soit l'usage : il pense, répartit, vérifie, tranche (seule exception : une limite propre à Opus, arrêt D). Si le forfait ne propose pas Opus, dis-le et continue en Sonnet. Il en va de même pour chaque discussion de projet.

**[RÈGLE PI.29]** **Les agents font le volume** : `diapo-*` en Sonnet, sauf `diapo-lecteur` (Haiku) et `diapo-expert` (le modèle du chef, Opus). Modèle fixé dans leur fichier : ne leur passe jamais de paramètre `model`, ne lance jamais d'agent en fork.

**[RÈGLE PI.30]** **Le travail mécanique passe à Haiku** (`diapo-lecteur`) : copies, relevés, tests de lecture. Ce qu'un script fait se fait par script, jamais à la main : sommes, comptages, tirets, numéros de page, débordements, tirages, choix de pages.

**[IMPÉRATIF PI.31]** **3 rendus complets du livrable au plus**, premier rendu et corrections de l'audit compris, **comptés dans `ETAT.md`** (`RENDUS COMPLETS : n / 3`). `build.py` appelé sans `--pages` lit ce compteur, refuse un quatrième rendu (« plafond de rendus complets atteint ») et l'incrémente avant de rendre ; la porte de chaque phase compare le compteur aux PDF complets de `travail/rendus/`, horodatés, et un écart fait échouer la porte. Ensuite, seules les pages fautives sont rendues (« Plafonds de boucle ») et remplacent leurs pages dans le PDF livré par PyMuPDF (`insert_pdf`), hors compteur, puis `livrable.txt` est régénéré (recette : `phase-6-fabrication.md`, P6.2). Les images se regardent en planches de 6 pages ; une page ne s'ouvre en grand que si un script ou une planche la signale ; après une correction, on ne rend que les pages modifiées.

**[RÈGLE PI.32]** **Avant de lancer un rendu, annonce l'usage que tu estimes** (en % de session et de semaine).

**[CONSEIL PI.33]** Coût mesuré d'un rendu Express (essai n°6, A4 de 10 pages, 13 feuilles) : 1 h 17 ; 17 agents ; 2 rendus complets ; 10 pages web ; 68 millions de tokens traités dont 21 en Opus, 46 en Sonnet, 1,4 en Haiku (4,4 millions hors lectures de cache) ; le fabricant pèse plus de la moitié des agents, le chef près d'un tiers. **La mesure est celle des tokens traités** (entrée, écriture et lecture de cache, sortie), lue dans les journaux `subagents/agent-<id>.jsonl` (appels dédoublonnés par identifiant de message) et dans le tien, **pas la taille de contexte donnée par la notification de fin d'agent**, qui ne dit que la taille du dernier appel. **Un sous-agent coûte environ 100 000 tokens dès son premier appel** (contexte de départ chargé par l'outil) : en Express, un seul lecteur Haiku pour tout le test écran (P7.19), jamais un par lot. Ce rendu a fait passer la jauge de 5 heures d'un forfait Team de 53 % à 72 % et la semaine de 16 % à 19 %, d'autres discussions tournant en parallèle (majorant : le rendu seul a coûté moins).

**[RÈGLE PI.34]** **Une longue conversation coûte à chaque reprise** (tout le contexte est relu en Opus) : dès qu'un travail est livré, le chef propose `/compact` de la discussion de projet ; l'état est dans `profil.md`, `ETAT_COURANT.md` et le sous-dossier. Hors travail (conseil, discussion), le chef répond court.

**[RÈGLE PI.35]** **Ordre de mission, 8 lignes au plus** : le rôle ; le module à lire (chemin absolu dans `universel/`) et sa sous-section `###` utile plutôt qu'un module entier ; les fichiers à lire et à écrire, par chemin ; le chemin du statut ; le chemin du lanceur Python ; les interdits ; le plafond de réponse, 6 lignes. Jamais ton raisonnement.

**[RÈGLE PI.36]** **Les skills lourdes** (`impeccable`, `pptx`, `frontend-slides`, `ui-ux-pro-max`, `marketing-skills`) se chargent dans l'agent qui s'en sert, jamais dans ton contexte.

**[RÈGLE PI.37]** `marketing-skills` : `diapo-expert` et `diapo-redacteur`, quand le domaine touche au marketing, à la stratégie ou au commercial. Ils chargent la ou les deux méthodes utiles (`marketing-plan`, `pricing`, `competitor-profiling`, `customer-research`, `product-marketing`, `launch`) comme grille de rigueur, jamais comme source de chiffres. Les outils de la référence passent avant elles.

**[RÈGLE PI.38]** `ui-ux-pro-max` : `diapo-fabricant`, en phase 5, comme catalogue de plus pour les palettes, les accords de polices et les types de graphiques. Il ne passe jamais avant le sujet, la marque, le goût et « beau d'abord ».

## Ce que change l'Express, en un seul endroit

**[RÈGLE PI.39]** Cible : 1 h à 1 h 30.

| Phase | En Express |
|---|---|
| 1 | Ghost deck court ; seuls les 2 chiffres les plus décisifs sont recoupés par deux sources ; le test des titres et la contre-expertise restent. |
| 2 | 5 pièces de rigueur au plus (les pièces exigées par le cas en sus). |
| 3 | 10 pages web lues au plus (P3.15), lignes A seulement (pages de tarifs d'une proposition : `phase-3-faits.md`). |
| 4 | `humanizer` seul, sans `stop-slop`. |
| 5 | Pas de planche des directions : l'énergie choisie à l'étape C en tient lieu, le reste de la direction se choisit par raisonnement (« Anti-générique »). 5 gabarits au plus, 2 familles de polices. |
| 6 | PDF seulement, plus le PPTX si les consignes l'exigent. |
| 7 | Contrôles par script et test écran, dans le plafond de rendus. Une planche de contrôle est permise juste après le premier PDF, en plus de celle d'après les corrections. |
| 8 | Le destinataire et le décideur, plus le directeur artistique en un seul temps (le regard neuf sur la planche, sans `05_charte.md`). |
| 9 | Liste de contrôle complète. |

**[RÈGLE PI.40]** **Fichiers de l'Express** : six, `ETAT.md`, `01_cadrage.md` (avec les titres et la contre-expertise), `02_contenu.yaml`, `03_verification.md`, `build.py` et le livrable. `build.py` porte aussi la charte (thèse éditoriale et tableau des rôles en commentaire de tête, jetons, gabarits) et les contrôles de la phase 7, en fonctions : en Express, « `05_charte.md` », « `tokens.css` » et « `gabarits.css` » désignent ce commentaire et ces fonctions, et la direction artistique choisie sans planche (table ci-dessus, phase 5) s'y écrit aussi : pas de `direction_express.md`. Pas de `controles.py` ni de `fiche_maitrise.md` à part : la fiche est la dernière section de `03_verification.md`, ta revue hostile (`revue_chef.md`, toujours écrite) une section de `01_cadrage.md`.

**[RÈGLE PI.41]** Restent permis en Express, car une règle les fait lire à un script, à un agent ou à un lecteur neuf : `statuts/`, `portes.py`, `calculs.py`, `chiffres_geles.txt`, `donnees.csv`, `credits.md`, `titres_seuls.txt`, `objections.md` (tes réponses aux objections, exigées par P1.25 et lues par la porte, PI.44), `prep_audit.py` (copie par script ce que reçoivent les auditeurs, P8.9), `PREUVES.md`, `POUR_LE_CHEF.md`, `REPONSES.md`, `audit/`, et `tirer.py` avec sa graine s'il reste un tirage.

## Vérifier sans relire

**[RÈGLE PI.42]** **Les statuts.** Chaque agent tient `travail/statuts/<phase>_<nom>.txt`, sur 3 lignes : AGENT, LU, FIN. Sans `FIN: OK`, un travail n'est pas livré, mais les lignes écrites restent : on reprend après elles.

**[RÈGLE PI.43]** Un agent coupé se reprend, il ne se relance pas de zéro : SendMessage avec l'identifiant noté dans ORDRES EN COURS, « continue à partir de ce qui existe ». Identifiant manquant ou session nouvelle : agent neuf avec « des fichiers existent déjà ; lis-les, complète-les, ne réécris pas ce qui est fait ».

**[RÈGLE PI.44]** **La porte.** `python travail/portes.py <phase>` est un script qui grandit avec le travail. Phase 1, tu l'écris avec les seuls contrôles de la phase 1 : chaque critère a sa page, chaque titre tient dans sa limite de mots, chaque objection a sa réponse dans `objections.md`. À l'entrée des phases 2, 3 et 4, après avoir lu leur module, ajoute-y leurs règles chiffrées. Les règles des phases 5 et 6 vivent dans `travail/controles.py`, écrit par `diapo-fabricant`.

**[RÈGLE PI.45]** Teste chaque contrôle sur un fichier volontairement fautif avant de t'en servir.

**[RÈGLE PI.46]** **Le sondage.** `portes.py` tire au sort 3 sections du fichier rendu et les affiche ; tu les lis en entier (le tirage, ce n'est pas toi qui le fais).

**[RÈGLE PI.47]** Porte et sondage vont dans `travail/PREUVES.md`, une ligne par section : « lue, RAS » ou « lue, défaut X ».

## Plafonds de boucle

**[RÈGLE PI.48]**

| Où | Plafond | Ensuite |
|---|---|---|
| Porte en échec, toute phase | 1 renvoi à l'agent, avec la liste exacte des défauts | défaut sous RESTE, on continue |
| Test des titres (phase 1) | 2 passes | on garde la meilleure version |
| Porte de la phase 4 | 2 passes | RESTE |
| Rendus complets du livrable (premier rendu et corrections de l'audit compris, tous modes) | 3 (« Économie ») ; ensuite, seules les pages fautives sont rendues, en 3 passes de contrôle au plus ; on s'arrête si les défauts ne baissent pas | RESTE |
| Rapport d'auditeur refusé (phase 8) | 1 relance | RESTE |
| Écart trouvé par le vérificateur (phase 8) | 1 écart : on corrige la ligne et on rouvre 5 lignes du même type. 2 écarts : une seule relance de la phase 3, limitée aux lignes A | RESTE |
| Agent coupé ou statut PARTIEL | 2 reprises, chacune avec la liste de ce qui manque | la partie manquante sous RESTE |
| Total des missions du travail (`MISSIONS TOTAL` de son `ETAT.md`) | 45 ; au-delà, seules les phases 8 et 9 lancent encore un agent | RESTE, annoncé au chef |
| Corrections de la phase 8 | 1 tour, puis un re-contrôle ciblé ; un second tour complet seulement en Approfondi, une fois | RESTE, avec son effet sur la note |

**[CONSEIL PI.49]** Un livrable avec ses défauts annoncés vaut mieux qu'une boucle sans fin.

## Sans agents

**[RÈGLE PI.50]** **Outil sans agents, ou agents `diapo-*` introuvables après l'installation** : fais chaque mission toi-même, dans l'ordre, avec les mêmes fichiers ; chaque fichier de rôle porte en tête « rôle simulé, non indépendant », reprise dans son statut ; entre deux rôles, relis seulement le fichier du rôle précédent et le module de ce rôle.

**[IMPÉRATIF PI.51]** **Les rôles simulés ne sont pas indépendants.** Test des titres, contre-expertise et audit, dans cet ordre :
1. un sous-agent générique de l'outil, avec le seul fichier à lire (`audit/` pour l'audit) ;
2. sinon une nouvelle discussion dans le même dossier, que la personne ouvre avec : « Lis uniquement audit/ et applique audit/consignes_audit.md, angle <angle>. Écris audit/rapport_<angle>.md et audit/statut_<angle>.txt. Termine par la liste des fichiers lus. » ;
3. sinon toi-même : le rapport écrit « audit non indépendant », la note est une auto-relecture, jamais une estimation fiable.
