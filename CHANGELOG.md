# Changelog

All notable changes to the `kaizen` plugin, newest first. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions before 1.0.0 are in `git log`.

## [kaizen 2.3.0] - 2026-11-26

Performance rules in three skills, on the maintainer's direct word, so an app built under them stays fast as its tables grow, on any stack. Written in this toolkit's own words from four published catalogs; none of them is installed or required.

### Added

- `db-ops`: an index for every column a query filters, joins or sorts on, in the same migration, with a catalog test that fails on an unindexed foreign key; indexed RLS columns and a per-user function called once per query; a sequential key and a retention decision for a table that will grow large.
- `logic-build`: a `Performance` section — no query or outside call inside a loop, guarded by the stack's lazy-load guard, a lint rule or a query-count test; only the columns and rows the screen uses; each read once per request; independent calls in parallel; slow work in a background job; clients created once per process; capped retries with backoff; a slow page measured before and after its fix. Upload caps under server handlers. The description now names fixing a slow page.
- `ui-build`: a `Performance` section — lazy routes and libraries, a bundle size budget that fails the build, asked once and recorded in the Stack table; images at their displayed size; long lists paginated or virtualized; every interval, listener and poll stopped on unmount.

### Changed

- `logic-build`: a write of several statements runs in a short transaction with no outside call inside it; paging past an API's row cap joins the line on reading only what the screen uses; the section `Errors and reads` is now `Errors`.
- `ui-build`: a loading skeleton takes the result's size as well as its shape.

To act on:

- Nothing by hand. A session adds the index test and the query guard where an app has none, and asks for the bundle budget once.

## [kaizen 2.2.0] - 2026-11-26

An output folder per repo, worktree and workspace, on the maintainer's direct word, after a script with an empty target path left four files at a drive root.

### Added

- `KAIZEN_OUTPUT_DIR`: when set, the hook prints `hooks/output.md` after the working rules, naming this session's own folder under it — `<repo>` in a main checkout, `<repo>-<worktree>` in a worktree, the folder's name in an Orca workspace without a repo, `_general` elsewhere. Files made for the user go there; a script stops when its output path is empty, and the session checks where the file landed. Unset, nothing is printed and nothing is said.
- A `PostToolUse` hook on `Write`: with `KAIZEN_OUTPUT_DIR` set, a new file written outside the session's folder, the project, the temp folder and `~/.claude` draws a note naming it. It refuses nothing. Claude Code only.

To act on:

- To use the output folder, set `KAIZEN_OUTPUT_DIR` in the `env` block of `~/.claude/settings.json`, or in the system environment for Antigravity, then start a new session; Antigravity also needs the plugin installed again.
- A line in your `CLAUDE.md` or a repo's that sends files to `<output>\<topic>\`: delete it, or make it name the same folders as the hook.

## [kaizen 2.1.0] - 2026-11-25

The working rules reach Antigravity again, on the maintainer's direct word: the same `hooks/rules.js` runs there as a `PreInvocation` hook.

### Added

- `hooks.json` at the repo root, read by Antigravity: before the first model call of a conversation, `hooks/rules.js` injects `hooks/rules.md` as a step that stays in it, once per conversation, and stays silent under `.kaizen-rules-off`. Seen on `agy` 1.3.3; reports say the IDE and the desktop app run no hook.

To act on:

- Antigravity: uninstall the plugin and install it again; an install there is a copy.

## [kaizen 2.0.0] - 2026-11-25

The working rules live in the plugin alone, on the maintainer's direct word: the hook prints them in every repo, and a repo's `CLAUDE.md` holds only what is true of that app, its changes to the rules included.

### Removed

- `norms-config` and its command `/kaizen:norms-config`: the plugin writes no working-rules block into a repo's `CLAUDE.md` or `AGENTS.md`, and no `Output` line.
- The hook no longer goes silent where a `CLAUDE.md` holds a block.

### Changed

- The rules moved to `hooks/rules.md`, without markers or a version.
- Each rule holds until the user waives it in chat or in the repo's `CLAUDE.md`; `Corrections` keeps its table in the repo's `CLAUDE.md`; `Skills, where installed` is `Skills`.

To act on:

- Every app repo with a `<!-- kaizen:rules` block in `CLAUDE.md` or `AGENTS.md`: delete the block, and move a line you reworded there to `## Rules for this app only`.
- A teammate or a machine that read the rules from the block: install the plugin.
- Antigravity: no working rules reach a session there.

## [kaizen 1.7.0] - 2026-11-25

Code stays lean through checks a machine runs, read only where they fail, on the maintainer's direct word after the audit of a real app: things rebuilt, giant files, leftovers and unchecked types. Nothing holds a commit. [What is proven](docs/reference/status.md) lists these as run in no session.

### Added

- `logic-build`: a `Lint floor` section — the linter's own rules, set to error, for unused imports and variables, an explicit `any`, a leftover console or debugger call and function size; old hits frozen in the linter's own baseline, which only shrinks. The floor is asked once, like a cache or a validator.
- `logic-build` and `ui-build`: a query, handler, error handling, form, screen state or fetch is written the way the repo already does it; a second way is a finding, never new code.
- `build-flow`: code added to a file over the repo's size limit goes into a new module named for its job; the limit is asked once and recorded in the Stack table.
- Docs: [Clean up on a schedule](docs/guide/scheduled-cleanup.md), a report of dead code, duplication and large functions, then one cleanup session.

### Changed

- `build-flow` step 9 and `ui-build`'s last step run the repo's typecheck, lint and tests on the files touched, reading only the failures, where they ran the lint alone.

To act on:

- Nothing is required. A session asks for the lint floor and the size limit the first time it needs them in a repo.

## [kaizen 1.6.1] - 2026-11-25

Working rule `Comments` settles a conflict with another plugin that asks for a `shortcut:` comment, on the maintainer's direct word: both reach the same session and contradict each other.

### Changed

- Working rule `Comments`: no `shortcut:` comment even where another plugin asks for one; a shortcut's limit is queued with when to upgrade it.
- The working-rules block sits between `<!-- kaizen:rules 1.6.1 -->` and `<!-- /kaizen:rules -->`.

To act on:

- Nothing is required. A repo with a block keeps its own: run `/kaizen:norms-config` there to write the 1.6.1 block.

## [kaizen 1.6.0] - 2026-11-25

The working rules reach every Claude Code session again, through a hook that only prints them, on the maintainer's direct word: a repo where `norms-config` never ran had none, and a block went stale after an update. [What is proven](docs/reference/status.md) lists the hook as seen in no installed session.

### Added

- Hook `hooks/rules.js` on `SessionStart` (startup, resume, clear, compact) and `SubagentStart`: prints the working-rules block into the context of a session or subagent whose `CLAUDE.md`, in the project folder or a folder above it, holds no block. It never refuses, holds or blocks, and prints nothing where Node is missing.
- An empty `.kaizen-rules-off` file in the project folder or a folder above it turns the hook off for that repo.
- Docs: [Rules hook](docs/reference/rules-hook.md).

### Changed

- The block lives in `skills/norms-config/rules.md`, the one file both the hook and `norms-config` read.
- Working rule `Skills, where installed` says to load the skill before its work, and names `build-flow` for a page or a feature.
- `norms-config` is optional: run it where a teammate works without the plugin, or to keep a reworded block.
- The working-rules block sits between `<!-- kaizen:rules 1.6.0 -->` and `<!-- /kaizen:rules -->`.

To act on:

- Nothing is required. A repo with an older block keeps it and the hook stays silent there: run `/kaizen:norms-config` to write the 1.6.0 block, or delete the block to take the plugin's.

## [kaizen 1.5.0] - 2026-11-19

`ui-build` follows Google's `modern-web-guidance` skill in a web app where it is installed, on the maintainer's direct word; it stays optional, and [What is proven](docs/reference/status.md) lists it as run in no session.

### Added

- `ui-build`: where `modern-web-guidance` is installed and the app is a web app, a new component, or client-side CSS or JS, takes from its guide how to use a browser feature; it never replaces a component the repo or its library has, and never overrules `DESIGN.md`.
- Docs: `modern-web-guidance` as the recommended companion for a web app, with its install on [Claude Code](docs/start/install.md#recommended-for-a-web-app) and [Antigravity](docs/guide/antigravity.md#recommended-for-a-web-app).

## [kaizen 1.4.0] - 2026-11-19

The `Corrections` and `Comments` working rules are one sentence each, because the block is read in every session of every app; what they shed moved to `logic-build`, which loads only when a check is written. Written on the maintainer's direct word; [What is proven](docs/reference/status.md) lists these as run in no session.

### Added

- `logic-build`: a `Checks from corrections` section — where the `| Rule | Enforced by |` table sits, a new check failing only on new additions where the pattern is common, proven to fail on the old mistake, an exception only on its own line with a reason, an expiry date and the user's yes, a prose rule broken again moving up a level, and a row leaving the table once its mistake cannot happen.
- `logic-build`: a rule that computes money, stock or pay also gets a property-based test of its invariant over generated input; the library is asked once and recorded in the Stack table.
- `logic-build`: allowed status transitions are enforced in the database, by a transitions table or a trigger, and their rule test attempts a forbidden transition.
- Docs: [Check features on a schedule](docs/guide/scheduled-walk.md), a read-only run that walks the features table on a schedule and reports what broke.

### Changed

- Working rule `Corrections` names the order of levels and the table only; `Comments` also forbids a comment that states a shortcut's limit, and keeps a license, an outside constraint, a public API contract or an issue link.
- `logic-build` also loads when a session writes a lint, type or test that makes a corrected mistake impossible.
- The working-rules block sits between `<!-- kaizen:rules 1.4.0 -->` and `<!-- /kaizen:rules -->`.

To act on:

- Every app repo: run `/kaizen:norms-config` to write the 1.4.0 block.

## [kaizen 1.3.0] - 2026-11-19

A correction now ends in a check where one can hold, because a rule an agent reads loses to the pattern it copies from the code beside it. These rules come from published practice of teams whose code is mostly written by agents, on the maintainer's direct word, and not from a miss seen twice in an app here; [What is proven](docs/reference/status.md) lists them as run in no session.

### Added

- Working rules `Corrections` and `Comments`, making the block ten lines. `Corrections`: after fixing what the user corrected, offer to make the mistake impossible — the code's structure, a type, a lint whose error names the replacement, a test, prose last — with a check that fails only on new additions where the pattern is common, proven to fail on the old mistake, and recorded in a `| Rule | Enforced by |` table under `## Rules for this app only`, outside the block. `Comments`: no comment that excuses a workaround; the rest of a fix, a shortcut's limit included, goes where the repo keeps its owed work.
- `docs-format`: a `## Features` table in `docs/product.md`, one row per feature — `Feature · How a user reaches it · Drive · Proof · Gotchas`.
- `app-settle`: Document mode writes the features table for the features the app's routes or menu show.
- `build-flow`: the walk ends on the feature's `Proof` with a screenshot of each state; a scripted walk runs only through the repo's one driver; a new feature adds its row; a vague bug report is read against the features table first; a fix that replaces a pattern used elsewhere queues the other copies as one line.
- `logic-build`: a bug fix's test is named in the row of the mistake it fixed, where `CLAUDE.md` keeps the table.

### Changed

- The working-rules block sits between `<!-- kaizen:rules 1.3.0 -->` and `<!-- /kaizen:rules -->`.
- `build-flow` also loads when the user reports a bug in a page.

To act on:

- Every app repo: run `/kaizen:norms-config` to write the 1.3.0 block.

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
