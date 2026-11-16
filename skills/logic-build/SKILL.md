---
name: logic-build
description: Rules for the logic layer of an app — which key goes where, where a business rule is enforced, server handlers, errors, the data-layer folder and the test every rule leaves. Use before writing a query, an API handler, an environment variable, anything that holds a key, or code that enforces a business rule.
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

- **A need with no recorded choice — cache, validator, dates, where errors go, background jobs — is asked once, with a recommendation**, then recorded as a row of the Stack table in `CLAUDE.md`. A recorded `none` is a decision.
- **Keep a library's defaults until a recorded reason changes one.**
- **Extract a query or a rule the second time it appears.**
- **Regenerate types from the live schema after every schema change.** `as any` on a call the types lack is a finding.

## Data layer

- **Every database call lives in one folder, and nothing outside it holds the database client.** Split it by domain, never by page.
- **The folder is the `Data layer` row of the Stack table in `CLAUDE.md`.** No row → write the query beside the ones that exist.

## Rule test

- **Every rule implemented leaves one test whose title quotes the rule's name**, and a bug fix leaves the test that fails without it.
- **The test attacks the enforcement point**: a constraint, trigger or RPC → attempt the forbidden write as the bound role and expect the refusal, then the permitted one. A computation → call it with the rule's value, the value just inside and the value just outside.
- **Never mock the call under test, and never fix a failing rule test by editing the test.**
- **No test runner → raise it once**: install one now, or carry on unproven with a line `Prove: <rule>` where the repo keeps its owed work.
