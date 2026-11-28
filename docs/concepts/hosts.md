# Hosts

The same eight skills install on Claude Code and on Antigravity; the working rules reach both, through a hook on each.

| | Claude Code | Antigravity |
|---|---|---|
| Manifest | `.claude-plugin/plugin.json` | `plugin.json` at the repo root, with the same version and the logo |
| Hook file | `hooks/claude-code.json` | `hooks.json` at the repo root |
| Install | `/plugin marketplace add`, then `/plugin install` | `agy plugin install <URL>`; not in Antigravity's marketplace yet |
| Update | By itself with `autoUpdate` on | Uninstall, then install again: an install from a URL is a copy. A marketplace install updates by itself, once `kaizen` is listed |
| Skills | All eight | All eight |
| Working rules | Printed by the plugin's hook into every session and subagent | Printed once per conversation, before its first model call, by a `PreInvocation` hook in `hooks.json` at the repo root — on the `agy` CLI |
| `Quota` row of `design-settle` | Read from `claude -p "/usage"` | Printed as `not read` |

> [!NOTE]
> Of 2.1.0, only the working rules were seen on Antigravity: on `agy` 1.3.3, installed from a folder. Every other row of that column describes what the plugin ships, never what was seen. See [What is proven](../reference/status.md).

## Switching hosts mid-work

Nothing a skill writes belongs to one host: `CLAUDE.md`, `docs/`, `DESIGN.md` and the commits are the whole hand-over. A session on the other host reads the same files.

## Related

- [Install](../start/install.md) — Claude Code.
- [Run on Antigravity](../guide/antigravity.md)
- [Update the plugin](../guide/update.md)
