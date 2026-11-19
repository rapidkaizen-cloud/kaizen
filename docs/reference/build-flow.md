# build-flow

How a session builds an app one page at a time, so each one ends on something that works.

| | |
|---|---|
| Kind | Skill — no command |
| Loads when | A session builds or continues a feature, a page or a batch of pages, or you report a bug in one |
| Reads | `docs/rules.md`, `docs/product.md`, `DESIGN.md` and the pages that exist. An absent file binds nothing |
| Writes | The page, its queue lines, its row in the features table of `docs/product.md`, the documents the change made false |
| Commits | One unit per commit, naming its paths |
| Source | `skills/build-flow/SKILL.md` |

## What you will see

- **One unit per session**: one page, or one batch of pages of the same kind. More work than that is queued.
- **A proposal before code.** What the documents or your request require is stated as `Bound`. What the session would add is `Optional`: one multi-select of what to drop, with `keep all` first.
- **A walk in the browser** as the role the page is for: the action it exists for, ending on the `Proof` its feature's row names, its empty state, one failure — a screenshot at each state.
- **A report per page**: built · walked in the browser as which role, with the path of each screenshot, or `not walked` · what is left.
- **A vague bug report read against the features table first**: the session finds the feature there and reproduces the bug by its `Drive`.

## One driver per repo

A walk that runs as a script runs through the one driver the repo already has: its end-to-end config, its own walk script, or the plugin's `scripts/verify_pages.js`. A session never writes a new script of its own for a walk, because scripts written per session drift apart. A repo with no driver gets one script, committed, and every later walk reuses it. Screenshots stay out of the commit.

## The queue

`docs/queue.md` holds one line per unit of work owed:

```
- <page> — <role> — <the work that can be finished there>
```

A line is deleted in the commit that finishes it, and the file with its last line. It has no status, checkbox or date: its history is `git log docs/queue.md`. A repo with no `docs/` folder keeps no queue, and the work left is listed in the closing report.

A fix that replaces a pattern used elsewhere fixes the case at hand only, and queues the other copies as one line, so they are cleaned in a change of their own:

```
- <pattern> — <count> copies — <files>
```

## Where it stops

A session leaves the working tree dirty and reports, at three points only:

1. **A destructive database operation.** It shows the row count, and you approve the number.
2. **A role test that misses**: a role sees a row it must not, or misses one it must.
3. **A business rule nobody recorded.** It asks; it never invents one.

Everything else it decides, and names each default in the closing report.

## What it does not cover

- **A page reported as working without a walk.** With no browser tool at hand the page is reported `not walked`.
- **The rules of each layer.** Those are [ui-build](ui-build.md), [db-ops](db-ops.md) and [logic-build](logic-build.md).

## Related

- [Start a new app](../guide/new-app.md)
- [Documents](../concepts/documents.md)
