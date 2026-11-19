---
name: norms-config
description: Writes or refreshes the kaizen working-rules block in this repo's `CLAUDE.md` — ten short rules on scope, language, git, data, secrets, asking, closing, corrections and comments, each one negotiable in chat. Use when the user asks to set up, install, refresh or change the working rules of a repo, or after a plugin update changed the block.
---

# norms-config — the working-rules block

Write the block below into the `CLAUDE.md` at the repo root. The rules are text: nothing enforces them, and the user may waive or reword any line.

1. **Read `CLAUDE.md`.** Absent → create it holding only the block.
2. **No block yet → append it at the end of the file.** A block is everything from `<!-- kaizen:rules` to `<!-- /kaizen:rules -->`.
3. **A block with an older version in its opening marker → replace it, markers included, and nothing outside it.**
4. **A block with this version that differs from the text below → the user edited it.** Show the lines that differ and ask which to keep before writing; never restore a line the user removed without that answer.
5. **`AGENTS.md` exists at the root → write the same block there by the same steps.** Never create `AGENTS.md`.
6. **The user names a folder for the files made for them → add one line to the block**: ``- **Output** — a file made for the user to open goes to `<folder>`, never into the repo.`` Never ask for a folder, and never add the line without one.
7. **Add nothing else to the block**: no key, no token, no URL that carries a credential.
8. **Commit the files written, naming their paths**, then report which files changed and which lines the user kept.

Copy the block exactly, the version in its marker included — it names the plugin version the block last changed in.

```markdown
<!-- kaizen:rules 1.4.0 -->
## Working rules

Each line holds until the user waives it in chat.

- **Scope** — do only what was asked: no refactor, rename or document outside it.
- **Language** — chat, docs and on-screen text in the user's language; identifiers, file names, routes and every database name in English.
- **Git** — commit a finished item in the same turn, naming its paths in `git add` and in `git commit -- <paths>`. Push, merge, force-push and history rewrite only on the user's word.
- **Data** — before `DROP`, `DELETE`, `TRUNCATE`, a rename, or an `UPDATE` with no narrow `WHERE`: count the rows, show the number, wait for a yes.
- **Secrets** — name the variable, never its value, in code, docs, commits and chat.
- **Asking** — put a decision as options with one recommendation and its trade-off; never hand the user a command to type.
- **Closing** — report per item what changed or `UNTOUCHED`, each default you chose, and what the user must do by hand.
- **Corrections** — fix what the user corrected, then offer to make it impossible at the highest level that holds — code, type, lint naming the replacement, test, prose last — and pair it with its enforcer in the `| Rule | Enforced by |` table outside this block.
- **Comments** — never comment a workaround or a shortcut's limit: fix the root cause or queue the rest; comment only a license, an outside constraint, a public API contract or an issue link.
- **Skills, where installed** — UI: `ui-build` · SQL: `db-ops` · query, key or env var: `logic-build` · a document: `docs-format`.
<!-- /kaizen:rules -->
```
