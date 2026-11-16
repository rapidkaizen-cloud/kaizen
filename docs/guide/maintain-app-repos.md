# Maintain app repos

A repo started under an older version still carries files and sections that 1.0.0 neither reads nor maintains; nothing breaks while they stay.

## After an update that changes the working rules

Run `/kaizn:norms-config` in each repo. A version's changelog entry says when the block changed. See [Working rules](../concepts/working-rules.md).

## What a repo from before 1.0.0 still carries

| Found | Where | What to do |
|---|---|---|
| No working rules | `CLAUDE.md` | Run `/kaizn:norms-config` once. Until then none of the old session norms reaches a session there: they are no longer printed at session start |
| `switches.json`, the marker `onboarded-output` | The plugin's data folder on the machine | Nothing reads them. Delete them or leave them |
| `.claude/destructive-gate.off` | The repo | Nothing reads it. Delete it |
| An output folder set through the old `norms-config` | `switches.json` | No longer printed or guarded. Name the folder to `/kaizn:norms-config` to get it as a line of the working rules |
| Sections an older `app-settle` wrote | `CLAUDE.md` | Kept as they are. `app-settle` adds only what the file lacks |
| A root `PRD.md` or `docs/PRD.md` | The repo | Read as it is. It no longer marks a repo as settled, and no skill moves it unless you ask |
| Lint floors and rule tests | The repo's lint config and tests | They are the repo's own and keep running. No skill maintains them |
| Documents beyond `product.md`, `rules.md`, `queue.md`, `changelog.md` | `docs/` | Kept, and kept true. No skill writes a new one unless you ask |
| The plugin installed at project scope | The repo's `.claude/settings.json` | It updates separately from the user-scope install and falls behind: see [Update the plugin](update.md) |

## What is gone, with nothing in its place

- **The audit and the modes `migrate`, `align`, `rework` and `seed`** of `app-settle`. It has two modes: `Bootstrap` and `Document`.
- **`logic-settle`.** A need with no recorded choice — a cache, a validator, where errors go — is asked once by the session that first meets it, and recorded in the Stack table of `CLAUDE.md`.
- **Every guard.** See [How it works](../concepts/how-it-works.md) for what holds a push or a destructive statement now.

## Related

- [Update the plugin](update.md) — moving to 1.0.0.
- [Documents](../concepts/documents.md)
