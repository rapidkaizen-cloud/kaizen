# db-ops

The rules a session follows for any SQL against an app's database: look first, change by migration file, count before anything is destroyed.

| | |
|---|---|
| Kind | Skill — no command |
| Loads when | A session writes or runs SQL, a migration or an RLS policy, or anything that deletes, renames or rewrites rows |
| Changes | Migration files, in the folder and with the tool the repo already uses |
| Source | `skills/db-ops/SKILL.md` |

## What you will see

- **The live schema read first.** Before a change, the session reads the tables, columns, constraints and policies it touches, and shows the result as returned.
- **A migration file for every schema change.** Only a `SELECT`, and a role test that ends in `ROLLBACK`, are run directly.
- **One order**: migration, run, read the schema again, regenerate types, then the frontend.
- **Proof after every block.** A `SELECT` that shows the resulting state follows each one.

## A destructive operation

`DROP`, dropping a column, a rename, a change of type, `DELETE`, `TRUNCATE`, and an `UPDATE` with no narrow `WHERE`. The session counts the rows with the operation's own predicate, prints one block per operation, and stops:

```
DESTRUCTIVE
Operation  : [what]
Affected   : [the number counted]
Expected   : [how many should be deleted or changed]
Reversible : [yes/no — if no, what is lost for good]
```

You approve the number, not the intent. The operation then runs inside a block that aborts itself when the count is not the approved one, and the report gives the actual count against `Expected` with the integrity checks. An abort stops the session with the frontend untouched.

> [!WARNING]
> This stop is a rule the session follows, not a lock on the database. It stands where the migration is written, not where it runs: a deploy pipeline applies the files with no stop, and so does anyone with the credentials. Keep backups, and give a session a login that is not the owner where you can.

## RLS

A policy that exists is not a policy that works, and the default connection is the owner, which bypasses every policy. So each RLS change is tested as each role with a real user id of that role, inside a transaction that is rolled back — the role that must see nothing included. The report is one line per role: rows visible against rows expected. A mismatch stops the session.

## Indexes and keys

- **An index for every column a query filters, joins or sorts on**, in the same migration: several columns share one index, equality first; text search gets a trigram or full-text index; an indexed column is never wrapped in a function where the query filters.
- **A test that fails on a foreign key with no index**, kept in the repo and named in the `| Rule | Enforced by |` table of `CLAUDE.md`.
- **The columns an RLS policy filters on are indexed too**, and a per-user function in a policy runs once per query, not once per row.
- **A table that will grow large** gets a key that increases in order — never a random UUIDv4 — and a decision on how long its rows are kept.

Further reading, not required: `supabase-postgres-best-practices` in [supabase/agent-skills](https://github.com/supabase/agent-skills) (MIT).

## What it does not cover

- **Enforcement.** You can waive the stop for a session; the session tells you once what is no longer counted.
- **A database it cannot reach.** With no connection, nothing is read and the session says so.

## Related

- [Working rules](../concepts/working-rules.md)
- [logic-build](logic-build.md)
