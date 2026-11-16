# Working rules

Eight lines of text in a repo's `CLAUDE.md` tell every session there how to work, and each one holds until you waive it in chat.

## Where they live

`/kaizn:norms-config` writes them at the end of the `CLAUDE.md` at the repo root, as one block between two markers:

```
<!-- kaizn:rules 1.0.0 -->
## Working rules
...
<!-- /kaizn:rules -->
```

The host reads `CLAUDE.md` when a session starts, so the rules reach every session in that repo. They travel with the repo: a teammate's session reads them whether or not that machine has the plugin. The number in the opening marker is the plugin version the block last changed in.

## The eight lines

| Line | What you will see a session do |
|---|---|
| `Scope` | Only what you asked: no refactor, rename or document outside it |
| `Language` | Chat, documents and on-screen text in your language; identifiers, file names, routes and database names in English |
| `Git` | Commit a finished item in the same turn, naming its files. Push, merge, force-push or rewrite history only on your word |
| `Data` | Before a statement that drops, deletes, truncates, renames or broadly updates: count the rows, show the number, wait for your yes |
| `Secrets` | Name a variable, never write its value |
| `Asking` | Put a decision to you as options with one recommendation and its trade-off, and run the command itself |
| `Closing` | Report per item what changed, each default it chose, and what you must do by hand |
| `Skills, where installed` | Read the `kaizn` skill for UI, SQL, logic or a document before that kind of work |

The exact text is in `skills/norms-config/SKILL.md`.

## Nothing enforces them

A session that skips a line is stopped by nothing. `Git` and `Data` are the two that matter for an app in production: see [How it works](how-it-works.md) for the protections worth keeping beside them.

## Waive or change a line

- **For one session**, say so in chat: "push without asking in this session".
- **For good**, edit the line in `CLAUDE.md`, or delete it. The next `/kaizn:norms-config` shows the lines that differ from the plugin's and asks which to keep; it never puts back a line you removed without your answer.

## After a plugin update

A version that changes the block says so in its changelog entry. Run `/kaizn:norms-config` again in each repo.

> [!WARNING]
> A block with an older version in its marker is replaced whole, your edits inside it included. Keep rules of your own outside the markers — under `## Rules for this app only`, the section `app-settle` writes for them.

## `AGENTS.md`

A repo with an `AGENTS.md` at its root gets the same block there, by the same steps. `norms-config` never creates that file.

## The output line

Name a folder when you run `norms-config` — "files for me go to `~/reports`" — and the block gets one more line that sends the files a session makes for you there, out of the repo. No folder is asked for, and none is assumed.

## Related

- [norms-config](../reference/norms-config.md) — what the command finds and what it does.
- [Maintain app repos](../guide/maintain-app-repos.md) — what a repo from an older version still carries.
