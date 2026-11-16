---
name: db-ops
description: Rules for any SQL against the app's database — introspect before DDL, migrations as files, the four phases of a destructive operation, and the RLS role test. Use before writing or running SQL, a migration or an RLS policy, and before anything that deletes, renames or rewrites rows.
---

# db-ops — SQL against a live database

Schema has git through migration files; data does not. A revert does not bring back a deleted row.

## Every schema change

- **Introspect before writing DDL**: read the tables, columns, constraints and policies the change touches from the live database, and show the result as returned.
- **Write every schema change as a migration file**, in the folder and with the tool the repo already uses. Run directly only a `SELECT` and a role test that ends in `ROLLBACK`.
- **Keep this order**: `migration → run → introspect AFTER → regenerate types → frontend`.
- **A step is one command up to its next stop**: read several objects in one `SELECT` (`json_build_object`, `UNION ALL`).
- **Follow every `DO $$` block with a `SELECT` that proves the state**: the block returns no rows, and `RAISE NOTICE` is not output.
- **A new table gets RLS enabled and its policy in the same migration.**

## A destructive operation

Destructive: `DROP` · `ALTER ... DROP COLUMN` · a rename · `ALTER TYPE` that changes the type · `DELETE` · `TRUNCATE` · `UPDATE` without a narrow `WHERE`.

The gate stands where the migration is written, not where it runs: a pipeline applies the files with no gate, so never tell the user the database is protected.

**Phase 1 — count.** Run `SELECT COUNT(*)` with the operation's own predicate, and state how many rows should be affected.

**Phase 2 — gate.** Print one block per operation, then stop. Several operations share one stop.

```
DESTRUCTIVE
Operation  : [what]
Affected   : [real number from SELECT COUNT — not an estimate]
Expected   : [how many should be deleted/changed — becomes the guard]
Reversible : [yes/no — if no, name what is lost permanently]
```

The user approves the number, not the intent. A user who waives the gate for the session is told once what is no longer counted.

**Phase 3 — guarded execution.** The operation aborts itself when the count is not the approved one. Operations approved at one stop run in one `DO` block.

```sql
DO $$
DECLARE n int;
BEGIN
  DELETE FROM <table> WHERE <predicate>;
  GET DIAGNOSTICS n = ROW_COUNT;
  IF n <> <Expected> THEN
    RAISE EXCEPTION 'Expected <Expected> rows, actual %. Aborted.', n;
  END IF;
END $$;
SELECT <query proving the resulting state>;
```

A change of structure checks before the operation, inside the same block:

```sql
DO $$
DECLARE n int;
BEGIN
  SELECT count(*) INTO n FROM <table> WHERE <column> IS NOT NULL;
  IF n <> <Expected> THEN
    RAISE EXCEPTION 'Expected <Expected> rows affected, actual %. Aborted.', n;
  END IF;
  ALTER TABLE <table> DROP COLUMN <column>;
END $$;
SELECT <query proving the resulting state>;
```

**Phase 4 — report.** Give the actual count against `Expected`, the `SELECT` output as returned, and the integrity checks: orphaned foreign keys, `NOT NULL` violated, failed casts. An abort or a failed check → stop entirely and leave the frontend untouched.

## RLS

RLS fails silently, and the default connection is the owner, which bypasses it. `qual` and `with_check` prove that a policy exists, never that it works.

- **Test every RLS change as each role**, with a real user id of that role:

```sql
BEGIN;
  SELECT set_config('request.jwt.claims',
    '{"sub":"<uuid of a user with this role>","role":"authenticated"}', true);
  SET LOCAL ROLE authenticated;
  SELECT <query representing this role's real access>;
ROLLBACK;
```

- **Test the role that must see zero rows too.**
- **Report per role**: role · user id · rows visible · rows expected · match. A mismatch → stop.
- **No user holds a role the test needs → seed one login directly by SQL, never in a migration**, with credentials from the session's own instructions and written into no file of the repo.
- **Qualify every column name that two tables in a policy share.**
- **Copy a predicate that must match an existing one from the introspection**, never retype it.
