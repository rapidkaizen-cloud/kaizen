# Changelog

All notable changes to the `kaizen` plugin, newest first. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions before 1.0.0 are in `git log`.

## [kaizen 1.2.0] - 2026-11-16

The plugin, its marketplace and its repo are renamed `kaizen`, because the earlier spelling read as a typo. Other Claude Code plugins named `kaizen` exist; installing one of them beside this one puts two plugins under one name.

### Changed

- The plugin and its marketplace are named `kaizen`: every skill is `/kaizen:<skill>`, and the install is `/plugin install kaizen@kaizen`.
- The repo moves to `rapidkaizen-cloud/kaizen`, where GitHub redirects the old URL, and the docs site to `https://rapidkaizen-cloud.github.io/kaizen/`, where the old address does not redirect.
- The working-rules block sits between `<!-- kaizen:rules 1.2.0 -->` and `<!-- /kaizen:rules -->`.
- `norms-help` opens its card with `kaizen <version>`.

### Removed

- The `renames` map in `marketplace.json`: an update in place no longer carries an earlier plugin name to `kaizen`.
- The changelog entries before 1.0.0; they stay in `git log`.

To act on:

- Claude Code: remove the old marketplace, add `rapidkaizen-cloud/kaizen`, install `kaizen@kaizen`, and turn `autoUpdate` on for `kaizen` — the steps are in `docs/guide/update.md`. An update in place does not move the plugin: its old key names a plugin the marketplace no longer has.
- Every app repo whose `.claude/settings.json` names the old plugin key: change it to `kaizen@kaizen` and commit it.
- Antigravity: uninstall the old copy, then install from `https://github.com/rapidkaizen-cloud/kaizen`.
- Anything written outside the plugin that invokes a skill — notes, aliases, scripts — changes its prefix to `/kaizen:`.
- A bookmark of the docs site moves to `https://rapidkaizen-cloud.github.io/kaizen/`.

## [kaizen 1.1.0] - 2026-11-16

The plugin ships no hook. The context reminder's note made a session end its turn at 200k, 500k and 800k tokens, and that interrupted the work more than it saved.

### Removed

- The context reminder: `scripts/remind_context.py`, its self-check, `hooks/hooks.json` and the page `docs/reference/context-reminder.md`. Nothing tells a session its context passed a milestone: watch the size with `/context` and the quota with `/usage`.

## [kaizen 1.0.0] - 2026-11-16

Every skill was rewritten to stand alone and to be short, and every guard was removed. The steps of the old skills drove a session's context to 300k–860k tokens, and one redesign took 8 windows of a Pro plan; and a hook cannot ask — it refuses, the case that should have passed included. The plugin is now nine skills of one file each, about 36,000 characters where it was 428,000 in 55 files, and one hook that only hands the session a note. Rules are text in the app repo's own `CLAUDE.md`, and you can waive any of them in chat.

### Added

- `norms-config` writes a block of eight working rules — scope, language, git, data, secrets, asking, closing, and which skill covers which work — into the repo's `CLAUDE.md`, between `<!-- kaizen:rules 1.0.0 -->` and `<!-- /kaizen:rules -->`, and into `AGENTS.md` where the repo has one. An older block is replaced whole; an edited block of the same version is shown and asked about. A folder you name for your files becomes one `Output` line.
- `logic-build`: a need with no recorded choice is asked once, with a recommendation, and recorded as a row of the Stack table in `CLAUDE.md`.
- `docs/concepts/working-rules.md`.

### Changed

- Every skill is one `SKILL.md` with no `references/` folder, requires no other skill, and runs where a document it reads is absent.
- `app-settle` has two modes, `Bootstrap` and `Document`: one interview of six themes, one round about the stack on a new app, then `CLAUDE.md`, `README.md`, `docs/README.md`, `docs/product.md`, `docs/rules.md`, `docs/changelog.md`, and `docs/queue.md` on a new app. It writes documents only.
- `design-settle` is one session: a reading, one round of questions, two frames, `DESIGN.md`, one proving page, one run of `verify_pages.js`, one commit.
- `impeccable`, `frontend-design` and `ui-ux-pro-max` are optional: read where installed, never asked for.
- `docs-format`: the documents are `README.md`, `DESIGN.md`, and under `docs/` `README.md`, `product.md`, `rules.md`, `queue.md`, `changelog.md`. A file of another kind already in `docs/` — `PRD.md`, `glossary.md`, `architecture.md`, `runbook.md`, a help page — stays and is kept true; none is written unless asked.
- The context reminder no longer holds a message: it hands the session one note at 200k, 500k and 800k tokens and is silent otherwise. It has no switch and ships on Claude Code only.
- `norms-config` no longer sets switches or an output folder: it writes the working rules.

### Removed

- Every guard: `guard_git`, `guard_destructive`, `guard_output`. Nothing holds a push, a merge, a destructive SQL statement or a file written outside the output folder.
- The `SessionStart` hook and the session norms it printed, with the `NOT SETTLED` and `HOST` blocks; the document reminder; the hand-over from another host's session.
- Switches: `switches.json`, the marker `onboarded-output`, `.claude/destructive-gate.off`, and the output folder the plugin printed.
- Skill `logic-settle`.
- `app-settle`: the modes `migrate`, `align` and `rework`, the `seed` repair, the audit, and the scaffold — Bootstrap writes documents and runs `git init`; the app's code starts with the first build session.
- `design-settle`: the audit and its scope, the `Fast` and `Full` modes, the canvas rounds, the checks in subagents; `scripts/audit_count.py`.
- `build-flow`: the Playwright spec per page, the external-writer rules, the account question before a walk.
- The lint floors and rule-test set-up a skill wrote.
- The root `hooks.json`: no hook ships on Antigravity.
- The pages of all of the above under `docs/`: `concepts/gates.md`, `concepts/session-norms.md`, `reference/guard-git.md`, `guard-destructive.md`, `guard-output.md`, `document-reminder.md`, `session-start.md`, `logic-settle.md`.

To act on:

- Run `/kaizen:norms-config` once in each app repo: the norms are no longer handed to a session at its start, and until then a session there follows none of them.
- Nothing holds a push, a merge or a destructive statement any more: turn on branch protection, keep database backups, and give sessions a database login that is not the owner.
- `switches.json` and the marker `onboarded-output` in the plugin's data folder, and `.claude/destructive-gate.off` in a repo, are read by nothing; delete them or leave them.
- The output folder is no longer printed or guarded: name it when you run `norms-config`, and it becomes a line of the block.
- `/kaizen:logic-settle` and `app-settle`'s modes `migrate`, `align`, `rework` and `seed` are gone, with nothing in their place.
- Lint floors and rule tests already in a repo stay as that repo's own configuration; no skill maintains them.
- `docs/PRD.md` no longer marks a repo as settled, and a root `PRD.md` is read as it is.
