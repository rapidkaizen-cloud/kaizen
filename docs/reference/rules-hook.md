# Rules hook

Prints the ten working rules into every Claude Code session and subagent, and every conversation of the Antigravity CLI, in every repo on a machine that has the plugin — and, where you set an output folder, the rule for it.

| | |
|---|---|
| Kind | Hook — `SessionStart` (startup, resume, clear, compact), `SubagentStart` and `PostToolUse` on `Write` on Claude Code; `PreInvocation` on Antigravity |
| Prints | `hooks/rules.md`, about 1,900 characters. With `KAIZEN_OUTPUT_DIR` set, `hooks/output.md` after it, about 700 characters |
| Refuses | Nothing. It never holds, asks or blocks, and ends without an error on every path |
| Needs | Node on `PATH`. Without it the hook prints nothing |
| Source | `hooks/claude-code.json` (Claude Code), `hooks.json` (Antigravity), `hooks/rules.js`; self-check `hooks/test_rules.py` |

## When it prints

| It finds | It does |
|---|---|
| Any project, whatever its `AGENTS.md` or `CLAUDE.md` holds | Prints the rules |
| `.kaizen-rules-off` in the project folder or a folder above it | Nothing, the output folder included |
| A subagent starting | The same as for its session |
| An Antigravity conversation | Prints once, before its first model call, as a step that stays in the conversation; never again in that conversation |
| `KAIZEN_OUTPUT_DIR` set | Adds the output folder of this session to what it prints |
| `KAIZEN_OUTPUT_DIR` set, and `Write` creates a file outside that folder | Tells the session the file's path and asks it to move the file there if it was made for you. Claude Code only |

## The output folder

Unset, a session saves its files wherever it likes, and the hook says nothing about them. Set, every file a session makes for you and not for the repo — a report, an export, a one-off script, a log — goes into one folder per place you work:

| The session runs in | Its folder under `KAIZEN_OUTPUT_DIR` |
|---|---|
| A repo's main checkout | `<repo>` |
| A worktree of it, an Orca workspace from the repo included | `<repo>-<worktree>`; a worktree whose name already starts with `<repo>-` keeps it as it is |
| An Orca workspace that is a folder without a repo | The folder's name |
| Anywhere else | `_general` |

Orca is recognized by an environment variable that starts with `ORCA_`.

To turn it on:

1. **Add the variable to the `env` block of `~/.claude/settings.json`**, as `"KAIZEN_OUTPUT_DIR": "<the folder>"`. On Antigravity, set it in the system environment instead.
2. **Start a new session.** A running one keeps what it was given at its start.

To turn it off, delete the variable. In one repo, `.kaizen-rules-off` turns off the output folder with the rules.

If your own `CLAUDE.md`, or a repo's `AGENTS.md` or `CLAUDE.md`, names an output folder too, make it say the same as the table above, or delete it: a session that reads two places picks one.

## Change a rule for one repo

Write the change in that repo's `AGENTS.md`, under `## Rules for this app only`. A session reads it beside the printed rules, and the rules give way to it. Keep the repo's `CLAUDE.md` to `@AGENTS.md` and what Claude Code alone reads: Antigravity never reads `CLAUDE.md`, and Claude Code reads `AGENTS.md` only through that line.

## Turn it off in one repo

1. **Create an empty file named `.kaizen-rules-off` at the repo root.**
2. **Commit it** to turn the hook off for everyone on the repo, or add it to `.gitignore` to turn it off on your machine only.

Delete the file to turn the hook back on. A session that is already running keeps what it was given at its start.

## What it does not cover

- **A machine without the plugin.** The rules live in the plugin, not in the repo: a teammate gets them by installing `kaizen`.
- **Antigravity outside the CLI.** Reports say the IDE and the desktop app run no hook. See [Hosts](../concepts/hosts.md).
- **Enforcement.** The rules reach the session as text. A session that skips one is stopped by nothing.
- **Files a script writes.** The hook sees only `Write`, and only after the file exists: a file a shell command saves elsewhere is kept in place by the rule's text alone.
- **New files in the project, the temp folder and `~/.claude`**, and files that already existed. The hook cannot tell a repo's file from one made for you, so it says nothing about them.
- **A move in the middle of a session.** The folder is worked out when the session starts; entering a worktree later does not change it.
- **Two repos with the same folder name.** They share one output folder.

## Related

- [Working rules](../concepts/working-rules.md) — the ten lines, and how to waive or change one.
- [How it works](../concepts/how-it-works.md) — what loads when.
