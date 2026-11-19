# Check features on a schedule

A scheduled run walks every row of your app's features table against the running app as a read-only account, and reports the rows whose proof no longer shows — it never changes data, opens a pull request or merges.

## Before you start

| You need | Where it comes from |
|---|---|
| A `## Features` table in `docs/product.md` with a `Drive` and a `Proof` on every row | `/kaizen:app-settle` writes it for an app that runs; each build session adds the row of the feature it builds |
| One driver in the repo | The one `build-flow` walks through: the repo's end-to-end config, its own walk script, or the plugin's `scripts/verify_pages.js` |
| An agent account that can only read | A login on the running app whose role is granted reads and no writes |

## Steps

1. **Check the table.** Read `## Features` in `docs/product.md`. A row with no `Drive` or no `Proof` cannot be walked: ask a session to fill it first.
2. **Mark the rows that need a write.** A row whose `Proof` shows only after something is saved, sent or deleted cannot be proven read-only. Write `needs a write` in its `Gotchas`; the run reports it as skipped instead of driving it.
3. **Create the read-only account.** Give it a role whose access rules grant reads only, then try one write by hand as that account: it must be refused. Keep its login in environment variables or the scheduler's secret store, never in the repo or in the instruction.
4. **Write the run's instruction** in a few sentences. It names:
   - the app's URL, and the variables that hold the account's login;
   - the features table as the list to walk, each row by its `Drive`, ending on its `Proof`;
   - the repo's driver as the only way to walk, with a screenshot at each `Proof`;
   - what it never does: write data, commit, push, open a pull request, merge;
   - the report: each failed row with its reason and screenshot, then each skipped row.
5. **Schedule it**, one of:
   - **A Claude Code routine.** In a session in the repo, run `/schedule` and give it the instruction and a time, such as every night. A routine runs in the cloud from the repo on GitHub, not on your machine: the app must be reachable from the internet, the login goes into the routine's environment, and the driver must be one committed in the repo, because a plugin installed on your machine may be absent there.
   - **A scheduler on your machine.** Task Scheduler on Windows, `cron` or `launchd` elsewhere, running `claude -p "<the instruction>"` in the repo. It reaches an app on your own network, and runs only while the machine is on. Nobody is there to approve a permission prompt, so allow the driver's command in the repo's settings first.
6. **Run it once by hand** before leaving it to the schedule. Every row of the table must appear in the report as passed, failed or skipped.
7. **Act on a failed row in an ordinary session**: paste the row and its reason. The session reads the features table first and reproduces the bug by the row's `Drive`; the fix and its pull request wait for your word as any other change does.

## What the run never does

- Write, edit or delete data in the app.
- Commit, push, open a pull request or merge.
- Weaken a row of the features table: a `Proof` it cannot reach is a failure.

> [!WARNING]
> The instruction is text, and nothing enforces it. The read-only account is what keeps a wrong step from changing data: never schedule the run as an account that can write.

## Related

- [Documents](../concepts/documents.md) — the features table.
- [build-flow](../reference/build-flow.md) — the walk and its one driver.
