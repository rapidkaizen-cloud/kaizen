# Rules hook

Prints the ten working rules into every Claude Code session and subagent, in every repo on a machine that has the plugin.

| | |
|---|---|
| Kind | Hook — `SessionStart` (startup, resume, clear, compact) and `SubagentStart` |
| Prints | `hooks/rules.md`, about 1,700 characters |
| Refuses | Nothing. It never holds, asks or blocks, and ends without an error on every path |
| Needs | Node on `PATH`. Without it the hook prints nothing |
| Source | `hooks/hooks.json`, `hooks/rules.js`; self-check `hooks/test_rules.py` |

## When it prints

| It finds | It does |
|---|---|
| Any project, whatever its `CLAUDE.md` holds | Prints the rules |
| `.kaizen-rules-off` in the project folder or a folder above it | Nothing |
| A subagent starting | The same as for its session |

## Change a rule for one repo

Write the change in that repo's `CLAUDE.md`, under `## Rules for this app only`. A session reads it beside the printed rules, and the rules give way to it.

## Turn it off in one repo

1. **Create an empty file named `.kaizen-rules-off` at the repo root.**
2. **Commit it** to turn the hook off for everyone on the repo, or add it to `.gitignore` to turn it off on your machine only.

Delete the file to turn the hook back on. A session that is already running keeps what it was given at its start.

## What it does not cover

- **A machine without the plugin.** The rules live in the plugin, not in the repo: a teammate gets them by installing `kaizen`.
- **Antigravity.** The hook is written for Claude Code only. See [Hosts](../concepts/hosts.md).
- **Enforcement.** The rules reach the session as text. A session that skips one is stopped by nothing.

## Related

- [Working rules](../concepts/working-rules.md) — the ten lines, and how to waive or change one.
- [How it works](../concepts/how-it-works.md) — what loads when.
