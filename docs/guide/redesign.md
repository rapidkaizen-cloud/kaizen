# Redesign the look

One `design-settle` session settles the direction and proves it on one page; every other page follows later, one per session.

## Before you start

- **A dev server the session can reach**, or let it start its own on a free port. It never stops a process it did not start.
- **On a Pro plan**, read [Run on a Pro plan](pro-plan.md) first.
- **Design skills are optional.** Where `impeccable`, `frontend-design` or `ui-ux-pro-max` is installed, the session reads the part it needs; none is required. See [Install](../start/install.md).

## Steps

1. **Run `/kaizn:design-settle`.** It reads the repo and prints a block: the build, the model, the quota, the documents and components it found. Then it gives its reading of the app in one sentence. Correct it before anything is asked or drawn.
2. **Answer one round of questions**, two at most: a direction out of three named ones or `decide for me`, a reference product, what stays (logo, brand colour, font, component library), theme and widths, the proving page, the copy voice. What your documents already answer is not asked. Where a `DESIGN.md` exists, the question is what must change, and the rest stays.
3. **Open the two frames.** The session draws the proving page twice, as two files you open in a browser. They differ in structure, never only in colour, and hold your app's real content.
4. **Pick `A`, `B`, a mix, or neither.** A mix or a correction is applied and shown again until you ratify it; `neither` gets one new pair.
5. **Read the lines it decided for you.** While it writes `DESIGN.md`, each value the picked frame does not show — the other theme, the focus ring, motion, the contrast pairs — is printed as one line with its basis. Cancel any of them in chat.
6. **Let it build the proving page.** The tokens go into the styling files, and that one page is built or restyled with the shared components it needs.
7. **Read the check rows.** One script run measures the proving page at both widths: console errors, fonts, accessibility, contrast, motion, overflow. You see only the rows that failed or could not be verified.
8. **Read the close.** The frames are deleted, the pages still on the old design are listed in `docs/queue.md`, and everything is committed once. Nothing is pushed.
9. **Restyle the pages left, one per session**: ask for one by its queue line.

> [!WARNING]
> In an app that already has pages, the tokens reach every page at once: colour, type and spacing change everywhere the moment the styling files are written, while the layout changes only on the proving page. The session says so before you pick.

## Related

- [design-settle](../reference/design-settle.md) — every stop, and what the check covers.
- [ui-build](../reference/ui-build.md) — the rules a later page is built by.
- [What is proven](../reference/status.md) — this flow has not yet run in a real app.
