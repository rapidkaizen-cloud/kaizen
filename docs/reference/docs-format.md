# docs-format

Which documents an app repo keeps, what belongs in each, and what is never written because the code already says it.

| | |
|---|---|
| Kind | Skill — no command |
| Loads when | A session creates or edits `README.md`, `DESIGN.md` or a file under `docs/`, or a commit makes one of them false |
| Changes | The documents only |
| Source | `skills/docs-format/SKILL.md` |

## The files

`README.md`, `DESIGN.md`, and under `docs/`: `README.md`, `product.md`, `rules.md`, `queue.md`, `changelog.md`. [Documents](../concepts/documents.md) says what each holds and what writes it.

## What you will see

- **No list of what exists.** A session writes the criterion that decides membership, never the tables, pages or files themselves.
- **No status, no date, no "currently".** The documents read the same next year; dates live in `docs/changelog.md` only.
- **A `Why:` under every rule**, three sentences at most: the reason, the trade-off, when to revisit it. An unknown reason is written as unknown.
- **A proposal before a prohibition.** A session proposes a prohibition or a non-goal and waits for your answer; it never writes one on its own.
- **`Docs: none`** with its reason, in the report of a commit that changes no document.

## What you can rely on

- **A missing file is not an error.** One is created only when the work at hand has something to put in it.
- **A file already in `docs/` stays** and is kept true. No other kind of file is written unless you ask.
- **Code that deviates from a document is reported as a finding**, never used as a reason to edit the document.
- **An environment variable appears by its name, never its value.**

## What it does not cover

- **A reminder.** Nothing checks that a commit carried its document: the rule is a line of the skill.
- **Moving a root `PRD.md`.** It is read as it is, and moved only when you ask.

## Related

- [Documents](../concepts/documents.md)
- [app-settle](app-settle.md)
