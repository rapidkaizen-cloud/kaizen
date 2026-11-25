# How it works

`kaizen` puts text in front of a session at two moments, and enforces none of it.

## What loads when

| When | What the session gets | From |
|---|---|---|
| A session starts | The repo's `CLAUDE.md` | The repo; the host reads it |
| A session or subagent starts | The [working rules](working-rules.md) | The plugin's [hook](../reference/rules-hook.md) |
| A session starts | The plugin's skills in the host's skill list | The plugin |
| The work matches a skill, or you run its command | That skill's one file | The plugin |

Beyond the working rules the plugin prints nothing when a session starts, and a skill that never loads costs its line in the skill list and nothing more.

## Every skill stands alone

A skill reads `CLAUDE.md`, `docs/` and `DESIGN.md` where the repo has them, and runs where it does not: the page a skill would have read simply binds nothing. No skill sends the session to another, so the order is yours. [Quickstart](../start/quickstart.md) gives one that suits a new app.

## Why nothing is enforced

Until 1.0.0 the plugin shipped hooks that refused a command: a push, a destructive statement, a file written to the wrong folder. A hook cannot ask: it can only refuse, the case that should have passed included, and each refusal costs one more call. The rules are now text, and you can waive any of them in chat. The context reminder, the last of those hooks, was removed in 1.1.0: watch a session's size with `/context` and the quota with `/usage`. The one hook since 1.6.0 prints the working rules and refuses nothing.

What that costs you:

- **A session that skips a line is stopped by nothing.** The plugin has no second check behind the text.
- **A push and a destructive statement are held by a sentence**, the `Git` and `Data` lines of the working rules. A session that reads them stops and waits; nothing refuses the command if it does not.
- **A machine without the plugin gets no rules.** The rules live in the plugin, not in the repo.

For an app that runs in production, keep the protections that do not depend on a session: branch protection on the remote, backups of the database, and a database login with less than owner rights for everyday work.

## Related

- [Working rules](working-rules.md) — the ten lines, and how to waive or change one.
- [Documents](documents.md) — the files a skill reads where they exist.
- [What is proven](../reference/status.md) — what has run for real since the rebuild.
