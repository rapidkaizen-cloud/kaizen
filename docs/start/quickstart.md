# Quickstart

Pick the case that matches your repo, run the commands, and answer what the session asks.

## A new app

1. **Open Claude Code in an empty directory.**
2. **Run `/kaizen:app-settle`.** It finds no app code, interviews you, asks one round about the stack, shows what it will write and waits for your yes. It then writes `CLAUDE.md` and the documents, and commits.
3. **Run `/kaizen:norms-config`.** It adds the eight working rules to `CLAUDE.md`.
4. **Run `/kaizen:design-settle`**, where the app has a UI.
5. **Ask for the first page.**

The long version: [Start a new app](../guide/new-app.md).

## An app that already runs

1. **Open Claude Code in the repo and run `/kaizen:norms-config`.** One commit; nothing about the app changes.
2. **Run `/kaizen:app-settle`** where the repo has no documents. It records the stack as it finds it and changes no code.
3. **Run `/kaizen:design-settle`** only when you want the look settled or changed.

The long version: [Bring in an existing app](../guide/existing-app.md).

## One of them alone

Each command works without the others. A repo with only the working rules, or only a `DESIGN.md`, is a complete use of the plugin.

## What you will notice afterwards

In a repo that carries the working rules, a session:

- **Commits a finished item in the same turn**, naming the files.
- **Pushes and merges only on your word.**
- **Counts the rows before a statement that deletes or rewrites them**, shows the number and waits for your yes.
- **Puts a decision to you as options with one recommendation**, and runs commands itself.

These are lines of text the session follows, never locks. See [Working rules](../concepts/working-rules.md).

## Stuck?

Run `/kaizen:norms-help`, or ask a session in your own words which command to run. See [norms-help](../reference/norms-help.md).
