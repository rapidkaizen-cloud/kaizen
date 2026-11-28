# logic-build

The rules a session follows for the logic layer: which key goes where, where a business rule is enforced, and the test each rule leaves.

| | |
|---|---|
| Kind | Skill — no command |
| Loads when | A session writes a query, an API handler, an environment variable, anything that holds a key, code that enforces a business rule, a check that makes a mistake you corrected impossible, or fixes a slow page |
| Reads | `docs/rules.md` and the Stack table of `AGENTS.md`, where the repo has them |
| Source | `skills/logic-build/SKILL.md` |

## What you will see

- **Keys kept apart.** The public key in the client, the secret one on the server only. A variable whose prefix ships it to the browser is never given a secret.
- **A stop on a committed secret.** The session names the variable and asks you to rotate it first.
- **One rule in one place.** Access in RLS, uniqueness in a constraint, the allowed moves between statuses in a transitions table or a trigger, a computation or a workflow in one named place. A client check that repeats a server rule is named a mirror.
- **A question for an unrecorded rule.** A business rule `docs/rules.md` does not hold is asked, never invented.
- **Errors you can act on.** The screen gets a sentence; the log gets the detail.
- **A test per rule**, titled with the rule's name, that attacks the point where the rule is enforced. For a status, it tries a forbidden transition and expects the refusal.
- **A property-based test for money, stock and pay**: generated input checks an invariant, such as a total always equal to the sum of its lines. The library is asked once and recorded in the Stack table.
- **The repo's way, once.** A query, handler or error handling is written the way the repo already does it; a second way is reported, never added.
- **A test per bug fix** that fails without the fix. Where `AGENTS.md` keeps a `Rule | Enforced by` table, the test is named in the row of the mistake it fixed.

## Checks from corrections

When a session turns a mistake you corrected into a check, by the `Corrections` line of the [working rules](../concepts/working-rules.md):

- **The `| Rule | Enforced by |` table** sits under `## Rules for this app only` in `AGENTS.md`.
- **Shown failing on the old mistake** before the check is kept.
- **Only new additions fail** where the pattern is already common; the old copies become one queue line.
- **An exception** sits on the offending line itself, with a reason, an expiry date and your yes.
- **A prose rule broken again** moves up one level in the same change.
- **A row leaves the table** once its mistake cannot happen.

## A choice nobody recorded

The first time a session needs something the repo has not chosen — a cache, a validator, a date library, where errors go, background jobs, the lint floor — it asks once, with a recommendation, and records the answer as a row of the Stack table in `AGENTS.md`. `none` is an answer, and it is recorded too.

## Lint floor

Asked once, then kept by every session that writes code: the linter's own rules, set to error, for unused imports and variables, an explicit `any` or its counterpart, a leftover console or debugger call, and function size at a limit recorded with it.

- **Old code is frozen** in the linter's own baseline file, never by lowering a rule to a warning. New code passes.
- **The baseline only shrinks.** A cleanup removes the entries it fixed; nothing is added to it.
- **What a linter cannot see** — unused exports and files, duplicated blocks — waits for a report: [Clean up on a schedule](../guide/scheduled-cleanup.md).

## Performance

- **No query or outside call inside a loop.** Writes are batched and a list is looked up by key. The session guards it with the stack's own check — the framework's lazy-loading guard or a lint rule, else a test that counts a page's queries — named in the `| Rule | Enforced by |` table.
- **Only what the screen uses is read**: a limit on every list, cursor paging on a big table, paging past an API's row cap, and filtering, sorting and totals done by the database.
- **The same data is read once** per request and through the client's data cache. A total over a big table is precomputed or cached, and every in-memory cache has a size cap or an expiry.
- **Independent calls run in parallel**, on the server and in the client.
- **Slow work runs in a background job** — email, exports, outside APIs, logging — and a big export or import streams in chunks.
- **Clients, config and static data are created once per process**, not per request.
- **Transactions stay short** and never wait on an outside call. An outside service is retried with capped backoff, inside its rate limit.
- **Uploads are capped** at the handler, images resized and compressed, and files kept in storage, never in a database column.
- **A page you report slow is measured first** — a trace, the query plan, the database's slow-query stats — and the report gives the numbers before and after the fix.

Further reading, not required: [Performance antipatterns for cloud applications](https://learn.microsoft.com/azure/architecture/antipatterns/) from Microsoft.

## The data layer

Every database call lives in one folder, named in the `Data layer` row of the Stack table. Where the row is absent, a new query goes beside the ones that exist.

## Without a test runner

The session raises it once: install one now, or carry on unproven with a line `Prove: <rule>` where the repo keeps its owed work.

## What it does not cover

- **A settled architecture document.** The Stack table of `AGENTS.md` is the record.

## Related

- [db-ops](db-ops.md)
- [Documents](../concepts/documents.md)
