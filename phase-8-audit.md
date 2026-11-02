Qui le lit, et quand : la discussion de projet, en phase 8, pour préparer `audit/`, lancer les auditeurs et arbitrer ; les auditeurs ne le lisent jamais directement : un script copie « Ce que fait chacun » (sans les blocs « Chef : ») et `principes.md` dans `audit/consignes_audit.md`.

# Phase 8 · Auto-audit, puis corrections (`diapo-auditeur`, Sonnet)

**[CONSEIL P8.1]** **Limites** : l'auditeur est le même modèle que le rédacteur, avec les mêmes angles morts ; le gain vient de l'isolement et de l'obligation de preuve.

**[IMPÉRATIF P8.2]** La note est un avis de relecteur, jamais une prévision.

## Préparation, par script

**[RÈGLE P8.3]** `audit/` contient seulement : le PDF et `livrable.txt` ; `titres.txt` (les seuls titres, dans l'ordre) ; `consignes_originales.txt` (énoncé, question, contraintes, extraits du document d'origine) ; `grille_originale.txt`, extraite du document d'origine et non de ta copie (grille présumée : `grille_presumee.txt`, étiquette en tête, total annoncé « sur grille présumée ») ; les pages du cours et du cas citées dans `01_cadrage.md` et les lignes CAS ; la planche des miniatures ; `objections_phase1.txt` (les 5 objections de `01_contre_expertise.md`, **sans tes réponses**) ; `cours_plan.txt` (plan du cours, outils attendus de `00_materiel.md`) ; `consignes_audit.md` (copie de `principes.md` et de « Ce que fait chacun », sans les blocs « Chef : »).

**[RÈGLE P8.4]** **En plus, selon l'auditeur.** **Vérificateur** : `03_verification.md`, `donnees.csv`.

**[RÈGLE P8.5]** **Directeur artistique** : 6 pages en grand choisies par script (couverture, synthèse, 2 graphiques, 1 rupture, décision) ; versions réduites et grises ; `interdits.txt` (« Ce qui trahit l'IA » de `direction-artistique.md` et polices-réflexes de `annexe-polices.md`, extraits par script) ; `05_charte.md`, seulement dans un second temps.

**[RÈGLE P8.6]** **Jury ou contradicteur** : le brief du cas et le rôle que le cours lui donne.

**[RÈGLE P8.7]** **Client** : `decideur.txt` (copié par script depuis le lecteur de `01_cadrage.md`) et, s'il y a une marque, son logo et ses couleurs officielles. Jamais la charte du groupe.

## Lancement

**[RÈGLE P8.8]** Les auditeurs partent **dans un même message**, en parallèle, chacun avec son angle (`professeur`, `verificateur`, `direction-artistique`, `contradicteur`, `client`), l'expert (`diapo-expert`) dans le même message. Sans agents : `pilotage.md`, « Sans agents ».

**[IMPÉRATIF P8.9]** Tout ce qu'un auditeur reçoit est copié par script dans `audit/`, jamais cité par son chemin dans `travail/`.

**[RÈGLE P8.10]** Ordre : « Lis uniquement `<sous-dossier>/audit/`, plus les pages web que tu dois rouvrir. Écris `<sous-dossier>/audit/rapport_<angle>.md` et `<sous-dossier>/audit/statut_<angle>.txt`. Termine par la liste des fichiers lus. »

**[IMPÉRATIF P8.11]** **Contrôle d'isolement** : avant de lire un rapport, `python <sous-dossier>/travail/portes.py isolement <identifiant>` ouvre le journal de l'agent (`~/.claude/projects/*/*/subagents/agent-<identifiant>.jsonl`) et liste tout appel d'outil dont l'entrée contient un chemin hors de `<sous-dossier>/audit/` : `travail`, `profil`, `ETAT_COURANT`, `universel`, `PROMPT_UNIVERSEL` ou le nom d'un autre sous-dossier. Appel listé : rapport refusé (une seule relance ; refusé deux fois, écarté et signalé sous RESTE).

**[RÈGLE P8.12]** Journal introuvable : « isolement non vérifié » dans le rapport. La liste des fichiers lus déclarée par l'agent ne prouve rien : seul le journal compte.

## Ce que fait chacun

**[IMPÉRATIF P8.13]** **Le professeur** note sévèrement. Départ : moyenne de la promotion, 12/20 ; un critère ne monte que sur une preuve citée (page et chiffre). Plafonds : question non traitée 8/20 ; recommandation absente ou contredite par les chiffres 10/20 ; chiffre inventé 12/20. Par critère : note, preuve, ce qu'il manque pour le palier suivant.

**[RÈGLE P8.14]** Puis **10 tests**, notés 0 (absent), 1 (présent mais non prouvé) ou 2 (présent, avec la page qui le prouve) :
1. **Réponse d'abord** : la première page donne la réponse, 3 raisons et sa preuve reine.
2. **Titres seuls** : à partir de `titres.txt`, l'argumentaire en 5 lignes, et l'endroit où il casse.
3. **« Et alors ? »** : pages dont la ligne du bas répète le titre ou n'a pas de conséquence.
4. **Alternatives** : deux au moins, plus le statu quo, avec la raison chiffrée du choix.
5. **Chiffres décisifs** : il identifie lui-même les 3 à 5 qui portent la décision ; datés, bon périmètre, recoupés ?
6. **Hypothèses, sensibilité et inconnues.**
7. **Objection** : écrite, avec une réponse chiffrée.
8. **Risques** : probabilité, impact chiffré, signal, parade.
9. **Exécutable** : responsable, échéance, livrable, indicateurs, critère d'arrêt.
10. **Cohérence** : même chiffre, même vocabulaire, même décision partout, aucune donnée défavorable écartée.

**[RÈGLE P8.15]** Test à 0 : point GRAVE ; test à 1 : point MOYEN ; test que la grille et la matière n'appellent pas : « sans objet ». Total des tests ramené sur 20, rendu à part de la note de la grille.

**[RÈGLE P8.16]** **Palier 17** : au-delà de 15/20 sur un critère, trois preuves, chacune avec sa page, sinon plafond à 15. 1. **Cours maîtrisé** : notions utiles d'après `cours_plan.txt` employées avec leur définition exacte, manquantes listées. 2. **Cours dépassé** : limite d'un outil du cours discutée pour ce cas. 3. **Appui savant** : deux références (auteur, année), chacune reliée à un argument.

**[RÈGLE P8.17]** **Réfutation** : en 5 lignes, la meilleure raison de rejeter la recommandation ; sans réponse du livrable : GRAVE. **Les 3 questions les plus dangereuses** : une question sans réponse dans le livrable est un point MOYEN.

**[IMPÉRATIF P8.18]** **Le vérificateur** refait chaque calcul ; rouvre l'URL des chiffres A et de 3 lignes tirées par script (un écart déclenche la règle des plafonds de boucle) ; liste les chiffres affichés absents de la table et tout ce qui est présenté comme un FAIT sans en être un ; fait **une passe de contradictions entre pages** (règle ou chiffre énoncé deux fois différemment, par exemple un seuil en points à une page et en pourcentage à une autre), avec les deux pages.

**[IMPÉRATIF P8.19]** **Le directeur artistique** (skill `impeccable`), en deux temps ; il écrit le premier avant d'ouvrir `05_charte.md`.
1. **Regard neuf** : 3 mots d'ambiance et ce que le livrable rappelle ; chaque interdit rencontré, avec page et extrait ; point focal de chaque page en grand ; lisibilité sur versions réduites et grises (aucune information sur la seule couleur) ; premier élément lu en une seconde sur chaque page en grand, et pages où deux éléments se disputent ce rang ; couverture et séparateur sans leur texte (ce qui reste d'identité) ; blancs subis plutôt que voulus, bords décalés sans raison ; les 3 pages les plus faibles.
2. **Écarts à la charte**, après lecture de `05_charte.md`, et si ses 3 mots rejoignent ceux de la direction.

**[RÈGLE P8.20]** Un interdit de `interdits.txt`, ou un regard neuf « propre, neutre, générique » : GRAVE.

**[IMPÉRATIF P8.21]** **L'expert de la branche** (`diapo-expert`, rôle tiré de la table du profil de la matière, `phase-1-cadrage.md`) lit comme ce professionnel : ce qui est faux, naïf ou non professionnel (vocabulaire, ordres de grandeur, pratiques, réglementation) ; ce qu'il ferait autrement, et pourquoi ; l'objection la plus forte de la contre-expertise est-elle bien traitée ? Un point faux dans le métier : GRAVE.

**[RÈGLE P8.22]** **Le contradicteur, ou le jury** (si le cours fait jouer ce rôle, et toujours en Approfondi) : ce qu'il refuserait de signer, la pire hypothèse, un pre-mortem.

**[IMPÉRATIF P8.23]** **Le client** (`diapo-auditeur`, angle `client`, dans tous les modes, Express compris) joue le décideur du cas : la directrice marketing de la marque s'il y a une marque, sinon le décideur que le cadrage a nommé. Il voit le livrable comme le client qui choisit l'agence ; il passe discrètement, sans jamais interrompre le groupe, et le chef applique ses corrections comme celles des autres. Il rend : l'impression des 30 premières secondes (couleur, énergie, « est-ce que je me reconnais ? ») ; ce qui donne confiance et ce qui fait douter ; « est-ce que je signe ? » ; les 3 changements qui le convaincraient.

**[RÈGLE P8.24]** Avec une marque, « je ne me reconnais pas » ou « ça ne nous ressemble pas » est GRAVE ; le client contrôle aussi la voix de marque (logo masqué).

**[IMPÉRATIF P8.25]** Tout constat cite la page, un extrait et le critère touché ; un constat sans citation est supprimé.

## Chef : qui audite selon le mode

**[IMPÉRATIF P8.26]** **Les trois regards, dans tous les modes** : le professeur, le directeur artistique et le client. Express : ces trois, le directeur artistique en un seul temps (le regard neuf) ; l'expert de la phase 1 reste obligatoire, celui de la phase 8 est sauté. Standard : professeur, vérificateur, directeur artistique, expert de la branche et client, plus le contradicteur si le cours fait jouer un jury. Approfondi : les six.

## Chef : arbitrage

**[IMPÉRATIF P8.27]** L'exactitude d'abord : un chiffre faux ou une source introuvable se corrige ou sort, quelle que soit la grille. Ensuite la grille, puis la charte : un critère que la correction laisse sans page est couvert autrement (preuve qualitative, HYPOTHÈSE chiffrée) et signalé. Chaque arbitrage tient en une ligne.

## Chef : corrections

**[IMPÉRATIF P8.28]** Tout GRAVE ou MOYEN est traité ; un point MINEUR écarté reçoit une ligne de raison.

**[RÈGLE P8.29]** Relance les portes des phases 4 et 7 sur les seules pages modifiées ; tout texte modifié repasse par `humanizer` (`phase-4-ecriture.md`).

**[RÈGLE P8.30]** Rends à nouveau les pages modifiées (rendu complet seulement s'il en reste dans le plafond) et cherche par `grep` chaque ancien chiffre dans tout le texte du livrable. L'auditeur concerné revérifie seulement les points corrigés ; la note « après » est la sienne, réestimée sur ces points, annoncée comme telle.

**[RÈGLE P8.31]** Le reste suit les plafonds de boucle (`pilotage.md`).
