# app-settle

A short interview about what an app is, then the repo's `CLAUDE.md` and its core documents.

| | |
|---|---|
| Kind | Skill — runs only when you ask |
| Run | `/kaizen:app-settle` |
| Reads | The repo root, `CLAUDE.md`, `README.md`, everything under `docs/`, the stack's manifest |
| Writes | `CLAUDE.md`, `README.md`, and under `docs/`: `README.md`, `product.md`, `rules.md`, `changelog.md`, and `queue.md` on a new app |
| Commits | Once, at the close. Never pushes |
| Source | `skills/app-settle/SKILL.md` |

## Two modes

| The repo holds | Mode | What happens |
|---|---|---|
| No app code | `Bootstrap` | The interview, one round about the stack, the documents, and `git init` where there is no repo |
| An app | `Document` | The interview, the stack recorded as found, the documents. Nothing about the app changes |

The session names the mode in the block it prints first.

## What happens

1. **The block**: the mode, the stack as found, the documents found, whether `CLAUDE.md` exists.
2. **Your story.** One open invitation, then the session's reading in one paragraph.
3. **Six themes**: the problem · who uses the app and how they work today · what each role must finish, and its limits · the business rules and the reason behind each number · the terms easy to misread · what the app is not for. Each is summarized back, and its gaps are asked in one batch.
4. **The stack.** On a new app, one round: platform, frontend, database with auth, hosting — each with a recommendation, its trade-off and `decide for me`. On an existing app, nothing is asked.
5. **The summary**: each file and what it will hold.
6. **The files**, then one commit and a report.

## Where it stops

- **After its reading of your story**, for your correction.
- **At the summary**, for an explicit yes. Nothing is written, installed or generated before it.

## What you can rely on

- **Nothing is invented.** An answer nobody gave is written `[needs verification]`, and the report lists each one.
- **No secret is written and no token is asked for.** An environment variable appears by its name.
- **A file that exists gets only what it lacks**, and no line of it is rewritten without your word.
- **`CLAUDE.md` is in English; the documents are in your language.**
- **The reason behind a number is always asked.** "It has always been that way" is written as said.

## What it does not cover

- **A scaffold.** It writes documents, never code; the app's code starts with the first build session.
- **`DESIGN.md`.** That is [design-settle](design-settle.md).
- **The working rules.** That is [norms-config](norms-config.md); a block already in `CLAUDE.md` is left as it is.
- **An audit, or a migration of documents from an older version.** See [Maintain app repos](../guide/maintain-app-repos.md).
- **Every choice beyond the four of the stack round.** A cache, a validator, a date library: each is asked by the session that first needs it.

## Related

- [Start a new app](../guide/new-app.md)
- [Bring in an existing app](../guide/existing-app.md)
- [Documents](../concepts/documents.md)
