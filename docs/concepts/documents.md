# Documents

An app repo keeps a small set of documents, and no skill requires any of them.

| File | Holds | Written by |
|---|---|---|
| `CLAUDE.md` | What is true of this app alone: locale, stack, ground truth, its own rules | `app-settle`; the [working rules](working-rules.md) come from the plugin, not from this file |
| `README.md` | What the app is, and how to run it | `app-settle` |
| `docs/README.md` | One sentence on the app, and a link to each document | `app-settle` |
| `docs/product.md` | Context, problem, success, non-goals, roles, prohibitions, and a features table: how a user reaches each feature, how a walk drives it, and what proves it worked | `app-settle`; a build session adds the row of each feature it builds |
| `docs/rules.md` | Each business rule under its own heading, with its `Why:` | `app-settle`, then any session that records a rule |
| `docs/queue.md` | Work owed, one line per page; a finished line is deleted | `app-settle` on a new app, `design-settle`, any session that queues work |
| `docs/changelog.md` | What changed in how the app behaves, newest first | Any session whose commit changes behaviour |
| `DESIGN.md` | The design system: tokens and the rules they cannot say | `design-settle` |

## None is required

A skill reads a file where it exists and runs where it does not:

- **No `DESIGN.md`** — a session building UI says so once, then builds from the tokens and components the repo already has.
- **No `docs/`** — a session building a page lists the work left in its closing report in place of a queue line.
- **No `docs/rules.md`** — a session that meets a business rule nobody recorded asks you for it.

A missing file is created only when the work at hand has something to put in it.

## Kept true in the same commit

A commit that makes a document false carries its correction, and a commit that changes how the app behaves carries its changelog line. No hook reminds a session of this: it is a line of the `docs-format` skill, and a session reports `Docs: none` with its reason when a commit changes no document.

## What stays out

Anything a live check can bring back: a list of tables or pages, a status, a description of the current state, a number measured today. The features table of `docs/product.md` is the one exception, because it holds what the code does not: how a user sees each feature and what proves it worked. A document holds what the code cannot say — the reason behind a rule, what must never be done, what the app is not for.

## Other files

- **A file already in `docs/`** stays and is kept true. No new kind of file is written unless you ask for it.
- **A root `PRD.md`** from an older version is read as it is, and moved only when you ask. See [Maintain app repos](../guide/maintain-app-repos.md).

## Related

- [docs-format](../reference/docs-format.md)
- [app-settle](../reference/app-settle.md)
