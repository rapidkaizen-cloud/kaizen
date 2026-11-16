#!/usr/bin/env python3
"""Tell the session once that its context passed a milestone.

The plugin's only hook, on `UserPromptSubmit`, and it never refuses anything: it hands
the session one note, or stays silent. Claude Code only - its transcript carries each
call's token usage.

Every call re-reads the whole context, so a step costs what the context holds when it
runs. A session cannot read that size: told to advise a new session after every commit, it
did so in a session that had barely started. So this measures instead - the input side of
a call's usage is the context that call read - and speaks at the first message after a
milestone is passed, once per milestone, silent in between. The note makes that point a
seam, because a session told only the size carried on at it.
"""
import json
import re
import sys

# A fresh session starts near 80k, so at the first a call costs about two and a half
# times a fresh one's. The steps after it are the user's choice.
MILESTONES = (200_000, 500_000, 800_000)

# Opens the note, the milestone after it: what marks one as said.
MARK = "CONTEXT CHECK - past "
SAID = re.compile(re.escape(MARK) + r"(\d+)k")


def read(transcript: str) -> tuple:
    """The context the session's first call read, the context its last call read, and the
    highest milestone a note already named."""
    first = last = said = 0
    try:
        with open(transcript, encoding="utf-8", errors="replace") as f:
            for line in f:
                if '"usage"' not in line and MARK not in line:
                    continue
                try:
                    entry = json.loads(line)
                except ValueError:
                    continue
                # A subagent's calls read its own context, not the session's.
                if not isinstance(entry, dict) or entry.get("isSidechain"):
                    continue
                # Only where the host recorded this hook's output: the session quoting the
                # note, or a file holding these words, is not the note.
                if entry.get("type") == "attachment":
                    said = max([said, *(int(n) * 1000 for n in SAID.findall(line))])
                    continue
                message = entry.get("message")
                usage = message.get("usage") if isinstance(message, dict) else None
                if entry.get("type") != "assistant" or not isinstance(usage, dict):
                    continue
                size = sum(
                    usage.get(k) or 0
                    for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens")
                )
                if size:  # an entry the host wrote itself carries zeros
                    first, last = first or size, size
    except (OSError, TypeError):
        return 0, 0, 0
    return first, last, said


def milestone(first: int, last: int, said: int) -> str:
    """The note for the milestone `last` just passed, or an empty string."""
    passed = max((m for m in MILESTONES if last >= m), default=0)
    # A milestone below one already named stays silent: after a compaction the context
    # grows through the same numbers again, and the user was told at the higher one.
    if passed <= said:
        return ""
    many = last >= 2 * first
    against = f", about {last / first:.0f} times what its first call read" if many else ""
    price = (
        f"each call here costs about {last / first:.0f} times a new session's"
        if many
        else f"each call here re-reads all {last // 1000}k"
    )
    return (
        f"{MARK}{passed // 1000}k: this session's context holds {last // 1000}k tokens"
        f"{against}, and every call re-reads all of it. "
        "Make this a seam: write where the work stands where a new session will read it - a "
        "`docs/queue.md` line where the repo keeps that file, else your closing line - then end "
        "the turn at the next point the work can be left, never mid-edit. Tell the user in one "
        f"line: that size, that {price}, and that a reply here continues at that price. Say it "
        "once: this note returns at the next milestone."
    )


def main() -> None:
    # As bytes: on Windows stdin decodes as the ANSI codepage, and a path outside it breaks.
    try:
        payload = json.loads(sys.stdin.buffer.read().decode("utf-8-sig", errors="replace"))
    except ValueError:
        payload = {}
    transcript = payload.get("transcript_path") if isinstance(payload, dict) else ""
    if text := milestone(*read(str(transcript or ""))):
        json.dump({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": text}}, sys.stdout)
    sys.exit(0)


if __name__ == "__main__":
    main()
