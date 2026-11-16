---
name: app-settle
description: Settles what an app is before it is built or continued — a short interview about the problem, the roles and the business rules, then the repo's `CLAUDE.md` and its core documents. Bootstrap mode for a new repo, Document mode for an app that already exists. Use only when the user asks to settle, bootstrap, set up or document an app.
---

# app-settle — what the app is, written down

## Hard limits

- **Run only when the user asks for it.**
- **Write only the files of Step 4.**
- **Do not invent**: an answer nobody gave is written `[needs verification]`.
- **No secret goes into any file and no token is asked for**: name the variable, never its value.
- **Print the summary of Step 3 and stop for an explicit yes before writing anything.**
- **Install no dependency and run no generator without that yes.**
- **Document mode changes nothing about the app**: no code, no schema, no config.

## Step 0 — which mode

Read the repo root, `CLAUDE.md`, `README.md`, everything under `docs/`, and the stack's manifest. Print the block whole:

```
APP-SETTLE
Mode      : Bootstrap — no app code yet | Document — an app exists
Stack     : [each item as found, with the file that says so] | none yet
Documents : [the files found] | none
CLAUDE.md : present | absent
```

- **Read the documents that exist before asking anything**, and ask only what they leave open.
- **Never rewrite a line of an existing document without the user's word.**

## Step 1 — the interview

1. **Open with one free invitation**: the app in the user's own words.
2. **Give your reading in one paragraph and stop for correction.**
   - Bootstrap: *"I read this as [problem] experienced by [who], currently handled by [the old way], with this app replacing [which part]."*
   - Document: *"I read this as [problem] experienced by [who], previously handled by [the old way], with this app now covering [which part]."*
3. **Cover six themes**: the real problem · who uses it and how they work today · the work each role must finish and its limits · the business rules and the reason behind each number · domain terms that are easy to misread · non-goals.

- **Summarize each theme back, then ask its gaps in one batch.**
- **Ask a domain question open**, with no options. `none` is an answer.
- **Never ask for a table, a screen or a folder name.**
- **Never skip the reason behind a number.** "It has always been that way" is written as said.
- **Stop asking when the six are answered.**

## Step 2 — the stack

- **Document → record the stack as found**, each row naming the file it was read from. Ask nothing.
- **Bootstrap → ask one round**: platform, frontend, database with auth, hosting. Give each one recommendation and its trade-off; `decide for me` takes it and is reported as a default.
- **Leave every other choice to the session that first needs it.**

## Step 3 — the summary

Print each file of Step 4 with what it will hold, mark every `[needs verification]`, then stop for the yes.

## Step 4 — the files

Write `CLAUDE.md` in English and the rest in the user's language. A file that exists gets only what it lacks.

**`CLAUDE.md`** — one opening line saying it holds what is true of this app alone, then:

| Section | Holds |
|---|---|
| `## Locale` | on screen · in the code · dates · numbers |
| `## Stack` | a table, one row per answer of Step 2, plus a `Data layer` row naming the one folder that holds database calls |
| `## Ground truth` | code and the live database for facts; `docs/` for intent and prohibitions; `DESIGN.md` for the design system |
| `## Rules for this app only` | empty at Bootstrap |

Leave everything else in an existing `CLAUDE.md` as it is, a block between `<!-- kaizen:rules` markers included.

**`docs/product.md`** — `# Product — <App name>`, then:

| Section | Holds |
|---|---|
| `## Context` | surface (platform, who uses it, where) · data · deploy |
| `## Problem` | two or three sentences: the state before the app and why it could not stay |
| `## Success` | one or two sentences |
| `## Non-goals` | one line each, with why |
| `## Roles` | a table `Role · Must be able to · Must not`, and one sentence on a user whose role is empty or unknown |
| `## Prohibitions` | what a later session would "fix" in good faith: the principle and its reason. Near-empty at Bootstrap is correct |

**`docs/rules.md`** — `# Rules` → `## <Group>` → `### <Topic>`, the rule in explicit sentences, then `Why: <reason · trade-off · condition for revisiting>` in three sentences at most. No numbering: the topic heading is the rule's name.

**`docs/changelog.md`** — `# Changelog` → `## YYYY-MM-DD` → one line per change in how the app behaves, newest first. Bootstrap writes the heading only.

**`docs/queue.md`** — Bootstrap only: one line per page the interview named, `- <page> — <role> — <the work that can be finished there>`.

**`docs/README.md`** — `# <App name>`, one sentence on what the app is for, and a link to each file that exists. Never the queue.

**`README.md`** — `# <App name>`, two or three sentences from Problem and Success, `## Run` with the command and the environment variables it needs by name, `## Documents` linking `docs/README.md`.

## Step 5 — close

- **Bootstrap with no git repo → `git init` on branch `main`.**
- **Commit once, naming the paths written.** Never push.
- **Report**: the files written, each `[needs verification]`, each default taken, and what the user must do by hand.
