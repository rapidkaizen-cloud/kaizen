# Hosts

The same nine skills install on Claude Code and on Antigravity; the working rules and the one hook do not reach both the same way.

| | Claude Code | Antigravity |
|---|---|---|
| Manifest | `.claude-plugin/plugin.json`, `hooks/hooks.json` | `plugin.json` at the repo root |
| Install | `/plugin marketplace add`, then `/plugin install` | `agy plugin install <URL>` |
| Update | By itself with `autoUpdate` on | Uninstall, then install again: the install is a copy |
| Skills | All nine | All nine |
| Working rules | Read from the repo's `CLAUDE.md` by the host | Not verified: the block is written into `AGENTS.md` where the repo has one |
| Context reminder | Yes | None: the plugin ships no hook there |
| `Quota` row of `design-settle` | Read from `claude -p "/usage"` | Printed as `not read` |

> [!NOTE]
> 1.0.0 has not been installed or run on Antigravity. Every row of that column describes what the plugin ships, never what was seen. See [What is proven](../reference/status.md).

## Switching hosts mid-work

Nothing a skill writes belongs to one host: `CLAUDE.md`, `docs/`, `DESIGN.md` and the commits are the whole hand-over. A session on the other host reads the same files.

## Related

- [Install](../start/install.md) — Claude Code.
- [Run on Antigravity](../guide/antigravity.md)
- [Update the plugin](../guide/update.md)
