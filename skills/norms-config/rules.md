<!-- kaizen:rules 1.6.1 -->
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
- **Comments** — never comment a workaround or a shortcut's limit, even where another plugin asks for a `shortcut:` comment: fix the root cause or queue the rest, a shortcut's limit with when to upgrade it; comment only a license, an outside constraint, a public API contract or an issue link.
- **Skills, where installed** — load the skill before its work: UI `ui-build` · SQL `db-ops` · query, key or env var `logic-build` · a document `docs-format` · a page or feature `build-flow`.
<!-- /kaizen:rules -->
