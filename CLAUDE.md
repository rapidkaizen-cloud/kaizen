# CLAUDE.md — repo kaizen

This repo is not an application. Its root is the plugin that other repos install, so a mistake here spreads to every app.

## Language

All files in this repo — `SKILL.md`, scripts, docs, README — are written in English, so they work for anyone who installs them.

Reply language is not fixed. Follow whichever language the user writes in.

## Rules

Skills here are read by other agents, not by humans. Write them as direct instructions, not as observations.

Keep every rule short. One rule is one imperative sentence. Give its reason in one clause, only when an agent would otherwise break the rule. Cut any paragraph that argues, defends, or restates. State each rule in one file only.

Write each skill as one `SKILL.md` with no `references/` folder, because a skill costs what a session reads to run it.

Make every skill stand alone: it names no other skill, requires none, and runs in a repo where `docs/` and `DESIGN.md` are absent. The one exception is the last line of the rules block in `skills/norms-config/rules.md`, which names five skills `where installed`.

Change a rule for a finding seen in two sessions or in a real app, or on the user's direct word; a finding seen once is a line of `docs/reference/status.md`, because one session's miss is as often the session as the rule.

Do not add a skill to `kaizen` without naming what would be lost if it did not exist. Every skill pays a context cost in every session through its description, including the sessions that never use it.

Never add a hook that refuses, holds or blocks, because a hook cannot ask and a rule here is negotiable in chat. The plugin ships one hook, `hooks/rules.js`, which only prints the rules block where a repo's `CLAUDE.md` lacks one; the context reminder was removed on the user's word because its note interrupted the work.

This plugin ships no templates. What a new app repo gets is written by `app-settle` for that repo's answers — never a stock file, which is a decision taken before its question was asked and goes stale without anyone re-reading it. Whatever a skill here tells a session to write lands in app repos that may not be private, so a rule that produces a file must never produce a secret in it: name the variable, never its value.

## Proof runs

A proof run tests a script on a throwaway copy of an app in the scratchpad. Never run one to judge a skill: a skill's findings come from its use in a real app, read with `app-eval`, because a copy answered by a script shows the copy's faults. Write only the public client values into the copy's `.env` — the URL and the publishable key; never copy the real `.env`. A server key reaches the copy only by the user's own hand: a key created for the run and revoked after it. Without one, report every server route `not verified — no server key in the proof copy`.

Write `the proof app`, never the app's name, a client, a person, or a domain, in any file or commit message of this repo, because anyone who installs the plugin reads its history.

## docs/

Write `docs/` for the people who install the plugin, never for agents: a rule stays in its skill and is not restated there.

A commit that changes what a user meets — a question, a stop, a command, a file a skill writes — corrects that feature's page under `docs/` in the same commit, or writes the page where it has none.

Put a page in the group its reader comes for: `start/` to begin, `concepts/` to understand, `guide/` to finish one task in numbered steps, `reference/` for one page per skill, hook and command.

List every page in `docs/README.md` under its group, because that file is the index on GitHub, the site's home and its sidebar, and what `norms-help` prints: a page it does not list is in none of them.

Write a page in GitHub-flavored Markdown only — no frontmatter, no `:::` container, no include — and open it with its `# ` title and one lead sentence, because the same file is read on GitHub, on the site and by a session.

Keep `docs/queue.md` only while it holds an edit this toolkit still owes, and delete it with its last item.

Write a rule no session has run as a line of `docs/reference/status.md`, never as a queue line, because a queue of runs owed refills with every edit.

Keep `CHANGELOG.md` at the root and the commands a user runs in `docs/reference/commands.md`, because `norms-help` prints the first's top entry and the second whole from an installed copy.

## Git

Commit, push and merge by the `Git` line of the rules block in `skills/norms-config/rules.md`, as an app repo does.

A commit that changes the plugin — `skills/`, `scripts/`, `hooks/` or a manifest — bumps its `version` in the same commit, because `/plugin update` compares version numbers only; `.githooks/pre-commit` refuses it otherwise, so run `git config core.hooksPath .githooks` once per clone.

A commit that bumps the version adds that version's entry to `CHANGELOG.md`, in English and in Keep a Changelog form, naming every rename or removal an installed app must act on; `.githooks/pre-commit` refuses the bump without it, and warns when the plugin changed and no page under `docs/` did.

A commit that changes the rules block in `skills/norms-config/rules.md` sets the version in its opening marker to that commit's plugin version, because the marker is how an app repo's block is found to be older.

A commit reaches app sessions only after it is pushed to `origin`, and the user decides every push.
