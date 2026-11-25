# Commands

Every command `kaizen` gives you, and the skills that load without one.

| Situation | Run |
|---|---|
| A new app, before any code | `/kaizen:app-settle` |
| An app that already runs and has no documents | `/kaizen:app-settle` |
| Settle or change the look of an app | `/kaizen:design-settle` |
| Stop the working rules being printed in one repo | An empty `.kaizen-rules-off` file at its root — see [Rules hook](rules-hook.md) |
| Which version is running, what changed, which page explains a feature | `/kaizen:norms-help` |

Each command stands alone: none requires another, and none starts another when it ends. A session may also load one when you ask in your own words; the command is the sure way.

## No command needed

A session loads these when the work calls for one: the last line of the [working rules](../concepts/working-rules.md) names each, and the skill list carries its description.

| Skill | Loads when a session |
|---|---|
| `build-flow` | builds or continues a feature, a page or a batch of pages |
| `docs-format` | creates or edits `README.md`, `DESIGN.md` or a file under `docs/` |
| `ui-build` | creates or edits a component, a styling value or on-screen text |
| `db-ops` | writes or runs SQL, a migration or an RLS policy |
| `logic-build` | writes a query, an API handler, an environment variable or anything that holds a key |

## Things you never type

`git` commands, SQL and install commands are the session's to run. Where the working rules are in the repo, a session puts a decision to you as options and then runs the command itself. What stays yours is what needs your own hands: a browser login, a dashboard, a key rotation, a payment.
