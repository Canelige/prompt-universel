Qui le lit, et quand : la discussion de projet, en phase 9, pour la liste de contrôle et le compte rendu final ; `diapo-redacteur` pour la seule « fiche de maîtrise » ; le chef, pour relayer le compte rendu et tenir `profil.md` et `ETAT_COURANT.md`.

# Phase 9 · Livraison

## Liste de contrôle

**[IMPÉRATIF P9.1]** Chaque critère de jugement est couvert, sa page est indiquée.

**[IMPÉRATIF P9.2]** Chaque chiffre affiché figure dans `03_verification.md`, avec son verdict.

**[IMPÉRATIF P9.3]** Hypothèses au registre. **Zéro crochet dans le livrable final** : les `[à compléter]` ne vivent que dans les fichiers de travail. Avant la livraison, demande à la personne, par le chef et en une seule question (arrêt E), les éléments manquants (noms de l'équipe ou de l'auteur, règle de l'école ou de l'entreprise sur l'IA). S'il en manque encore : « version à compléter » dans le nom du fichier (`_version-a-completer`), zone concernée vide ou phrase reformulée sans elle, trous listés dans le compte rendu final.

**[RÈGLE P9.4]** `07_controles.md` affiche `ok` partout, ou chaque défaut figure sous RESTE.

**[IMPÉRATIF P9.5]** L'audit est fait, ses points GRAVE et MOYEN sont corrigés.

**[RÈGLE P9.6]** L'annexe Sources suit le format demandé par le destinataire (APA par défaut) ; crédits des images donnés. Pages et intervalles : le tiret court du clavier (12-15) remplace le demi-tiret de l'APA.

**[IMPÉRATIF P9.7]** La déclaration d'usage de l'IA est jointe, si l'école ou l'entreprise l'exige.

**[IMPÉRATIF P9.8]** **Test de singularité** : remplace mentalement le nom de l'entreprise ou du pays par un autre ; si presque tout reste vrai, la page est générique et repasse en phase 2. Écris en une ligne, dans `PREUVES.md`, les 3 choses qui rendent ce travail identifiable comme celui de cette personne.

**[RÈGLE P9.9]** `travail/fiche_maitrise.md` existe (en Express, dernière section de `03_verification.md`), écrite par `diapo-redacteur` d'après `02_contenu.yaml` et `03_verification.md`, puis passée par `humanizer` : par page, l'idée à retenir, l'origine de chaque chiffre, la question que le destinataire poserait (professeur, client, jury). La personne la lit avant l'oral.

**[IMPÉRATIF P9.10]** **`humanizer`, puis contrôle anti-IA final**, sur tout ce qui est livré : texte du livrable, notes du PPTX (lues avec `python-pptx`), `oral.md`, `fiche_maitrise.md`, annexes, déclaration d'usage de l'IA. Chaque fichier porte « humanizer passé » dans un statut ; puis le script tourne.

**[IMPÉRATIF P9.11]** Résultat attendu de **zéro** : U+2014, U+2013, émojis, « Lorem », « TODO », crochet `[à compléter]`, tics sans condition de la phase 4 (crucial, incontournable, synergie, holistique…).

**[RÈGLE P9.12]** Tics à condition (« clé », « enjeu », « permettre de ») : comptés par page ; au-delà d'un par page, la phrase repasse par la phase 4. « Enjeu chiffré » dans la synthèse et « sans clé d'accès » restent permis.

**[RÈGLE P9.13]** Refonte ciblée, pages non modifiées : le script remplace seulement les tirets (virgule, deux-points ou « de … à »), sans autre réécriture.

**[RÈGLE P9.14]** Résultat collé dans `PREUVES.md`. 2 passes au plus ; ce qui reste se corrige à la main, car un seul résultat fait échouer la livraison (`principes.md`, principe 8).

**[RÈGLE P9.15]** Le livrable final est dans `<sous-dossier>/livraison/`, ouvert et vérifié dans le format demandé.

**[RÈGLE P9.16]** Écris au chef, dans le compte rendu, la ligne d'historique pour `profil.md` (date de rendu, sujet, livrable, direction, palette, polices, usage consommé), tes observations et la question du retour à poser (note, commentaires, suite donnée) ; le chef met `profil.md` à jour.

**[RÈGLE P9.17]** `ETAT.md` du travail : PHASE = livré, PROCHAIN GESTE = « demander le retour du destinataire (note, commentaires, suite donnée) ». Le chef met la ligne du projet dans `ETAT_COURANT.md` à « livré le <date> : demander le retour », marque la discussion comme terminée si l'application le permet, puis propose `/compact` de la discussion de projet : tout est dans `profil.md`, `ETAT_COURANT.md` et le sous-dossier.

## Le compte rendu final

**[RÈGLE P9.18]** La discussion de projet écrit `<sous-dossier>/livraison/rapport.md`, 10 lignes au plus :
1. Fichiers livrés, avec chemin complet, dans `<sous-dossier>/livraison/`.
2. Note des critères et total des 10 tests, avant et après corrections, avec les principales corrections (avis de relecteur ; un audit non indépendant se dit auto-relecture) ; verdict du décideur : signe ou non, et pourquoi.
3. Mode réellement appliqué, allègements faits ; les 3 objections les plus fortes des experts, et ce que tu en as fait.
4. Hypothèses qui restent, chiffres non trouvés, skills absentes.
5. Ce que la personne doit compléter (liste exacte des trous si le fichier porte « version à compléter »), polices à installer s'il y en a.
6. Planche des miniatures ; en refonte, planche avant/après.
7. Ce qui est à noter dans `profil.md`, usage consommé par ce travail.
8. Pour chaque contrôle annoncé : VÉRIFIÉ, PARTIELLEMENT VÉRIFIÉ, NON VÉRIFIÉ ou NON DISPONIBLE.

**[IMPÉRATIF P9.19]** Jamais « vérifié » pour un contrôle qui n'a pas tourné.

**[RÈGLE P9.20]** Le chef relaie en 3 à 6 lignes : le livrable, la note estimée, le verdict du décideur, ce qui reste à compléter ; il ouvre la planche (`open` ou `start`) et le chemin de `rapport.md` ; il dit en une ligne ce qu'il a noté (« J'ai noté que… »).
