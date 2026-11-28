# Start a new app

From an empty directory to the first page, in sessions you start yourself.

## Steps

1. **Open Claude Code in an empty directory and run `/kaizen:app-settle`.** It prints a short block: the mode — `Bootstrap` here — and what it found.
2. **Describe the app in your own words.** The session gives its reading in one paragraph and waits for your correction. It then asks about six themes: the problem, who uses the app and how they work today, what each role must finish, the business rules and the reason behind each number, the terms that are easy to misread, and what the app is not for. `none` is an answer.
3. **Answer one round about the stack**: platform, frontend, database with auth, hosting. Each comes with a recommendation and its trade-off, and `decide for me` takes it.
4. **Read the summary and say yes.** It lists each file and what it will hold, with every `[needs verification]` marked. Nothing is written before your yes.
5. **Let it write and commit.** `AGENTS.md`, a `CLAUDE.md` that loads it, `README.md`, and under `docs/`: `product.md`, `rules.md`, `changelog.md`, `queue.md` and `README.md`. It runs `git init` where the directory is no repo yet, commits once, and pushes nothing.
6. **Run `/kaizen:design-settle`** where the app has a UI. You pick between two frames of one page, and that page is built first. [Redesign the look](redesign.md) walks through the run.
7. **Ask for the next page**, by its line in `docs/queue.md`. A session builds one page, or one batch of pages of the same kind, and queues the rest.

> [!NOTE]
> `app-settle` writes documents, never code: it scaffolds nothing. The app's code starts with the session that builds the first page.

## Related

- [app-settle](../reference/app-settle.md)
- [Rules hook](../reference/rules-hook.md)
- [build-flow](../reference/build-flow.md) — how a page is built, and where a session stops.
- [Documents](../concepts/documents.md)
