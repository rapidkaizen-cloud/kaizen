# norms-config

Writes or refreshes the ten working rules in a repo's `CLAUDE.md`.

| | |
|---|---|
| Kind | Skill — runs when you ask |
| Run | `/kaizen:norms-config` |
| Writes | `CLAUDE.md` at the repo root, and `AGENTS.md` where the repo already has one |
| Commits | The files it wrote, naming their paths. Never pushes |
| Source | `skills/norms-config/SKILL.md` |

## What it does

| It finds | It does |
|---|---|
| No `CLAUDE.md` | Creates it, holding only the block |
| A `CLAUDE.md` with no block | Appends the block at the end |
| A block from an older plugin version | Replaces it whole, markers included |
| A block of this version that differs | Shows the lines that differ and asks which to keep |
| An `AGENTS.md` at the root | Writes the same block there. It never creates the file |
| A folder you name for the files made for you | Adds one `Output` line holding it |

The block sits between `<!-- kaizen:rules <version> -->` and `<!-- /kaizen:rules -->`. [Working rules](../concepts/working-rules.md) lists its ten lines.

## What you can rely on

- **Nothing outside the markers is touched.**
- **A line you removed is not restored** without your answer.
- **No folder is asked for.** The `Output` line appears only when you name one.
- **No secret**: no key, no token, no URL that carries a credential.

> [!WARNING]
> A block from an older version is replaced whole, your edits inside it included. Keep a rule of your own outside the markers.

## What it does not cover

- **Enforcement.** The rules are text: a session follows them, and you can waive any of them in chat.
- **Other repos.** It writes into the repo it is run in. Run it once in each.
- **Switches.** There is none to set; a rule you do not want is a line you delete.

## Related

- [Working rules](../concepts/working-rules.md)
- [Maintain app repos](../guide/maintain-app-repos.md)
