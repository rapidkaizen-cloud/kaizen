---
name: logic-build
description: Rules for the logic layer of an app — which key goes where, where a business rule is enforced, server handlers, errors, the data-layer folder, the test every rule leaves and the check a correction becomes. Use before writing a query, an API handler, an environment variable, anything that holds a key, code that enforces a business rule, or a lint, type or test that makes a mistake the user corrected impossible.
---

# logic-build — keys, rules, queries

## Keys

| Key | Lives | Protection |
|---|---|---|
| anon / publishable | the client | RLS is its only protection |
| `service_role` / secret | the server only | bypasses RLS entirely |

- **Never put `service_role` in client code**: it does not weaken RLS, it removes it.
- **Before writing an environment variable, ask "can whoever holds the client read this?"** `VITE_*`, `NEXT_PUBLIC_*` and `PUBLIC_*` ship to every visitor, and a build freezes the value in.
- **A secret already committed is a stop**: report it, name the variable, and tell the user to rotate it first.
- **Write a key by its variable name, never its value**, in a document, a commit or a report.

## One rule, one place

| Kind of rule | Enforced in |
|---|---|
| Access | RLS, always |
| Uniqueness | a unique constraint, always |
| Allowed status transitions | a transitions table or a trigger in the database, always |
| Computation, workflow | one named place |

- **Client code is convenience only**: name a check that repeats a server rule as a mirror, in the code.
- **A business rule the repo's `docs/rules.md` does not hold is a stop**: ask, never invent it. A repo with no such file → ask the user for the rule and build from the answer.
- **No server layer → enforce in the database**: an RLS policy; `CHECK`, `NOT NULL` or a foreign key; a trigger or an RPC.
- **`SECURITY DEFINER` only with a named reason**, a narrow body, and a test as each role.
- **A need for a real secret is a need for a server surface**: raise it as a stack change, never work around it in the client.

## Server handlers

- **Parse the input at the handler's entry and reject what does not fit.**
- **Every handler authorizes itself**, with the user's token by preference. Use `service_role` only where the operation must exceed the user's rights, and write the why beside it.
- **A write of several statements runs in one transaction or one RPC.**

## Errors and reads

- **The user gets a sentence they can act on; the log gets the detail.** Raw database text never reaches the screen.
- **Never swallow an error**: a call that returns its error is read at the call site.
- **Page every list read wherever the API caps rows.**

## Libraries and reuse

- **A need with no recorded choice — cache, validator, dates, where errors go, background jobs, property-based tests, the lint floor — is asked once, with a recommendation**, then recorded as a row of the Stack table in `CLAUDE.md`. A recorded `none` is a decision.
- **Keep a library's defaults until a recorded reason changes one.**
- **Before writing a query, a handler or error handling, find how the repo already does it and do it that way**; a second way is a finding in the closing report, never new code.
- **Extract a query or a rule the second time it appears.**
- **Regenerate types from the live schema after every schema change.** `as any` on a call the types lack is a finding.

## Lint floor

- **The floor is the linter's own rules, set to error, for unused imports and variables, an explicit `any` or its counterpart, a leftover console or debugger call, and function size at the limit recorded with it.**
- **Freeze the hits already in the repo in the linter's own baseline file**, never by lowering a rule to a warning or turning it off; new code passes the floor.
- **Never add to the baseline; a cleanup removes the entries it fixed.**

## Data layer

- **Every database call lives in one folder, and nothing outside it holds the database client.** Split it by domain, never by page.
- **The folder is the `Data layer` row of the Stack table in `CLAUDE.md`.** No row → write the query beside the ones that exist.

## Rule test

- **Every rule implemented leaves one test whose title quotes the rule's name**, and a bug fix leaves the test that fails without it.
- **Where `CLAUDE.md` keeps a `Rule | Enforced by` table, name a bug fix's test in the row of the mistake it fixed.**
- **The test attacks the enforcement point**: a constraint, trigger or RPC → attempt the forbidden write, a forbidden status transition included, as the bound role and expect the refusal, then the permitted one. A computation → call it with the rule's value, the value just inside and the value just outside.
- **A rule that computes money, stock or pay also gets a property-based test that checks its invariant over generated input** — a total always equals the sum of its lines — with fast-check in TypeScript or its counterpart in the stack.
- **Never mock the call under test, and never fix a failing rule test by editing the test.**
- **No test runner → raise it once**: install one now, or carry on unproven with a line `Prove: <rule>` where the repo keeps its owed work.

## Checks from corrections

- **Keep the `| Rule | Enforced by |` table under `## Rules for this app only` in the app's `CLAUDE.md`**, because a refresh of the working-rules block replaces everything inside it.
- **Where the pattern is already common, fail a new check only on new additions.**
- **Prove a new check fails on the old mistake before keeping it.**
- **Allow an exception only on the offending line itself, with its reason, an expiry date and the user's yes.**
- **A prose rule broken again moves up one level in the same change.**
- **Delete a table row once its mistake cannot happen.**
