# Commands

Every command `kaizen` gives you, and the skills that load without one.

| Situation | Run |
|---|---|
| A new app, before any code | `/kaizen:app-settle` |
| An app that already runs and has no documents | `/kaizen:app-settle` |
| Put the working rules into a repo's `CLAUDE.md`, or refresh them after an update | `/kaizen:norms-config` |
| Settle or change the look of an app | `/kaizen:design-settle` |
| Which version is running, what changed, which page explains a feature | `/kaizen:norms-help` |

Each command stands alone: none requires another, and none starts another when it ends. A session may also load one when you ask in your own words; the command is the sure way.

## No command needed

A session loads these by their description when the work calls for one.

| Skill | Loads when a session |
|---|---|
| `build-flow` | builds or continues a feature, a page or a batch of pages |
| `docs-format` | creates or edits `README.md`, `DESIGN.md` or a file under `docs/` |
| `ui-build` | creates or edits a component, a styling value or on-screen text |
| `db-ops` | writes or runs SQL, a migration or an RLS policy |
| `logic-build` | writes a query, an API handler, an environment variable or anything that holds a key |

The last line of the [working rules](../concepts/working-rules.md) names four of them, so a repo that carries the rules points its sessions at them as well.

## Things you never type

`git` commands, SQL and install commands are the session's to run. Where the working rules are in the repo, a session puts a decision to you as options and then runs the command itself. What stays yours is what needs your own hands: a browser login, a dashboard, a key rotation, a payment.
