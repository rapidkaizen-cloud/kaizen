---
name: build-flow
description: How to build an app one page at a time so every session ends on something that works — the unit of work, the queue line, proposing a page's content before code, the order inside a page, and the three stops. Use when the user asks to build or continue a feature, a page or a batch of pages.
---

# build-flow — one page at a time

## The unit

- **Build what fits one context window**: one page, or one batch of pages of the same kind.
- **Test every split**: *if I stop here, does any page that used to work stop working?* Yes → cut somewhere else.
- **More work than one unit → build the first unit and queue the rest.**

## The queue

`docs/queue.md` is a queue, never a record. A repo with no `docs/` folder keeps none: list the rest in the closing report instead.

- **One line per unit**: `- <page> — <role> — <the work that can be finished there>`.
- **Add `(needs: <page>)` only for a real dependency.**
- **Delete a line in the commit that finishes it, and the file with its last line.** History is `git log docs/queue.md`.
- **No status column, checkbox or date.**

## Before code

- **Read what binds the page**: `docs/rules.md`, the roles and prohibitions of `docs/product.md`, `DESIGN.md`, and the pages that exist. A file that is absent binds nothing.
- **Propose the page's content, then ask everything in one turn**:
  - `Bound` — what the documents or the request require. Stated, never asked.
  - `Optional` — what you would add. One multi-select of what to drop, with `keep all` first.
- **A page whose data source is not built yet is built against a fixture typed like the real response**, and the report says so.
- **Hand a subagent only work that needs no taste and no decision**: a search, a count, a mechanical edit across files.

## Order inside a page

A page that writes or reads new data:

1. The business rule, written down before its code.
2. The migration and its RLS policy.
3. The test of that policy as each role.
4. Types regenerated from the live schema.
5. The query, in the data layer.
6. The test of the rule.
7. The page, wired to the query, with its loading, empty and failed states.
8. A walk in the browser as the role the page is for: the action it exists for, its empty state, one failure.
9. The repo's lint command.
10. The documents the change made false.

A page with no new data starts at step 7.

- **No browser tool at hand → report the page `not walked`**, never as working.
- **Read every new on-screen string once before the lint**: short, one term per concept.

## The three stops

Stop, leave the working tree dirty and report, only at:

1. **A destructive database operation**: count the rows and show the number. The user approves a number, never an intent.
2. **A role test that misses**: a role sees a row it must not, or misses one it must.
3. **A business rule nobody recorded**: ask, never invent it.

Anything else is yours to decide: take the default and name it in the closing report.

## Closing

- **Commit the unit, naming its paths**, with the documents it made false and without its queue line.
- **Report per page**: built · walked as which role, or `not walked` · what is left.
- **A commit that changes no document says so**: `Docs: none — <why>`.
