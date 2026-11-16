# design-settle

One session that settles an app's visual direction: two frames to pick from, then `DESIGN.md` and one proving page.

| | |
|---|---|
| Kind | Skill — runs only when you ask |
| Run | `/kaizn:design-settle` |
| Reads | `CLAUDE.md`, `docs/`, `DESIGN.md`, the styling files, the component folder, the routes |
| Writes | `DESIGN.md`, the styling files, the proving page and the shared components it needs, lines in `docs/queue.md` |
| Works in | `src/design-canvas/` — the frames and the check's screenshots, deleted at the close |
| Commits | Once, at the close. Never pushes, merges or opens a pull request |
| Source | `skills/design-settle/SKILL.md`, `scripts/verify_pages.js`, `scripts/audit_measure.js` |
| Self-check | `node scripts/verify_pages.js --selftest`, `python3 scripts/test_verify_pages.py`, `python3 scripts/test_audit_measure.py` |

## The block

Printed first, before anything is asked:

| Row | Holds |
|---|---|
| `Skill build` | The plugin version this session runs |
| `Model` | The model the session runs on |
| `Quota` | The `used` lines of `claude -p "/usage"`, on Claude Code; `not read` elsewhere. Read again at the close |
| `Documents`, `DESIGN.md`, `UI components` | What the repo holds. An absent file is a row that says so, never a stop |
| `Kind of app`, `Platform`, `Primary role` | The session's reading |
| `Design material` | The design skills installed, or `none` |

## Where it stops

1. **After its reading**, one sentence, for your correction.
2. **At the one round of questions**, two at most. What the documents already answer is not asked.
3. **At the two frames**: `A`, `B`, a mix, or neither. A mix is applied and shown again until you ratify it; `neither` gets one new pair.

It does not stop while it writes `DESIGN.md`: each value the picked frame does not show is printed as one line with its basis, and a line you cancel is corrected in one edit.

## The frames

Two files, `frame-a.html` and `frame-b.html`, each opened in a browser by its path. They draw the proving page — the page the primary role uses most, unless you name another — with the app's real labels and rows, at both widths, as the platform's own apps look. They differ in structure: layout, navigation, density.

## The check

One run of `verify_pages.js` on the proving page, at the desktop breakpoint and the lowest supported width:

| Check | Fails on |
|---|---|
| `errors` | A console error or a page error |
| `fonts` | A font that failed to load |
| `axe` | A serious or critical accessibility violation |
| `contrast` | A text or non-text pair under its contrast floor |
| `motion` | An animation or a transition that still runs with reduced motion on |
| `overflow` | Horizontal overflow |

The script runs your installed Chrome headless on a temporary profile, and takes Playwright from the app repo's own `node_modules`. Where the repo has none, every check is reported `not verified` and nothing is installed. A desktop build is checked through its own `.exe`.

## What you can rely on

- **`DESIGN.md` holds only what you chose or let stand.** A value decided by nobody is `[needs verification]`.
- **It is never written from the existing code.**
- **Keeping everything as it is is a valid ending.**
- **One design file.** No second document, no staging folder.
- **No process the session did not start is stopped.**

## What it does not cover

- **The other pages.** Their layout is untouched; they are listed in `docs/queue.md` — in the report where the repo keeps no `docs/` — and restyled one per session.
- **An audit of the app as it is.**
- **A design skill.** `impeccable`, `frontend-design` and `ui-ux-pro-max` are read where installed; none is required, and none may write a file.

> [!WARNING]
> In an app that already has pages, the tokens reach every page the moment the styling files are written. The session says so at the frames.

## Related

- [Redesign the look](../guide/redesign.md)
- [Run on a Pro plan](../guide/pro-plan.md)
- [ui-build](ui-build.md)
