Who reads it, and when: the lead alone, the first time on a computer (`~/.claude/atelier-rendus.ok` absent), then once per workshop for "The workshop" (`CLAUDE.md` absent from the root). Never an agent.

# Installing the computer and the workshop

## Installing the computer (once only)

**[RULE IN.1]** **Lead: you guide.** Before each step, explain in one or two simple sentences what you are about to do and why; when they have to act, say which button to click, what to type, and what they should see next.

**[RULE IN.2]** **Welcome message**, after getting to know them, to adapt, in 6 lines at most:
> "This is the first time on this computer: I install the workshop first, 30 to 60 minutes, one time only. Check that **Auto** mode is selected, in the selector under the text box: I will hardly have anything for you to approve. Auto mode may refuse an installation: you will see a notification, and I will tell you what to do. If the computer asks for your password, type it yourself, never here."

### I1. The basic tools

**[RULE IN.3]** Detect the system (Mac or Windows). Check `git`, `python3` (or `py`), `node`, `pdftotext` and `claude` (the command-line program), and install what is missing. Check `claude --version`: 2.1.271 or later; otherwise ask them to update the app and reopen it (without this, the auditors would read the lead's memory).

**[RULE IN.4]** **Mac.**
- Run `xcode-select -p`. If it fails, say: "An Apple window will open: click Install, accept, wait for it to finish (10 to 20 minutes), then write continue." Then run `xcode-select --install`.
- If Homebrew is missing, have them install it in the Terminal app (the password does not show while typing): give the command from brew.sh, then this line to paste: `echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile`. Wait for "continue".
- This session does not see `brew` yet: write its full path (`/opt/homebrew/bin/brew`; `/usr/local/bin/brew` on an Intel Mac). Run `/opt/homebrew/bin/brew install git python node poppler`, then, if `claude` is missing, `/opt/homebrew/bin/brew install --cask claude-code`.

**[RULE IN.5]** **Windows.** Add `--accept-source-agreements --accept-package-agreements` to each command, and warn them: "Windows will ask several times for permission to install: click Yes."
- `winget install --id Git.Git -e`, `winget install --id Python.Python.3.12 -e`, `winget install --id OpenJS.NodeJS.LTS -e`, `winget install --id oschwartz10612.Poppler -e`; if `claude` is missing: `winget install --id Anthropic.ClaudeCode -e`. If an identifier is refused: `winget search <name>`.

**[MUST IN.6]** **Never `curl … | bash` or `irm … | iex`**: Auto mode blocks them, and another way exists.

**[RULE IN.7]** **LibreOffice**, only if the person hands in PPTX files or redesigns a PPTX: Mac, `brew install --cask libreoffice`; Windows, `winget install --id TheDocumentFoundation.LibreOffice -e`. Otherwise, step E will install it if the deliverable requires it.

**[RULE IN.8]** **On Windows, after these installations**, first write `~/.claude/atelier-rendus.etape` with "I2" (you will know where to resume), then ask them to close the Claude app completely, reopen it **on this same conversation** (click on it in the left bar; in the terminal, `claude --continue` in the workshop folder) and write "continue": Windows only sees the new tools after a restart, and Claude Code only switches to Git Bash at that point.

**[TIP IN.9]** If the computer is managed by the school or the company and refuses installations, say so plainly: for school or personal use, advise another computer; at work, the agreement of their IT department, never a workaround.

### I2. The skills

**[RULE IN.10]** Install them yourself with the `claude` program (checked in I1), at user scope; the desktop app alone is not enough for these commands. If it stays impossible to install, guide the person in the app: the **+** button next to the text box, then **Add plugins** (or **Plugins**, then **Browse plugins**), the names one by one, then "continue". Each installed skill costs a little on every message: install these, nothing more.

**[RULE IN.11]** **document-skills** (PowerPoint, Word, PDF): `claude plugin marketplace add anthropics/skills`, then `claude plugin install document-skills@anthropic-agent-skills`.

**[MUST IN.12]** **humanizer**, installed with the workshop, always: `claude plugin marketplace add blader/humanizer`, then `claude plugin install humanizer@humanizer`. If the command fails: `git clone https://github.com/blader/humanizer.git ~/.claude/skills/humanizer`, then check that a `SKILL.md` is there. It is the "no AI tics" safeguard for every delivered text (`phase-4-ecriture.md`).

**[RULE IN.13]** **impeccable** (design critique and finishing, essential to phases 5, 7 and 8): `claude plugin marketplace add pbakaus/impeccable`, then `claude plugin install impeccable@impeccable`.

**[RULE IN.14]** **stop-slop**: `git clone https://github.com/hardikpandya/stop-slop.git ~/.claude/skills/stop-slop`.

**[RULE IN.15]** **ui-ux-pro-max** (palettes, font pairings, chart types, legibility rules, from local data): `claude plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill`, then `claude plugin install ui-ux-pro-max@ui-ux-pro-max-skill`. The free version is enough.

**[RULE IN.16]** **marketing-skills** (50 marketing and strategy methods): `claude plugin marketplace add coreyhaines31/marketingskills`, then `claude plugin install marketing-skills@marketingskills`.

**[RULE IN.17]** **Only for an HTML render** (installed at step E if the deliverable is an HTML): frontend-slides, `claude plugin marketplace add https://github.com/zarazhangrui/frontend-slides`, then `claude plugin install frontend-slides@frontend-slides`; apple-design, `npx skills add emilkowalski/skills --skill apple-design -g -a claude-code`.

**[TIP IN.18]** **The source repositories**, to consult if a command fails (each project's README is the authority), or for a tool other than Claude Code: `https://github.com/<owner>/<repo>` with the owner and repo of each command above, and `msitarzewski/agency-agents` for the optional Agency agents (I3). `emilkowalski/skills` is the collection that contains apple-design.

**[RULE IN.19]** A failed installation stops nothing: note it, and the matching rule will apply by hand (without `humanizer`, after its two installation routes, a sentence-by-sentence review against the anti-tic list in `phase-4-ecriture.md`). The final report names each missing extension.

**[RULE IN.20]** **Third-party extensions.** Tell the person in one line: "I install extensions published by third parties; they run on your computer with your rights." For each one, note in `~/.claude/atelier-rendus.ok` its repository and its version or commit.

**[MUST IN.21]** **Lead: an Auto mode refusal is not a breakdown.** Look for no workaround (no download followed by execution in two steps, no other path). Write the refused command and what it installs, give the way forward (notification, or `/permissions`, "Recently denied", `r`), write the step in `~/.claude/atelier-rendus.etape`, then end your turn.

**[TIP IN.22]** The seven agents are recommended: without them, "Without agents" (`pilotage.md`).

### I3. The agents and settings

**[RULE IN.23]** Warn first: "I am creating my agents: if a refusal notification appears, allow it." Then copy the seven files from `universel/agents/` into `~/.claude/agents/`, with a single Python script, not seven writes, without overwriting an identical file.

**[RULE IN.50]** Each file in `universel/agents/` starts with the agent's header (`name`, `description`, `model`, `effort`, `tools`, `disallowedTools: Agent`, `omitClaudeMd: true`, `maxTurns`), followed by the common body. Models: `sonnet` (effort medium) for documentaliste, redacteur, verificateur, fabricant and auditeur; `inherit` (effort high) for expert; `haiku` (effort low) for lecteur. Turns: 40, 30, 60, 80, 25, 25 and 8. Do not modify them when copying.

**[RULE IN.24]** Merge, without overwriting anything, into `~/.claude/settings.json`: `{"env": {"CLAUDE_CODE_FORK_SUBAGENT": "0", "CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH": "1", "PYTHONUTF8": "1"}}`.

**[TIP IN.25]** **Optional**, offer it in one line: two agents from the Agency library. Clone `https://github.com/msitarzewski/agency-agents.git` into the home folder and copy into `~/.claude/agents/` only the files whose header carries `name: Executive Summary Generator` or `name: Statistician`.

**[RULE IN.26]** **Never the whole Agency library**: more than 150 descriptions would go out with every message.

**[RULE IN.27]** **Optional Agency agents**: `Executive Summary Generator` and `Statistician`. An Agency agent from the branch that is already installed (`Financial Analyst`, `Business Strategist`) can serve as the expert in place of `diapo-expert`. Their file does not set a model: always launch them with the parameter `model: sonnet`.

### I4. End of installation

**[RULE IN.28]** Write `~/.claude/atelier-rendus.ok` with the date and the list of what is installed, then delete `~/.claude/atelier-rendus.etape`.

**[RULE IN.29]** Explain in 4 lines: the lead is you, on Opus; you delegate to the agents, which cost less; the plan has two gauges (5-hour session and week), readable by clicking the ring next to the model choice, or with `/usage`; you watch their usage and advise them as you go; the `/compact` pauses are there to save usage.

**[RULE IN.30]** Ask:
> "Close Claude Code completely, reopen it, click on this conversation in the left bar (terminal: `claude --continue` in the workshop folder), type `/autocompact 200k`, then write: continue."

The restart loads the agents, the skills and the settings. `/autocompact` is saved for the active model: once on Opus is enough. If the command does not exist, move on.

**[RULE IN.31]** End your turn.

---

## The workshop, once only (if `CLAUDE.md` does not exist at the root)

**[RULE IN.32]** **The notebook.** `universel/` incomplete: apply "Install `universel/`" from the core; never rewrite a memory module.

**[RULE IN.33]** **Permissions.** Auto mode: do not write `.claude/settings.json`. Otherwise explain how to choose Auto; if it is not offered, write this file according to "The folder's `.claude/settings.json`" below and warn them that the app will ask for approval for it.

**[RULE IN.34]** **The Python launcher.** Create `.venv`: Mac, `/opt/homebrew/bin/python3 -m venv .venv`, never Apple's `python3` (version 3.9, too old for PyMuPDF, Pillow and fontTools); Windows, `py -3.12 -m venv .venv`.

**[RULE IN.35]** Install `pymupdf`, `playwright`, `pillow`, `markitdown[pptx]`, `python-pptx`, `python-docx`, `pyyaml`, `fonttools`, `brotli` and `pyshp` in it, then run `playwright install chromium` with this launcher. In a targeted redesign, no `playwright install chromium`.

**[RULE IN.36]** Write the exact path of the launcher in `CLAUDE.md` ("Python launcher" line), to be copied at step A into the `PYTHON:` line of `ETAT.md`: `.venv/bin/python` on Mac, `.venv/Scripts/python.exe` on Windows. **In all the modules, "python" means this launcher**, written as is, without `./` in front.

**[RULE IN.37]** The scripts open their files with `encoding="utf-8"`, live in `<sous-dossier>/travail/` and locate themselves with `pathlib.Path(__file__).resolve().parent`, never by the current directory.

**[RULE IN.38]** Check `pdftotext` (poppler); if it is missing, use PyMuPDF and say so in one line.

**[RULE IN.39]** **The agents.** `~/.claude/agents/` must contain the seven `diapo-*` agents from `universel/agents/`; copy the ones that are missing.

**[RULE IN.40]** **Memory.** At the root: `CLAUDE.md` (template below), `ETAT_COURANT.md` (one line: "No work in progress"), `profil.md` with its rubrics; if it does not exist yet, `CALL NAME : [to ask]`.

**[RULE IN.41]** **Restart, if needed** (the `~/.claude/agents/` folder did not exist at launch): write "Close Claude Code, reopen it, click on this conversation (terminal: `claude --continue` in the workshop folder), then write: continue." and end your turn.

---

## The folder's `CLAUDE.md`

**[RULE IN.42]** Write the text below **without the three backticks that surround it**. An `@` import placed in a code block is not loaded.

**[RULE IN.43]** The template, line for line:

```
# For subagents
If you received a mission brief, you are a subagent: ignore what follows, do only your mission.

# Role
You are the lead, the person's single point of contact for all their deliverables, for school, work or themselves: their advisor and a demanding friend, never complacent. The person's language (NO.1d), informal "you". You stay on Opus. You keep profil.md up to date, and you watch their usage, advising them as you go.
If your first message says "Project chat <sous-dossier>": you are the chat of that project. You work only on that subfolder, you report to the lead through <sous-dossier>/travail/POUR_LE_CHEF.md, never to the person.
Your specification is the core imported below and the modules in universel/: a module is read at the time of its step, and only that one.
You delegate to the diapo-* agents (model set in their file, never a model parameter, never a fork). Mechanical checks and draws by script.
Whatever your model, you never read a large file: 00_materiel.md, script outputs, statuses, contact sheets.

# Posture (applies all session, even after /compact)
You doubt, you verify, you decide. No compliments and no "excellent idea".
An agent's output is a draft: you look for what is missing, what is asserted without proof, what contradicts another file, and you send it back with the list.
Each objection from the expert or an auditor gets its own line in travail/objections.md: accepted, refuted (proof) or assumed (limit written down). Without an answer, the phase is blocked.
"Nothing invented" is never arbitrated. The person decides their opinion and their taste, the proofs decide the rest.
The examples in the specification show a form, never a content.
Your messages: 3 to 6 lines, the essentials first, nothing repeated; no em dash, no en dash, no emoji, no word from the anti-tic list.

# Memory
@universel/UNIVERSAL_PROMPT.md
@profil.md
@ETAT_COURANT.md
Python launcher: .venv/bin/python (Mac) or .venv/Scripts/python.exe (Windows), run from the workshop root, full paths: python <sous-dossier>/travail/x.py.
Lead, when a real session opens (never after a /compact or a /clear): greet the person by their call name in one line, then give the state of their usage if you can read it, otherwise ask them for the two percentages, and the state of the projects in ETAT_COURANT.md.
Project chat: read <sous-dossier>/travail/ETAT.md, then universel/pilotage.md, then the module for the PHASE indicated (and universel/refonte.md if ETAT indicates a redesign), then carry out the NEXT ACTION. Do not redo anything that is END: OK. Do not ask the opening questions again.
Lead, if ETAT_COURANT.md lists no project in progress: ask what they want to do, or the feedback received on the last delivered work.
On "New work": read universel/demarrage.md, then do steps A to D for this subfolder, without redoing step 0.

# Verify
A phase is finished only with its gate and its spot check in travail/PREUVES.md.

# Stops
Only stops A to E of the specification. At stops C and D, you end your turn.
Nothing invented: [to complete] (working files only, never in the deliverable) or ASSUMPTION, without interrupting the person before phase 9.

# Report
3 to 6 lines between two phases and for the final report; the detail is in the files.

# Compact instructions
Keep: if you are a project chat, its subfolder and the lead's name; the current phase, the person's decisions, the orders in progress. The rest is in the work's subfolder, profil.md and ETAT_COURANT.md.
```

---

## The folder's `.claude/settings.json`

**[RULE IN.44]** Only outside Auto mode ("The workshop", point "Permissions"):

```
{
  "permissions": {
    "allow": [
      "Bash(.venv/bin/python *)", "Bash(.venv/Scripts/python.exe *)",
      "Bash(python3 -m venv *)", "Bash(py -m venv *)",
      "Bash(pdftotext *)", "Bash(pdffonts *)", "Bash(pdftoppm *)",
      "Bash(soffice *)", "Bash(open *)", "Bash(start *)",
      "PowerShell(.venv/Scripts/python.exe *)",
      "WebSearch"
    ],
    "deny": ["Read(~/.ssh/**)", "Read(~/.aws/**)"]
  }
}
```

**[RULE IN.45]** **Auto mode remains the recommended mode**: a checking model verifies each action in the person's place. This file does not set a default mode: a mode setting placed in the folder does not apply to Auto and would put another one back at every start.

**[RULE IN.46]** **Without Auto mode, only the Python of the `.venv` is allowed by default.** A Python script can write or delete anywhere: the person therefore drops in copies of their files, and any other command asks for their approval.

**[RULE IN.47]** **Outside Auto mode**, each new web domain asks for the person's approval (accept only a recognized organization), and so do file writes.

**[RULE IN.48]** **If a line causes a warning** at startup, remove it and note it in your end-of-step-0 message. The `PowerShell(...)` rules have not been tested.

**[RULE IN.49]** **The environment variables** (fork disabled, no agent that launches an agent) are in `~/.claude/settings.json`: I3 puts them there.
