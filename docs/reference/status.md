# What is proven

What has been seen working, and what has only been written — so you know which parts of `kaizen` 1.0.0 you are the first to run.

Version 1.0.0 rewrote every skill. What earlier versions proved was proved on text that no longer exists, so it is not carried here.

## Proven on Claude Code

| What | How it was seen |
|---|---|
| `verify_pages.js` | Its self-check passes, and it was run in headless Chrome against two scratch pages |
| `norms-help` | Its self-check passes: the card is built from the files of this version |
| Rules hook | Its self-check passes: it prints where a repo has no block, and stays silent with a block, with `.kaizen-rules-off` and without Node, from folders whose paths hold a space |
| `Quota` | `claude -p "/usage"` was read on a Max plan |

## Proven on Antigravity

Nothing at 1.0.0. The plugin has not been installed there since the rewrite.

## Not yet verified

- **Every rebuilt skill.** `app-settle`, `design-settle`, `norms-config`, `build-flow`, `docs-format`, `ui-build`, `db-ops` and `logic-build` at 1.0.0 have run in no session, on no model.
- **The 1.3.0 additions.** The `Corrections` and `Comments` working rules, the features table, the walk through one driver and the queue line for old copies were written on the maintainer's word from published practice of teams whose code is mostly written by agents, not from a miss seen in an app here, and have run in no session.
- **The 1.4.0 additions.** The one-sentence `Corrections` and `Comments` lines, the checks section of `logic-build`, the property-based test for money, stock and pay, the status-transitions row, and the run in [Check features on a schedule](../guide/scheduled-walk.md) have run in no session.
- **The 1.5.0 addition.** `ui-build` following `modern-web-guidance` in a web app has run in no session, on Claude Code or Antigravity.
- **The 1.6.0 hook in a session.** No installed session has been seen receiving the rules from it, and none has loaded `build-flow` from the rules' last line.
- **The 1.6.1 `Comments` clause.** No session has yet queued a shortcut's limit in place of a `shortcut:` comment another plugin asked for.
- **The 1.7.0 additions.** Typecheck and tests on the files a unit touched, the size limit, one way per task, the lint floor with its baseline, and the run in [Clean up on a schedule](../guide/scheduled-cleanup.md) have run in no session.
- **Loading by itself.** Whether a session loads a rule skill without being asked depends on the host listing its description; where it lists the name only, the working rules' last line names it.
- **The working rules as text.** How well a session keeps a rule nothing enforces has not been measured.
- **What a run costs.** Every figure in [Run on a Pro plan](../guide/pro-plan.md) was measured on the flow before 1.0.0.
- **`verify_pages.js` against a desktop build**: not yet attached to a WebView2 or Electron app.
- **`Quota` on a Pro plan.**
- **`AGENTS.md` on Antigravity**: whether the block written there reaches a session.

## Related

- [How it works](../concepts/how-it-works.md)
- [Antigravity](../guide/antigravity.md)
