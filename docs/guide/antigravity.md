# Run on Antigravity

One command in a terminal, once per machine, and the eight skills are there in every folder `agy` opens. For Claude Code, see [Install](../start/install.md).

> [!NOTE]
> Version 1.0.0 has not been installed or run on Antigravity. What this page says was seen on earlier versions; [What is proven](../reference/status.md) says what has not been seen since.

## Before you start

| Needs | Why |
|---|---|
| The Antigravity CLI, `agy` | The host the command below is typed into. The IDE and Antigravity 2.0 are not verified |
| `python3` | `norms-help` calls it |

## Install the plugin

```
agy plugin install https://github.com/rapidkaizen-cloud/kaizen
```

The copy lands in `~/.gemini/config/plugins/kaizen`.

> [!WARNING]
> Install it for the machine, never through a repo's `.agents/plugins.json`. Registered per folder, the plugin loaded a minute after an interactive conversation began.

## What is absent there

- **The `Quota` row** of `design-settle`: it reads `not read`.
- **The working rules.** The hook that prints them is written for Claude Code only.

## Optional design skills

None is required: the same three as on Claude Code, read where installed.

| Skill | Install |
|---|---|
| `impeccable` | Copy the folder that holds its `SKILL.md` to `~/.gemini/config/skills/impeccable/` |
| `frontend-design` | Copy its folder to `~/.gemini/config/skills/frontend-design/` |
| `ui-ux-pro-max` | Copy the folder that holds its `SKILL.md` to `~/.gemini/config/skills/ui-ux-pro-max/` |

> [!NOTE]
> A skill is found only as a folder of its own under `~/.gemini/config/skills/`. Under `~/.gemini/antigravity-cli/skills/`, or as a link to a folder elsewhere, it is never listed.

## Recommended for a web app

`modern-web-guidance`, which `ui-build` follows for how new UI uses a browser feature — see [Install](../start/install.md#recommended-for-a-web-app). Not required.

```
agy plugin install https://github.com/GoogleChrome/modern-web-guidance
```

## Check that it loaded

- `agy plugin list` names `kaizen`.

## Update

```
agy plugin uninstall kaizen
agy plugin install https://github.com/rapidkaizen-cloud/kaizen
```

The install is a copy, and nothing refreshes it.

## Headless runs

A headless run (`agy -p`) cannot be asked for permission, and a skill file sits outside the workspace.

1. **Allow the plugin folder to be read**, in `~/.gemini/antigravity-cli/settings.json`, or the run stops at the first skill it reads:

   ```json
   {"permissions": {"allow": ["read_file(C:/Users/<you>/.gemini/config/plugins/kaizen)"]}}
   ```

2. **For a headless `design-settle` run, allow all of these**, or the turn ends with no output at the first one missing:

   | Permission | On |
   |---|---|
   | `read_file` | The plugin, the skills folder, the repo |
   | `write_file` | The repo |
   | `command(*)` | Every command — `command(git)` does not cover `git status` |

3. **Refuse what must never run through `deny`**, which does not end the turn.
4. **Continue the conversation with `--conversation <id>`.** A dev server started in a headless turn dies when the turn ends.

## Related

- [Hosts](../concepts/hosts.md) — what differs from Claude Code, and switching hosts mid-work.
- [What is proven](../reference/status.md) — what has run for real on Antigravity.
