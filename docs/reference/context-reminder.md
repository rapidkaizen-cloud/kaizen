# Context reminder

A note handed to the session once its context passes 200k, 500k and 800k tokens — the only hook the plugin ships, and it never refuses anything.

| | |
|---|---|
| Kind | Hook — hands the session a note, or stays silent |
| Runs on | `UserPromptSubmit`, on Claude Code only |
| Reads | The session's transcript: the token usage of each call |
| Changes | Nothing |
| Source | `scripts/remind_context.py` |
| Self-check | `python3 scripts/test_remind_context.py` |

## Why it exists

Every call re-reads the whole context, so a step costs what the context holds when it runs. A session cannot read that size itself, so the hook measures it: the input side of a call's usage is the context that call read.

## What you will see

At your first message after a milestone is passed, the session gets a note that opens `CONTEXT CHECK - past 200k:`. It tells the session to:

1. Write where the work stands where a new session will read it — a `docs/queue.md` line where the repo keeps that file, else its closing line.
2. End the turn at the next point the work can be left, never mid-edit.
3. Tell you in one line: the size, what each call now costs against a new session's, and that a reply continues at that price.

You decide whether to carry on. Nothing is held: a reply in the same session continues the work.

## When it stays silent

- **Under 200k.**
- **A milestone already named**, until the next one.
- **A milestone below one already named.** After a compaction the context grows through the same numbers again, and you were told at the higher one.
- **A transcript it cannot read**, or one with no usage in it.

## What it does not cover

- **A subagent's context.** Only the session's own calls are counted.
- **Your plan's quota or the window's percentage.** It reports tokens held, not what is left.
- **Antigravity.** No hook ships there.
- **A switch.** There is none; the note costs one line at three points of a long session.

## Related

- [Run on a Pro plan](../guide/pro-plan.md)
- [How it works](../concepts/how-it-works.md)
