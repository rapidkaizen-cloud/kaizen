# Hosts

The same eight skills install on Claude Code and on Antigravity; the working rules reach Claude Code only.

| | Claude Code | Antigravity |
|---|---|---|
| Manifest | `.claude-plugin/plugin.json` | `plugin.json` at the repo root |
| Install | `/plugin marketplace add`, then `/plugin install` | `agy plugin install <URL>` |
| Update | By itself with `autoUpdate` on | Uninstall, then install again: the install is a copy |
| Skills | All eight | All eight |
| Working rules | Printed by the plugin's hook | None: no hook runs there |
| `Quota` row of `design-settle` | Read from `claude -p "/usage"` | Printed as `not read` |

> [!NOTE]
> 1.0.0 has not been installed or run on Antigravity. Every row of that column describes what the plugin ships, never what was seen. See [What is proven](../reference/status.md).

## Switching hosts mid-work

Nothing a skill writes belongs to one host: `CLAUDE.md`, `docs/`, `DESIGN.md` and the commits are the whole hand-over. A session on the other host reads the same files.

## Related

- [Install](../start/install.md) — Claude Code.
- [Run on Antigravity](../guide/antigravity.md)
- [Update the plugin](../guide/update.md)
