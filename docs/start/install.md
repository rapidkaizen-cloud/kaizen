# Install

Two commands in Claude Code and a restart. For Antigravity, see [Run on Antigravity](../guide/antigravity.md).

## Before you start

| Needs | Why |
|---|---|
| Claude Code | The host the commands below are typed into |
| `python3` | `norms-help` calls it |
| Node.js | The script `design-settle` checks a page with runs on it |

## Install the plugin

```
/plugin marketplace add rapidkaizen-cloud/kaizen
/plugin install kaizen@kaizen
```

1. **Install at user scope only.** A project-scope entry updates separately and falls behind.
2. **Turn on `autoUpdate`.** In `~/.claude/settings.json`, set `"autoUpdate": true` on `kaizen` under `extraKnownMarketplaces`, so a new version reaches the machine at its next start.
3. **Restart Claude Code.**

The plugin asks nothing and prints nothing when a session starts. To give a repo the working rules, run `/kaizen:norms-config` once in it: see [Working rules](../concepts/working-rules.md).

## Optional design skills

None is required, and a session never asks for one. Where one is installed, `design-settle` and `ui-build` read the part of it the work at hand needs.

| Skill | Install |
|---|---|
| `impeccable` | `npx impeccable install` |
| `frontend-design` | `/plugin` |
| `ui-ux-pro-max` | `/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill`, then `/plugin install ui-ux-pro-max@ui-ux-pro-max-skill` |

## A browser

- **For `design-settle`'s check**: Chrome installed on the machine, and Playwright in the app repo's own `node_modules`. Nothing is installed for you: where the repo has no Playwright, the check is reported `not verified`.
- **For walking a page a session built**: any browser tool the session has, an MCP server for example. Without one the page is reported `not walked`.

## Check that it loaded

- `/plugin` lists `kaizen`.
- `/kaizen:norms-help` prints the running version, the commands and the last change, in any session.
- `design-settle` prints the running build as `Skill build` in the block it opens with.

## Next

- [Quickstart](quickstart.md) — the first run.
- [Update the plugin](../guide/update.md) — on a machine without `autoUpdate`, and moving to 1.0.0.
- [Run on a Pro plan](../guide/pro-plan.md) — what to turn off before a redesign on a Pro plan.
