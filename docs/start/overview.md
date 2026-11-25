# Overview

`kaizen` is one plugin of eight standalone skills for building an app with an agent, plus ten working rules every Claude Code session gets.

Nothing in it is enforced. A skill is text a session reads when the work calls for it, and a working rule is a line you can waive in chat. The plugin's one hook prints the working rules and refuses nothing.

## The parts

| Part | What it does | When it runs |
|---|---|---|
| `app-settle` | Interviews you about the problem, the roles and the business rules, then writes the repo's `CLAUDE.md` and its core documents | When you invoke it |
| `design-settle` | Settles the look: two direction frames you pick from on screen, then `DESIGN.md` and one proving page | When you invoke it |
| `build-flow`, `docs-format`, `ui-build`, `db-ops`, `logic-build` | Carry the rules for building a page, a document, UI, SQL and application logic | By themselves, when the work matches the working rules' last line or their description |
| Rules hook | Prints the ten working rules into each session and subagent | When one starts, in every repo |
| `norms-help` | Prints the commands, these pages, the version and its last change | When you ask |

## Every skill stands alone

No skill requires another, and none starts another when it ends. Each one reads `CLAUDE.md`, `docs/` and `DESIGN.md` where the repo has them, and runs where it does not. Which skill to run, and in which order, is yours to choose; [Quickstart](quickstart.md) gives an order that suits a new app.

## What it adds to a session

Each skill is one file, read only when it loads; the eight together are under 40,000 characters. When a session or subagent starts, the [hook](../reference/rules-hook.md) prints the working rules, about 1,700 characters. A session meets the rest through the skill list.

## Next

- [Install](install.md) — the two commands and the optional design skills.
- [Quickstart](quickstart.md) — the first run on a new app or an existing one.
- [Commands](../reference/commands.md) — what to run in which situation.
