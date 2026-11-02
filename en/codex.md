Who reads it, and when: the lead, from the first message, if not running in Claude Code (Codex, Cursor...), in place of the Claude Code-specific parts of `installation.md`.

# A tool other than Claude Code (Codex, Cursor...)

**[RULE CX.1]** **First of all, in Codex.** A folder outside Git opens read-only, and the network is off by default. Ask the person to add these lines to `~/.codex/config.toml`, then to reopen Codex in the folder:

    sandbox_mode = "workspace-write"
    [sandbox_workspace_write]
    network_access = true

**[RULE CX.2]** Without this, neither the `.venv`, nor the fonts, nor the web sources get through. The skills install outside the folder: Codex will ask for an approval, which the person accepts.

**[TIP CX.3]** Check these keys against the Codex documentation, which is the authority.

**[RULE CX.4]** Usage is read with the tool's command (`/status` in Codex); the percentage thresholds remain.

**[RULE CX.5]** **Keep the same way of working whenever the tool allows it** (Codex has its subagents, its `SKILL.md` skills and an `AGENTS.md` memory file: consult the tool's documentation for the exact format).

**[RULE CX.6]** **The subagents.** Recreate the seven agents from `universel/agents/` in the tool's format, with the same role, the same common body and the same tools. Models: the most capable for the lead; an intermediate model for the others, with a high effort for `diapo-expert`; the lightest for `diapo-lecteur`.

**[RULE CX.7]** All the modules apply, except what is specific to Claude Code: `/usage`, `/autocompact`, `/model`, the gauge ring, `SendMessage`, the fork, the `model` parameter, `omitClaudeMd`, `maxTurns`, the `@` import, the isolation check by log, the session and sidebar tools of the desktop app.

**[RULE CX.8]** Fallbacks:
- without a usage readout, the mode is chosen on the person's time alone, and stop D triggers when the tool announces a limit;
- a cut-off agent is resumed by a new agent;
- `AGENTS.md` carries the line "Read `universel/UNIVERSAL_PROMPT.md`, `profil.md`, then `ETAT_COURANT.md`, then, in a project chat, the `ETAT.md` of its subfolder, first" in place of the imports;
- the audit reports carry the mention "isolation not verified";
- the project chats: if the tool opens several conversations in the same folder, give the person the exact steps in one or two lines (`demarrage.md`, "The project chats"); otherwise, run the project in your conversation.

**[RULE CX.9]** **The skills.** Install `humanizer` (always), `stop-slop`, `impeccable`, `ui-ux-pro-max` and `marketing-skills` the tool's way: its skills folder, or `npx skills add <repo> -a <tool>`. The `claude plugin` plugins do not apply. A skill that cannot be installed is replaced by the matching rule in the modules.

**[RULE CX.10]** **Memory** is written in the tool's instruction file (`AGENTS.md` for Codex, at the root), with the content of the `CLAUDE.md` template from `installation.md`, plus `travail/ETAT.md`. Compaction follows the tool's commands.

**[RULE CX.11]** **The workshop installation** is limited to the basic tools (I1). Step 0 skips the points specific to Claude Code: the `settings.json` and the restart.

**[RULE CX.12]** **Only if the tool has no subagents:** apply "Without agents" (`pilotage.md`). Each mission brief becomes a step that you do yourself, with the same files and the same statuses, rereading only the module cited.
