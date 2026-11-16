# kaizen docs

`kaizen` is nine standalone skills for building an app with an agent, and eight working rules a repo keeps in its own `CLAUDE.md`. These pages are for the people who install it. What an agent obeys is in `skills/`; nothing here is a rule, and where a page and a skill disagree the skill is right and the page is the defect.

New here: [Overview](start/overview.md), then [Install](start/install.md), then [Quickstart](start/quickstart.md).

## Getting started

| Page | Holds |
|---|---|
| [Overview](start/overview.md) | The parts of the plugin, and what each one does |
| [Install](start/install.md) | What the machine needs, the two commands, the optional design skills |
| [Quickstart](start/quickstart.md) | The first run, on a new app or an existing one |

## Concepts

| Page | Holds |
|---|---|
| [How it works](concepts/how-it-works.md) | What loads when, and what it means that nothing is enforced |
| [Working rules](concepts/working-rules.md) | The eight lines in a repo's `CLAUDE.md`, and how to waive or change one |
| [Documents](concepts/documents.md) | The files an app repo keeps, and what gets each one written |
| [Hosts](concepts/hosts.md) | What differs between Claude Code and Antigravity |

## Guides

| Page | Holds |
|---|---|
| [Start a new app](guide/new-app.md) | From an empty directory to the first page |
| [Bring in an existing app](guide/existing-app.md) | Working rules and documents for an app that already runs |
| [Redesign the look](guide/redesign.md) | One `design-settle` session, then one page per session |
| [Run on a Pro plan](guide/pro-plan.md) | Four settings of your machine that decide what a session costs |
| [Update the plugin](guide/update.md) | Updating, moving to 1.0.0, and the two older moves |
| [Run on Antigravity](guide/antigravity.md) | Install, update, and what is absent there |
| [Maintain app repos](guide/maintain-app-repos.md) | What a repo started under an older version still carries |

## Reference: commands and skills

| Page | Holds |
|---|---|
| [Commands](reference/commands.md) | What to run in which situation |
| [app-settle](reference/app-settle.md) | The interview that writes `CLAUDE.md` and the core documents |
| [design-settle](reference/design-settle.md) | Two frames, `DESIGN.md` and one proving page, in one session |
| [norms-config](reference/norms-config.md) | Writing and refreshing the working rules in a repo |
| [norms-help](reference/norms-help.md) | The card: version, commands, pages, last change |
| [build-flow](reference/build-flow.md) | Building one page at a time, and its three stops |
| [docs-format](reference/docs-format.md) | Which documents a repo keeps, and what stays out of them |
| [ui-build](reference/ui-build.md) | Components, states and on-screen text |
| [db-ops](reference/db-ops.md) | Migrations, destructive operations and the RLS role test |
| [logic-build](reference/logic-build.md) | Keys, business rules, queries and their tests |

## Project

| Page | Holds |
|---|---|
| [What is proven](reference/status.md) | What has run for real, and what has not |
| [Changelog](https://github.com/rapidkaizen-cloud/kaizen/blob/main/CHANGELOG.md) | Every version, newest first |

A feature with no page here has its skill as the only source: `skills/<name>/SKILL.md`.
