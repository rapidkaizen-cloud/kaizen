# Clean up on a schedule

A run on request or on a schedule reports the dead code, duplication and oversized functions in your app, and one cleanup session removes what it found — nothing holds a commit in between.

## Before you start

| You need | Where it comes from |
|---|---|
| A lint floor with a baseline | A session asks for it once, by `logic-build`, and records it as a row of the Stack table in `AGENTS.md` |
| A detector for what a linter cannot see: unused exports and files, duplicated blocks | Your choice, such as `fallow` or `knip` for TypeScript, or PHPStan with a dead-code extension for PHP. Record it in the same row |

## Steps

1. **Write the run's instruction** in a few sentences. It names:
   - the detector's command, run over the whole repo;
   - the report: a count per kind and the ten largest of each, never the full output;
   - what it never does: change a file, commit, push.
2. **Run it when you want, or schedule it** the two ways [Check features on a schedule](scheduled-walk.md#steps) describes: a `/schedule` routine, or a scheduler on your machine. Once a month suits most apps.
3. **Clean up in one session.** Paste the report. The session deletes what is unused, merges near-copies that must change together, splits a function only by job, and removes from the baseline each entry it fixed. It hands the mechanical deletions to a subagent.
4. **Compare the next report.** Each count goes down or stays; a count that grew names the code written since the last run.

## Why a report, not a gate

Nothing refuses a commit. The lint floor is met in the session that writes the code, and what only a whole-repo detector sees waits for this run. A count per kind keeps the run cheap to read, where a full list would be read again in every session that opens it.

## What the run never does

- Change a file, commit or push.
- Add to the baseline.

## Related

- [logic-build](../reference/logic-build.md#lint-floor) — the lint floor and its baseline.
- [build-flow](../reference/build-flow.md) — typecheck, lint and tests on the files a unit touched.
