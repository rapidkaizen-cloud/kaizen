# Hosts

The same eight skills install on Claude Code and on Antigravity; the working rules reach both, through a hook on each.

| | Claude Code | Antigravity |
|---|---|---|
| Manifest | `.claude-plugin/plugin.json` | `plugin.json` at the repo root, with the same version and the logo |
| Hook file | `hooks/claude-code.json` | `hooks.json` at the repo root |
| Install | `/plugin marketplace add`, then `/plugin install` | `agy plugin install <URL>`; not in Antigravity's marketplace |
| Update | By itself with `autoUpdate` on | Uninstall, then install again: the install is a copy |
| Skills | All eight | All eight |
| Working rules | Printed by the plugin's hook into every session and subagent | Printed once per conversation, before its first model call, by a `PreInvocation` hook in `hooks.json` at the repo root — on the `agy` CLI |
| Repo instructions | `CLAUDE.md`; `AGENTS.md` through its `@AGENTS.md` line, or where the repo has no `CLAUDE.md` | `AGENTS.md`; never `CLAUDE.md` |
| `Quota` row of `design-settle` | Read from `claude -p "/usage"` | Printed as `not read` |

> [!NOTE]
> Of 2.1.0, only the working rules were seen on Antigravity: on `agy` 1.3.3, installed from a folder. Which repo file it reads was seen on `agy` 1.5.16. Every other row of that column describes what the plugin ships, never what was seen. See [What is proven](../reference/status.md).

## Switching hosts mid-work

Nothing a skill writes belongs to one host: `AGENTS.md`, `docs/`, `DESIGN.md` and the commits are the whole hand-over. A session on either host reads them, as long as a repo's own rules sit in `AGENTS.md`: a line written only in `CLAUDE.md` never reaches Antigravity, and in a repo with a `CLAUDE.md`, Claude Code reads `AGENTS.md` only through its `@AGENTS.md` line. A symlink from `CLAUDE.md` to `AGENTS.md` does not work on Windows, where Git checks it out as a text holding the path.

## Related

- [Install](../start/install.md) — Claude Code.
- [Run on Antigravity](../guide/antigravity.md)
- [Update the plugin](../guide/update.md)
