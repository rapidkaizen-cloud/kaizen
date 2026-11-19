# kaizen

`kaizen` is a plugin for Claude Code and Antigravity: nine standalone skills for building an app with an agent. Two interviews write an app's documents and its design, five sets of rules load as a session builds, one skill writes ten working rules into the repo's own `CLAUDE.md`, and one prints help. Nothing is enforced: every rule is text you can waive in chat.

The name is *kaizen*, Japanese for continuous improvement.

## Install

Claude Code:

```
/plugin marketplace add rapidkaizen-cloud/kaizen
/plugin install kaizen@kaizen
```

Antigravity:

```
agy plugin install https://github.com/rapidkaizen-cloud/kaizen
```

Requirements and optional design skills: [Claude Code](docs/start/install.md), [Antigravity](docs/guide/antigravity.md).

## Use

In an empty folder, run `/kaizen:app-settle`, then `/kaizen:norms-config`, and `/kaizen:design-settle` where the app has a UI. After that, ask for a page. Each skill stands alone: run any one without the others.

An app that already exists: [Quickstart](docs/start/quickstart.md). Every command: [Commands](docs/reference/commands.md).

## Documentation

<https://rapidkaizen-cloud.github.io/kaizen/>, or the same pages under [`docs/`](docs/README.md). What changed: [CHANGELOG.md](CHANGELOG.md). In a session: `/kaizen:norms-help`.
