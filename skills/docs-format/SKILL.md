---
name: docs-format
description: Rules for an app repo's documents — which files exist, what belongs in each, and what must never be written because the code or the database already says it. Use before creating or editing `README.md`, `DESIGN.md` or any file under `docs/`, and when a commit makes one of them false.
---

# docs-format — the documents of an app repo

Write for the developer or the agent who continues the app, in the user's language.

## The files

| File | Holds |
|---|---|
| `README.md` | what the app is, how to run it — environment variables by name |
| `docs/README.md` | one sentence on the app and a link to each file that exists; never the queue |
| `docs/product.md` | context, problem, success, non-goals, roles, prohibitions, features |
| `docs/rules.md` | each business rule under its own heading, with its `Why:` |
| `docs/queue.md` | work owed, one line each; a finished line is deleted, an empty file is deleted |
| `docs/changelog.md` | what changed in how the app behaves, newest first; an entry is never edited |
| `DESIGN.md` | the design system |

- **Write these and no other file unless the user asks for it.** A file already in `docs/` stays and is kept true.
- **A missing file is not an error**: create one only when the work at hand has something to put in it.
- **A root `PRD.md` in an older repo is read as it is**, and moved only on the user's request.

## What to write

- **Write only what a live check cannot recover.** Test: *deleted, could reading the repo or introspecting the database bring it back?* Yes → do not write it.
- **Code wins about what exists; the document wins about what ought to be.** Code that deviates from a document is a finding, never a reason to edit the document.
- **Replace each stale shape with what lasts**:

| Never write | Write instead |
|---|---|
| a list of what exists (tables, pages, files) | the criterion that decides membership |
| a status (`done`, `in progress`) | nothing |
| a description of the current state | the constraint that state must keep |
| a table, column or file name | the concept it stands for |
| a number measured today | only the reason behind a rule's value |
| how something came to be | the state it produced |

- **Name an environment variable, never its value.**
- **Write timelessly**: present tense, no `now`, `new`, `currently` or `previously`, and no date outside `docs/changelog.md`.

## Rules and prohibitions

- **Write a rule before its implementation.** Test: *a business decision, or a mechanism I just built?* Only the first is a rule.
- **Give each rule a `Why:` of three sentences at most**: the reason, the trade-off, the condition for revisiting it. An unknown reason is written `Why: unknown — it has always been this way`.
- **Propose a prohibition or a non-goal, then stop for the user's answer**: never write one on your own.
- **`DESIGN.md` derives user → `DESIGN.md` → styling files**: a value enters it only when the user ratified it.

## Features

The `## Features` table of `docs/product.md` is the one list of what exists a document keeps, routes and selectors included, because a walk and an unclear bug report start from it. One row per feature a user reaches:

| Column | Holds |
|---|---|
| `Feature` | its name as the user says it |
| `How a user reaches it` | the clicks from the start page, as the user sees them |
| `Drive` | the route, selector or shortcut a walk uses |
| `Proof` | the end state on screen that shows it worked |
| `Gotchas` | a precondition or trap a walk meets, or `none` |

- **A walk that cannot reach a row's `Proof` is a failure with its reason in `Gotchas`**, never a reason to weaken the row.

## The same commit

- **A commit that makes a document false carries its correction.**
- **A commit that changes how the app behaves carries its `docs/changelog.md` entry**, where the repo keeps that file.
- **A commit that changes no document says so in the report**: `Docs: none — <why>`.
