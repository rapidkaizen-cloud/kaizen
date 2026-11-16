# Bring in an existing app

Give an app that already runs the working rules and, where it has none, its documents — without changing the app.

## Steps

1. **Open Claude Code in the repo and run `/kaizn:norms-config`.** It appends the working rules to `CLAUDE.md`, or creates the file holding only them, and commits. Text outside the block is left as it is.
2. **Run `/kaizn:app-settle` where the repo has no documents.** It finds app code and names the mode `Document`.
3. **Describe the app, then correct the session's reading.** It reads what the repo already says first and asks only what that leaves open, over the same six themes as on a [new app](new-app.md).
4. **Let it record the stack as found.** Each row names the file it was read from; nothing is asked.
5. **Read the summary and say yes.** A file that exists gets only what it lacks, and no line of an existing document is rewritten without your word.
6. **Run `/kaizn:design-settle` only when you want the look settled or changed.** Keeping everything as it is is a valid ending of that run. See [Redesign the look](redesign.md).

## What this does not do

- **No audit.** Nothing compares the code to the documents or lists what deviates.
- **No migration.** A root `PRD.md` and other documents from an older version stay where they are: see [Maintain app repos](maintain-app-repos.md).
- **No change to the app.** `Document` mode touches no code, schema or config.

## Related

- [app-settle](../reference/app-settle.md)
- [norms-config](../reference/norms-config.md)
- [Working rules](../concepts/working-rules.md)
