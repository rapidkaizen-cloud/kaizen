# What is proven

What has been seen working, and what has only been written — so you know which parts of `kaizen` 1.0.0 you are the first to run.

Version 1.0.0 rewrote every skill. What earlier versions proved was proved on text that no longer exists, so it is not carried here.

## Proven on Claude Code

| What | How it was seen |
|---|---|
| `verify_pages.js` | Its self-check passes, and it was run in headless Chrome against two scratch pages |
| `norms-help` | Its self-check passes: the card is built from the files of this version |
| `Quota` | `claude -p "/usage"` was read on a Max plan |

## Proven on Antigravity

Nothing at 1.0.0. The plugin has not been installed there since the rewrite.

## Not yet verified

- **Every rebuilt skill.** `app-settle`, `design-settle`, `norms-config`, `build-flow`, `docs-format`, `ui-build`, `db-ops` and `logic-build` at 1.0.0 have run in no session, on no model.
- **Loading by itself.** Whether a session loads a rule skill without being asked depends on the host listing its description; where it lists the name only, name the skill or keep the working rules' last line.
- **The working rules as text.** How well a session keeps a rule nothing enforces has not been measured.
- **What a run costs.** Every figure in [Run on a Pro plan](../guide/pro-plan.md) was measured on the flow before 1.0.0.
- **`verify_pages.js` against a desktop build**: not yet attached to a WebView2 or Electron app.
- **`Quota` on a Pro plan.**
- **`AGENTS.md` on Antigravity**: whether the block written there reaches a session.

## Related

- [How it works](../concepts/how-it-works.md)
- [Antigravity](../guide/antigravity.md)
