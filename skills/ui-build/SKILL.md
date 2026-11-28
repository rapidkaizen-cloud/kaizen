---
name: ui-build
description: Rules for building or changing any UI — where a component comes from, the loading, empty and failed states, inputs that write, and how on-screen text is written. Use before creating or editing a component, touching a styling value, or writing any user-facing text.
---

# ui-build — components, states, copy

## Read first

- **Read `DESIGN.md` before any component.** It wins over every other source of taste.
- **No `DESIGN.md` → say so once, then build from the tokens and components the repo already has**, and write no new styling value. A repo with no UI yet takes its values from the user.
- **A line of it marked `[needs verification]` → take the value from an existing component**, and name it at the close.
- **A design skill is installed (`impeccable`, `frontend-design`, `ui-ux-pro-max`) → read only its part for the component at hand.** None is required.
- **`modern-web-guidance` is installed and the app is a web app → follow its guide for how a new component, or client-side CSS or JS, uses a browser feature**; it never replaces a component the repo or its library has, and never overrules `DESIGN.md`. It is not required.
- **Read the shared component folder itself**, never a search for it.

## Where a component comes from

Before building, name the existing component that covers each element. Take the first source that fits:

1. **A component already in the repo.**
2. **The installed component library**: list its component directory before deciding it lacks something.
3. **A new component, only when nothing fits**: say what fails — looking slightly different is not a reason — follow the library's idiom, and say in its header which rule it holds.

- **Before writing a form, screen state or a fetch on a page, find how the repo already does it and do it that way**; a second way is a finding in the closing report, never new code.
- **Extract a visual pattern the second time it appears**, and add it to the design-system route where the repo has one.
- **Put every on-screen string in the one dictionary file** where the repo has one.

## States

Write these with the component, never after it.

- **Loading**: a skeleton of the result's shape and size; a spinner only for work with no shape.
- **Empty**: why it is empty and what to do next, ending on the one action. A filtered list names the query and offers the exit: `No results for "quarterly". Clear filters`.
- **Failed**: the message beside its cause, with a retry. It never disappears on its own.
- **Never park lasting information in an empty state.**

## Inputs that write

- **A date field writes only a complete, valid date.**
- **A paid or slow call fires on an explicit action**, never on blur or a keystroke.

## Performance

- **Lazy-load a route and a heavy library, import only the parts used, and load a third-party script after the page is interactive.**
- **Keep a bundle size budget that fails the build**, asked once and recorded in the Stack table of `AGENTS.md`.
- **Serve an image at its displayed size in WebP or AVIF, always with width and height**: lazy below the fold, the hero eager at high priority.
- **Paginate or virtualize a long list.**
- **Stop every interval, listener, subscription and poll on unmount**, pause polling while the tab is hidden, and move CPU-heavy work to a worker.

## Writing

Count words in the app's language.

| Kind | Where | Cap |
|---|---|---|
| Action | button, link, menu, tab | 2 words |
| Name | label, column header, badge, heading | 3 words |
| Explanation | helper, empty and error state, tooltip, toast, subtitle | 1 sentence, 8 words |

The body of a destructive confirmation may run two sentences.

- **One term per concept**, in the voice `DESIGN.md` records — neutral where it records none.
- **Address the reader as "you".**
- **Never assemble a sentence from fragments around a variable.**
- **A button label starts with a verb**, and a confirmation button repeats the consequence: `Delete project` / `Cancel`.
- **Link text names its destination.**
- **Sentence case everywhere.**
- **Label a toggle for its ON state.**
- **A placeholder is an example, never the label.**
- **Never write a state the screen already shows.**
- **An error is an instruction beside its field, phrased positively**: `Choose a password with at least 8 characters`, `Unable to save. Check your connection and try again.` No blame, no `Oops`, no exclamation mark.
- **Existing copy that breaks a rule is a finding**, never rewritten inside other work.

The writing rules are adapted from the `better-writing` skill of [jakubkrehel/skills](https://github.com/jakubkrehel/skills) (MIT).

## Before committing

- **Run the repo's typecheck and lint on the files you touched** and fix what they report, reading only the failures.
