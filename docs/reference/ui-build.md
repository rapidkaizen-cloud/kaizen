# ui-build

The rules a session builds UI by: where a component comes from, its states, and how on-screen text is written.

| | |
|---|---|
| Kind | Skill — no command |
| Loads when | A session creates or edits a component, touches a styling value, or writes on-screen text |
| Reads | `DESIGN.md`, the shared component folder, an installed design skill for the part at hand, `modern-web-guidance` in a web app |
| Source | `skills/ui-build/SKILL.md` |

## What you will see

- **An existing component named for each element** before anything is built. A new one comes only when nothing fits, with what fails said — looking slightly different is not a reason.
- **Three states with every component**: a skeleton while loading, an empty state that says why and what to do next, a failure with its cause and a retry.
- **Short text.** Two words for an action, three for a name, one sentence of eight words for an explanation; one term per concept; a button that starts with a verb.
- **The lint command run** before the commit.

## Without a `DESIGN.md`

The session says so once, then builds from the tokens and components the repo already has, and writes no new styling value. A repo with no UI yet takes its values from you.

## Design skills

Where `impeccable`, `frontend-design` or `ui-ux-pro-max` is installed, the session reads only the part for the component at hand. None is required.

## Web guidance

Where `modern-web-guidance` is installed and the app is a web app, the session follows its guide for how a new component, or client-side CSS or JS, uses a browser feature — never to replace a component your repo or its library has, and never against `DESIGN.md`. It is not required: see [Install](../start/install.md#recommended-for-a-web-app).

## What it does not cover

- **Existing copy that breaks a rule.** It is reported as a finding, never rewritten inside other work.
- **The design itself.** `DESIGN.md` wins over every other source of taste, and [design-settle](design-settle.md) writes it.

The writing rules are adapted from the `better-writing` skill of [jakubkrehel/skills](https://github.com/jakubkrehel/skills) (MIT).

## Related

- [design-settle](design-settle.md)
- [build-flow](build-flow.md)
