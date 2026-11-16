---
name: design-settle
description: Settles an app's visual direction in one session — a reading, one round of questions, two direction frames drawn as real pages for the user to pick on screen, then `DESIGN.md` and one proving page. Use only when the user asks to design, redesign or restyle an app, or to settle its design system.
---

# design-settle — direction, DESIGN.md, one proving page

One session settles the direction and proves it on one page. Every other page is later work, one page per session, built from `DESIGN.md`.

## Hard limits

- **Run only when the user asks for it.** A product with no UI → say the skill does not apply, and stop.
- **Rank sources user → code → documents.** Never write `DESIGN.md` from existing code: a finding becomes a line only once the user ratifies it.
- **Keeping everything as it is is a valid ending**: manufacture no change.
- **Nothing the user did not choose is silent**: each value you decide beyond the picked frame is one line with its basis, which the user can cancel. Decided by nobody → `[needs verification]`.
- **Frame files live only under `src/design-canvas/`.**
- **Never write a second design file**: no `MASTER.md`, no `design-system/` folder, no staging document.
- **A code-minimizing mode of the session governs how the code is written, never what the design holds.**
- **Commit once, at the close.** Never push, merge or open a pull request.

## Step 0 — read, print, read back

Read in one round: `CLAUDE.md`, `docs/README.md` and the files it links, `DESIGN.md`, the styling files, the listing of the component folder, the routes. A file that is absent is a row that says so, never a stop.

Print the block whole:

```
DESIGN-SETTLE
Skill build     : kaizen [version, from .claude-plugin/plugin.json two levels above this file]
Model           : [the model this session runs on, as the host names it]
Quota           : [the `used` lines of `claude -p "/usage" --strict-mcp-config`, on Claude Code] | not read — [host]
Documents       : [the files read] | none
DESIGN.md       : written | absent
UI components   : [count of component files]
Kind of app     : [...]
Platform        : [web | desktop | mobile]
Primary role    : [who uses it most]
Design material : [the design skills installed] | none
```

Then one sentence, and stop for correction before anything is asked or drawn:

*"I read this as [kind of app] on [platform] for [who uses it], leaning [the feel that fits], because [reason from the documents or the code]."*

## Step 1 — one round of questions

Ask in one round, two at most, and skip what the documents already answer:

- **Direction**: three named directions that fit the reading, one sentence each, plus `decide for me`. A tick is a leaning, never a specification.
- **Reference**: a real product whose look the user wants, or refuses.
- **What stays**: logo, brand colour, font, the component library in use.
- **Theme and widths**: light, dark or both; the desktop breakpoint and the lowest supported width.
- **Proving page**: the page the primary role uses most, unless the user names another.
- **Copy voice**: formal or casual, in the app's language.

- **No styling stack recorded → ask it in the same round**, recommending the frontend's own default.
- **A `DESIGN.md` already written → ask what must change.** What the user does not name stays.

## Step 2 — two frames

Draw the proving page twice, as `src/design-canvas/frame-a.html` and `frame-b.html`: each one file, self-contained, opened in a browser by its path.

- **Make the two differ in structure** — layout, navigation, density — never only in colour or font.
- **Fill them with the app's real content**: its labels, its roles, rows that could exist. No placeholder text.
- **Draw what the platform's own apps look like**: a desktop tool is a tool window, a mobile app a phone screen. Never a web dashboard unless the work is monitoring.
- **Make each frame hold at both widths of Step 1.**
- **Name every CSS variable as the token it will become.**
- **A design skill is installed (`impeccable`, `frontend-design`, `ui-ux-pro-max`) → read only its part for what you are drawing.** None is required, and none may write a file.

Give both paths with one line of rationale each, and stop: `A`, `B`, a mix, or neither.

- **A mix or a correction → apply it to the picked file and show it again**, until the user ratifies it.
- **Neither → ask what both miss, then draw one new pair.**
- **In an app that already has pages, say at this stop that the tokens reach every page at once**, while the layout changes only on the proving page.

## Step 3 — `DESIGN.md`

1. **Read the format live**: `npx -p @google/design.md designmd spec --rules`. Never from memory. The command fails → write by the order below and report `format not verified`.
2. **Write the tokens as YAML frontmatter**: `name`, `version`, `colors` (ramp steps and semantic aliases), `typography`, `rounded`, `spacing`, `components`. A token's name is the name the styling files use.
3. **Write the sections in this order, each heading once**:

| Section | Holds |
|---|---|
| `## Overview` | direction, signature, reference, copy voice, what is not used |
| `## Colors` · `## Typography` | the rules the tokens cannot say |
| `## Layout` | spacing base, desktop breakpoint, lowest supported width, density |
| `## Elevation & Depth` · `## Shapes` | as ratified |
| `## Components` | a table of component tokens; one icon family |
| `## Do's and Don'ts` | only what the user ratified |
| `## Page Composition` | the shell, the proving page by route, a table of page kinds |
| `## Contrast` | each pair against 4.5:1 for text and 3:1 for non-text |

4. **Tokens hold values, prose holds rules.**
5. **Print each value the picked frame does not show** — the other theme, focus ring, motion, the pairs of `## Contrast` — as one line with its basis. Carry on; a line the user cancels is corrected in one edit.
6. **Lint it**: `npx -p @google/design.md designmd lint DESIGN.md`, to zero errors. `orphaned-tokens` on a ramp step or an alias is expected.

## Step 4 — the proving page

- **Write the tokens into the styling files**, under the names `DESIGN.md` gives them.
- **Build or restyle only the shared components the proving page needs**, then the page itself.
- **Leave every other page's layout alone.**

## Step 5 — one check run

- **Use the dev server that is running, or start your own on a free port.** Never stop a process this session did not start.
- **Run from the app repo**: `node <plugin folder>/scripts/verify_pages.js --url <dev server> --widths <desktop>,<lowest> --out src/design-canvas/verify <page>=<route>` — the plugin folder is two levels above this file, and the screenshots land where Step 6 deletes them. A desktop build takes `--app <built .exe>` in place of `--url`.
- **Read only the rows marked `FAIL` or `n/v`.** Fix a `FAIL` on the proving page, and run once more.
- **Exit 3 means the repo has no Playwright**: report every check `not verified`, and install nothing.
- **Run the repo's lint command.**

## Step 6 — close

- **Delete `src/design-canvas/`.**
- **List the pages still on the old design**: as lines `- <page> — <role> — restyle to DESIGN.md` in `docs/queue.md` where the repo keeps `docs/`, in the report otherwise.
- **Commit once, naming the paths.**
- **Report**: what the user chose · each value you decided, with its basis · every `[needs verification]` · the check rows that are not `pass` · the pages left · the `Quota` line read again.
