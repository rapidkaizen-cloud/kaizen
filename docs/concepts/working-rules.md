# Working rules

Ten lines of text in a repo's `CLAUDE.md` tell every session there how to work, and each one holds until you waive it in chat.

## Where they live

`/kaizen:norms-config` writes them at the end of the `CLAUDE.md` at the repo root, as one block between two markers:

```
<!-- kaizen:rules 1.3.0 -->
## Working rules
...
<!-- /kaizen:rules -->
```

The host reads `CLAUDE.md` when a session starts, so the rules reach every session in that repo. They travel with the repo: a teammate's session reads them whether or not that machine has the plugin. The number in the opening marker is the plugin version the block last changed in.

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
| `Comments` | No comment that excuses a workaround: the root cause is fixed, or the rest is queued as owed work |
| `Skills, where installed` | Read the `kaizen` skill for UI, SQL, logic or a document before that kind of work |

The exact text is in `skills/norms-config/SKILL.md`.

## Nothing enforces them

A session that skips a line is stopped by nothing. `Git` and `Data` are the two that matter for an app in production: see [How it works](how-it-works.md) for the protections worth keeping beside them.

## Waive or change a line

- **For one session**, say so in chat: "push without asking in this session".
- **For good**, edit the line in `CLAUDE.md`, or delete it. The next `/kaizen:norms-config` shows the lines that differ from the plugin's and asks which to keep; it never puts back a line you removed without your answer.

## After a plugin update

A version that changes the block says so in its changelog entry. Run `/kaizen:norms-config` again in each repo.

> [!WARNING]
> A block with an older version in its marker is replaced whole, your edits inside it included. Keep rules of your own outside the markers — under `## Rules for this app only`, the section `app-settle` writes for them.

## Corrections become checks

A rule an agent reads loses to the code it copies, so a correction you make is worth more as a check than as a line of text. After fixing what you corrected, a session offers to make the mistake impossible, trying in this order:

1. **The code's structure** — one owner for a piece of state, one way to do a task.
2. **A type** that cannot hold the wrong value.
3. **A lint** whose error names the file, type or function to use instead.
4. **A test.**
5. **Prose**, only for a judgment call nothing can check.

A new check is shown failing on the old mistake before it is kept. Where the pattern is already common, it fails only on new additions, and the old copies become a queue line to clean later. An exception sits on its own line with a reason, an expiry date and your yes.

Each rule and what enforces it is a row of a `| Rule | Enforced by |` table under `## Rules for this app only` in `CLAUDE.md`, outside the markers, so a refresh of the block never removes it. A rule kept only as prose and broken again moves up a level in the same change; a rule leaves the table once its mistake cannot happen.

Nothing is preset: a repo gets a check only from a correction you made in it.

## Comments

A comment that explains why a workaround is fine is read by the next session as permission to copy it. A session fixes the root cause, or lands the smallest fix and queues the rest, a shortcut's known limit included. Comments that stay: a license header, behavior forced by a dependency, vendor or protocol outside the repo, a public API's contract, an issue or RFC link.

## `AGENTS.md`

A repo with an `AGENTS.md` at its root gets the same block there, by the same steps. `norms-config` never creates that file.

## The output line

Name a folder when you run `norms-config` — "files for me go to `~/reports`" — and the block gets one more line that sends the files a session makes for you there, out of the repo. No folder is asked for, and none is assumed.

## Related

- [norms-config](../reference/norms-config.md) — what the command finds and what it does.
- [Maintain app repos](../guide/maintain-app-repos.md) — what a repo from an older version still carries.
