# app-settle

A short interview about what an app is, then the repo's `AGENTS.md` and its core documents.

| | |
|---|---|
| Kind | Skill — runs only when you ask |
| Run | `/kaizen:app-settle` |
| Reads | The repo root, `AGENTS.md`, `CLAUDE.md`, `README.md`, everything under `docs/`, the stack's manifest |
| Writes | `AGENTS.md`, `CLAUDE.md`, `README.md`, and under `docs/`: `README.md`, `product.md`, `rules.md`, `changelog.md`, and `queue.md` on a new app |
| Commits | Once, at the close. Never pushes |
| Source | `skills/app-settle/SKILL.md` |

## Two modes

| The repo holds | Mode | What happens |
|---|---|---|
| No app code | `Bootstrap` | The interview, one round about the stack, the documents, and `git init` where there is no repo |
| An app | `Document` | The interview, the stack recorded as found, the documents. Nothing about the app changes |

The session names the mode in the block it prints first.

## What happens

1. **The block**: the mode, the stack as found, the documents found, whether `AGENTS.md` exists, and what `CLAUDE.md` holds.
2. **Your story.** One open invitation, then the session's reading in one paragraph.
3. **Six themes**: the problem · who uses the app and how they work today · what each role must finish, and its limits · the business rules and the reason behind each number · the terms easy to misread · what the app is not for. Each is summarized back, and its gaps are asked in one batch.
4. **The stack.** On a new app, one round: platform, frontend, database with auth, hosting — each with a recommendation, its trade-off and `decide for me`. On an existing app, nothing is asked.
5. **The summary**: each file and what it will hold, and each line moving from `CLAUDE.md` to `AGENTS.md`.
6. **The files**, then one commit and a report. On an existing app, `docs/product.md` gets a features table: one row per feature the app's routes or menu show, with how a user reaches it, how a walk drives it, and what proves it worked. On a new app the table starts with the first page built.

## Where it stops

- **After its reading of your story**, for your correction.
- **At the summary**, for an explicit yes. Nothing is written, installed or generated before it.

## What you can rely on

- **Nothing is invented.** An answer nobody gave is written `[needs verification]`, and the report lists each one.
- **No secret is written and no token is asked for.** An environment variable appears by its name.
- **A file that exists gets only what it lacks**, and no line of it is rewritten without your word.
- **One file for the app's own rules.** `AGENTS.md` holds them, so every agent reads the same lines. `CLAUDE.md` holds `@AGENTS.md` and only what Claude Code alone reads. In a repo whose `CLAUDE.md` holds rules of its own, they move into `AGENTS.md`, and where two lines contradict you are asked which holds. A `CLAUDE.md` that is a symlink becomes a plain file.
- **`AGENTS.md` and `CLAUDE.md` are in English; the documents are in your language.**
- **The reason behind a number is always asked.** "It has always been that way" is written as said.

## What it does not cover

- **A scaffold.** It writes documents, never code; the app's code starts with the first build session.
- **`DESIGN.md`.** That is [design-settle](design-settle.md).
- **The working rules.** The plugin's [hook](rules-hook.md) prints them; `app-settle` writes none into `AGENTS.md`.
- **An audit, or a migration of documents from an older version** beyond moving `CLAUDE.md` into `AGENTS.md`. See [Maintain app repos](../guide/maintain-app-repos.md).
- **Every choice beyond the four of the stack round.** A cache, a validator, a date library: each is asked by the session that first needs it.

## Related

- [Start a new app](../guide/new-app.md)
- [Bring in an existing app](../guide/existing-app.md)
- [Documents](../concepts/documents.md)
