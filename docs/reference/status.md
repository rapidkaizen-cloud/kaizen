# What is proven

What has been seen working, and what has only been written — so you know which parts of `kaizen` 1.0.0 you are the first to run.

Version 1.0.0 rewrote every skill. What earlier versions proved was proved on text that no longer exists, so it is not carried here.

## Proven on Claude Code

| What | How it was seen |
|---|---|
| `verify_pages.js` | Its self-check passes, and it was run in headless Chrome against two scratch pages |
| `norms-help` | Its self-check passes: the card is built from the files of this version |
| Rules hook | Its self-check passes: it prints in every project, and stays silent with `.kaizen-rules-off` and without Node, from folders whose paths hold a space. An installed 1.7.0 session on Windows received the rules at its start |
| `Quota` | `claude -p "/usage"` was read on a Max plan |
| `@AGENTS.md` (2.5.0) | A headless Sonnet session on Claude Code 2.1.332, with no tool to read files, quoted a word found only in `AGENTS.md` of a folder whose `CLAUDE.md` held `@AGENTS.md` alone. Where `CLAUDE.md` held a line of its own and no import, it named no word from `AGENTS.md` |
| Hook file (2.4.0) | `claude plugin validate` lists the three hooks from `hooks/claude-code.json`, and a headless session on Claude Code 2.1.332 received the rules from a copy loaded with `--plugin-dir` |
| Output folder (2.2.0) | Its self-check passes on Windows. Sessions on Claude Code 2.1.332 on Windows used the right folder in a repo, a worktree (a plain file, a script and a subagent), an Orca folder workspace and a plain folder outside Orca, on Haiku, and in a repo on Opus 5.5 with a user `CLAUDE.md` still holding the old `Output` line. `Write` from a worktree into the repo's folder drew the hook's note. Unset, files stayed in the project. An earlier draft with one folder for all was kept by Haiku, Sonnet 5.5 and Opus 5.5, by file, script and subagent, and by an icon-extraction task like the one that left files at a drive root |

## Proven on Antigravity

| What | How it was seen |
|---|---|
| Working rules | 2.1.0 installed from a folder on `agy` 1.3.3: a headless conversation received them once, before its first model call, and not again on its second turn |
| Output folder | An earlier draft with one folder for all, on `agy` 1.5.13 with Gemini 3.8 Flash Low: a plain file landed there; of two runs through a script, one left a copy outside after its three-minute limit |
| Marketplace check (2.4.0) | `agy plugin validate --strict` passes with no finding on `agy` 1.5.16 |
| Repo instructions (2.5.0) | On `agy` 1.5.16 a headless conversation, given a different word in each file, quoted the words of `AGENTS.md` and `GEMINI.md` and never the one of `CLAUDE.md` |

## Not yet verified

- **Every rebuilt skill.** `app-settle`, `design-settle`, `build-flow`, `docs-format`, `ui-build`, `db-ops` and `logic-build` at 1.0.0 have run in no session, on no model.
- **The 1.3.0 additions.** The `Corrections` and `Comments` working rules, the features table, the walk through one driver and the queue line for old copies were written on the maintainer's word from published practice of teams whose code is mostly written by agents, not from a miss seen in an app here, and have run in no session.
- **The 1.4.0 additions.** The one-sentence `Corrections` and `Comments` lines, the checks section of `logic-build`, the property-based test for money, stock and pay, the status-transitions row, and the run in [Check features on a schedule](../guide/scheduled-walk.md) have run in no session.
- **The 1.5.0 addition.** `ui-build` following `modern-web-guidance` in a web app has run in no session, on Claude Code or Antigravity.
- **The 1.6.0 router line.** No session has been seen loading `build-flow` from the rules' last line.
- **The 1.6.1 `Comments` clause.** No session has yet queued a shortcut's limit in place of a `shortcut:` comment another plugin asked for.
- **The 1.7.0 additions.** Typecheck and tests on the files a unit touched, the size limit, one way per task, the lint floor with its baseline, and the run in [Clean up on a schedule](../guide/scheduled-cleanup.md) have run in no session.
- **The 2.0.0 waiver in a repo's own rules.** No session has yet been seen giving way to a line of a repo's `AGENTS.md` or `CLAUDE.md` that changes a printed rule.
- **The 2.5.0 move to `AGENTS.md`.** `app-settle` writing `AGENTS.md` and a `CLAUDE.md` that imports it, and moving a `CLAUDE.md`'s own lines across, has run in no session; no session has yet been seen writing a new repo rule into `AGENTS.md` from the working rules' first line.
- **Loading by itself.** Whether a session loads a rule skill without being asked depends on the host listing its description; where it lists the name only, the working rules' last line names it.
- **The working rules as text.** How well a session keeps a rule nothing enforces has not been measured.
- **What a run costs.** Every figure in [Run on a Pro plan](../guide/pro-plan.md) was measured on the flow before 1.0.0.
- **`verify_pages.js` against a desktop build**: not yet attached to a WebView2 or Electron app.
- **`Quota` on a Pro plan.**
- **The 2.3.0 performance rules.** The index, key and RLS lines of `db-ops`, the performance sections of `logic-build` and `ui-build`, and the three checks they add — the index test, the query guard and the bundle budget — were written on the maintainer's word from published catalogs, not from a miss seen in an app here, and have run in no session.
- **The 2.4.0 listing fields on Antigravity.** The logo, display name and suggested prompts were read by the validator only; the plugin is not submitted to Antigravity's marketplace.
- **The 2.2.0 output folder** on Linux and macOS (only the hook command under `dash` and the path logic under Node's POSIX rules were run), in the Claude desktop app, in a workspace Orca created itself, and split per repo in a real Antigravity session. The `Write` note was seen on Haiku only.

## Related

- [How it works](../concepts/how-it-works.md)
- [Antigravity](../guide/antigravity.md)
