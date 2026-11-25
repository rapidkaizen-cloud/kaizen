# Rules hook

Prints the ten working rules into every Claude Code session and subagent whose repo has no block of its own.

| | |
|---|---|
| Kind | Hook — `SessionStart` (startup, resume, clear, compact) and `SubagentStart` |
| Prints | The block in `skills/norms-config/rules.md`, about 1,700 characters |
| Refuses | Nothing. It never holds, asks or blocks, and ends without an error on every path |
| Needs | Node on `PATH`. Without it the hook prints nothing |
| Source | `hooks/hooks.json`, `hooks/rules.js`; self-check `hooks/test_rules.py` |

## When it prints

| It finds | It does |
|---|---|
| No `CLAUDE.md`, or one with no block | Prints the plugin's block |
| A `CLAUDE.md` holding a block, in the project folder or a folder above it | Nothing: the repo's block wins, whatever its version |
| `.kaizen-rules-off` in the project folder or a folder above it | Nothing |
| A subagent starting | The same as for its session |

A block counts only where its opening marker starts a line, so the marker quoted in a sentence does not silence the hook.

## Turn it off in one repo

1. **Create an empty file named `.kaizen-rules-off` at the repo root.**
2. **Commit it** to turn the hook off for everyone on the repo, or add it to `.gitignore` to turn it off on your machine only.

Delete the file to turn the hook back on. A session that is already running keeps what it was given at its start.

## Keep a repo's own rules

Run [`/kaizen:norms-config`](norms-config.md) in the repo. The block it writes into `CLAUDE.md` is then what every session reads, on machines with or without the plugin, and the hook stays silent there.

A line you reword or delete in that block stays as you left it. After an update that changes the block, the repo keeps its older one until you run `norms-config` again; delete the block to go back to the plugin's.

## What it does not cover

- **Antigravity.** The hook is written for Claude Code only. See [Hosts](../concepts/hosts.md).
- **Enforcement.** The rules reach the session as text. A session that skips one is stopped by nothing.

## Related

- [Working rules](../concepts/working-rules.md) — the ten lines, and how to waive or change one.
- [How it works](../concepts/how-it-works.md) — what loads when.
