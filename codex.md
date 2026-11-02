Qui le lit, et quand : le chef, dès le premier message, s'il ne tourne pas dans Claude Code (Codex, Cursor…), à la place des parties propres à Claude Code de `installation.md`.

# Autre outil que Claude Code (Codex, Cursor…)

**[RÈGLE CX.1]** **Avant tout, dans Codex.** Un dossier hors Git s'ouvre en lecture seule, et le réseau est coupé par défaut. Demande à la personne d'ajouter ces lignes dans `~/.codex/config.toml`, puis de rouvrir Codex dans le dossier :

    sandbox_mode = "workspace-write"
    [sandbox_workspace_write]
    network_access = true

**[RÈGLE CX.2]** Sans cela, ni le `.venv`, ni les polices, ni les sources web ne passent. Les skills s'installent hors du dossier : Codex demandera une approbation, que la personne accepte.

**[CONSEIL CX.3]** Vérifie ces clés dans la documentation de Codex, qui fait foi.

**[RÈGLE CX.4]** L'usage se lit avec la commande de l'outil (`/status` dans Codex) ; les seuils en pourcentage restent.

**[RÈGLE CX.5]** **Garde le même fonctionnement chaque fois que l'outil le permet** (Codex a ses sous-agents, ses skills `SKILL.md` et un fichier de mémoire `AGENTS.md` : consulte la documentation de l'outil pour le format exact).

**[RÈGLE CX.6]** **Les sous-agents.** Recrée les sept agents de `universel/agents/` dans le format de l'outil, avec le même rôle, le même corps commun et les mêmes outils. Modèles : le plus capable pour le chef ; un modèle intermédiaire pour les autres, avec un effort élevé pour `diapo-expert` ; le plus léger pour `diapo-lecteur`.

**[RÈGLE CX.7]** Tous les modules s'appliquent, sauf ce qui est propre à Claude Code : `/usage`, `/autocompact`, `/model`, l'anneau de jauge, `SendMessage`, le fork, le paramètre `model`, `omitClaudeMd`, `maxTurns`, l'import `@`, le contrôle d'isolement par journal, les outils de sessions et de barre latérale de l'application de bureau.

**[RÈGLE CX.8]** Replis :
- sans relevé d'usage, le mode se choisit sur le temps du groupe seul, et l'arrêt D se déclenche quand l'outil annonce une limite ;
- un agent coupé se reprend par un agent neuf ;
- `AGENTS.md` porte la ligne « Lis `universel/PROMPT_UNIVERSEL.md`, `profil.md`, puis `ETAT_COURANT.md`, puis, dans une discussion de projet, le `ETAT.md` de son sous-dossier, en premier » à la place des imports ;
- les rapports d'audit portent la mention « isolement non vérifié » ;
- les discussions de projet : si l'outil ouvre plusieurs conversations dans le même dossier, donne à la personne les gestes exacts en une ou deux lignes (`demarrage.md`, « Les discussions de projet ») ; sinon, mène le projet dans ta conversation.

**[RÈGLE CX.9]** **Les skills.** Installe `humanizer` (toujours), `stop-slop`, `impeccable`, `ui-ux-pro-max` et `marketing-skills` à la façon de l'outil : son dossier de skills, ou `npx skills add <dépôt> -a <outil>`. Les plugins `claude plugin` ne s'appliquent pas. Une skill impossible à installer se remplace par la règle correspondante des modules.

**[RÈGLE CX.10]** **La mémoire** s'écrit dans le fichier d'instructions de l'outil (`AGENTS.md` pour Codex, à la racine), avec le contenu du modèle `CLAUDE.md` de `installation.md`, plus `travail/ETAT.md`. Le compactage suit les commandes de l'outil.

**[RÈGLE CX.11]** **L'installation de l'atelier** se limite aux outils de base (I1). L'étape 0 saute les points propres à Claude Code : le `settings.json` et le redémarrage.

**[RÈGLE CX.12]** **Seulement si l'outil n'a pas de sous-agents :** applique « Sans agents » (`pilotage.md`). Chaque ordre de mission devient une étape que tu fais toi-même, avec les mêmes fichiers et les mêmes statuts, en relisant seulement le module cité.
