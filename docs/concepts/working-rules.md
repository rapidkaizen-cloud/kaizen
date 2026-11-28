# Working rules

Ten lines of text tell every session how to work, and each one holds until you waive it, in chat or in the repo's `AGENTS.md`.

## Where they come from

The plugin's [hook](../reference/rules-hook.md) prints them into every Claude Code session and subagent, and every conversation of the Antigravity CLI, in every repo on a machine that has the plugin. A repo keeps no copy: its `AGENTS.md` holds only what is true of that app, its own rules included, and its `CLAUDE.md` holds `@AGENTS.md` and what Claude Code alone reads. The exact text is in `hooks/rules.md`.

## The ten lines

| Line | What you will see a session do |
|---|---|
| `Scope` | Only what you asked: no refactor, rename or document outside it |
| `Language` | Chat, documents and on-screen text in your language; identifiers, file names, routes and database names in English |
| `Git` | Commit a finished item in the same turn, naming its files. Push, merge, force-push or rewrite history only on your word |
| `Data` | Before a statement that drops, deletes, truncates, renames or broadly updates: count the rows, show the number, wait for your yes |
| `Secrets` | Name a variable, never write its value |
| `Asking` | Put a decision to you as options with one recommendation and its trade-off, and run the command itself |
| `Closing` | Report per item what changed, each default it chose, and what you must do by hand |
| `Corrections` | After fixing a mistake you corrected, offer to make it impossible: in the code's structure, a type, a lint, a test, and prose only last |
| `Comments` | No comment that excuses a workaround or states a shortcut's limit, a `shortcut:` comment included: the root cause is fixed, or the rest is queued as owed work |
| `Skills` | Load the `kaizen` skill for UI, SQL, logic, a document or a page before that kind of work |

## Nothing enforces them

A session that skips a line is stopped by nothing. `Git` and `Data` are the two that matter for an app in production: see [How it works](how-it-works.md) for the protections worth keeping beside them.

## Waive or change a line

- **For one session**, say so in chat: "push without asking in this session".
- **For one repo, for good**, write it in that repo's `AGENTS.md`, under `## Rules for this app only`: "In this repo, push without asking." A session reads that file beside the rules, and the rules give way to it.
- **All ten, in one repo**: an empty `.kaizen-rules-off` at its root. See [Rules hook](../reference/rules-hook.md#turn-it-off-in-one-repo).

## After a plugin update

A version that changes the rules says so in its changelog entry, and the next session gets them. Nothing is run in a repo.

## Corrections become checks

A rule an agent reads loses to the code it copies, so a correction you make is worth more as a check than as a line of text. After fixing what you corrected, a session offers to make the mistake impossible, trying in this order:

1. **The code's structure** — one owner for a piece of state, one way to do a task.
2. **A type** that cannot hold the wrong value.
3. **A lint** whose error names the file, type or function to use instead.
4. **A test.**
5. **Prose**, only for a judgment call nothing can check.

Each rule and what enforces it is a row of a `| Rule | Enforced by |` table under `## Rules for this app only` in `AGENTS.md`. How a check is kept — where the table sits, the proof, the exception, when a row leaves — is in [logic-build](../reference/logic-build.md#checks-from-corrections).

Nothing is preset: a repo gets a check only from a correction you made in it.

## Comments

A comment that explains why a workaround is fine is read by the next session as permission to copy it. A session fixes the root cause, or queues the rest as owed work. A shortcut's known limit is queued too, with when to upgrade it, never left as a comment, even where another plugin asks for a `shortcut:` comment. The queue is where the next piece of work is picked from, so the limit gets fixed instead of waiting for someone to search the code. Comments that stay: a license, a constraint from outside the repo, a public API's contract, an issue link.

## The output folder

Set `KAIZEN_OUTPUT_DIR` and the hook adds one more rule: every file a session makes for you and not for the repo goes into a folder of its own under it — `<repo>` in a main checkout, `<repo>-<worktree>` in a worktree, the folder's name in an Orca workspace without a repo, `_general` anywhere else. A script is given the full path and stops when it is empty, and the session checks the file landed there. Leave the variable unset and nothing is said about where files go. How to set it is in [Rules hook](../reference/rules-hook.md#the-output-folder).

## Related

- [Rules hook](../reference/rules-hook.md) — what prints the rules, and how to turn it off in one repo.
- [Maintain app repos](../guide/maintain-app-repos.md) — what a repo from an older version still carries.
