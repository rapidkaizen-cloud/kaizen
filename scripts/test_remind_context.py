#!/usr/bin/env python3
"""Self-check remind_context.py as the hook on every message the user sends: when the
context note stays silent, what it says at a milestone, and that no message is ever held.

Every case exits 0; what differs is whether stdout carries the note.
Run directly: python3 test_remind_context.py
"""
import json
import subprocess
import tempfile
from pathlib import Path

HOOK = Path(__file__).parent / "remind_context.py"

# `python3`, not sys.executable: the interpreter name hooks.json invokes.
PYTHON = "python3"


def sent(transcript: str = "", raw: str = "") -> str:
    """The note the hook hands the session for a message, or an empty string."""
    payload = {"hook_event_name": "UserPromptSubmit", "prompt": "is it done?"}
    if transcript:
        payload["transcript_path"] = transcript
    result = subprocess.run([PYTHON, str(HOOK)], input=raw or json.dumps(payload), capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    if not result.stdout:
        return ""
    out = json.loads(result.stdout)
    assert "decision" not in out  # the hook reminds, it never holds a message
    assert out["hookSpecificOutput"]["hookEventName"] == "UserPromptSubmit"
    return out["hookSpecificOutput"]["additionalContext"]


def called(fresh: int, cached: int = 0, written: int = 0, **flags) -> dict:
    """An assistant entry as Claude Code writes it: the call's usage beside its content."""
    usage = {"input_tokens": fresh, "cache_read_input_tokens": cached, "cache_creation_input_tokens": written, "output_tokens": 900}
    return {"type": "assistant", "message": {"role": "assistant", "content": [], "usage": usage}, **flags}


def told(text: str) -> dict:
    """The entry the host writes when a hook hands the model text."""
    return {"type": "attachment", "attachment": {"type": "hook_additional_context", "content": [text], "hookEvent": "UserPromptSubmit"}}


def demo() -> None:
    with tempfile.TemporaryDirectory() as tmp:

        def transcript(*entries) -> str:
            path = Path(tmp) / f"t{len(list(Path(tmp).glob('t*.jsonl')))}.jsonl"
            path.write_text("\n".join(json.dumps(e) for e in entries) + "\nnot json\n", encoding="utf-8")
            return str(path)

        start = called(40, cached=60_000, written=14_000)  # 74k, as a session starts

        # silent first: no transcript, a missing one, a payload that is not JSON, a short session
        assert sent() == ""
        assert sent(str(Path(tmp) / "missing.jsonl")) == ""
        assert sent(raw="not json") == ""
        assert sent(raw="[]") == ""
        assert sent(transcript(start, called(40, cached=199_000))) == ""

        # the first message past a milestone: the size, and what it is against the start
        long = [start, called(900, cached=215_000, written=5_085)]
        said = sent(transcript(*long))
        assert said.startswith("CONTEXT CHECK - past 200k: this session's context holds 220k tokens")
        assert "about 3 times what its first call read" in said and "Make this a seam" in said
        assert "`docs/queue.md` line" in said and "costs about 3 times a new session's" in said

        # ... once: the host recorded the note, and the next message says nothing
        assert sent(transcript(*long, told(said), called(40, cached=260_000))) == ""
        # ... and again at the next milestone, whatever was skipped on the way
        further = sent(transcript(*long, told(said), called(40, cached=510_000)))
        assert further.startswith("CONTEXT CHECK - past 500k") and "510k" in further
        assert sent(transcript(start, called(40, cached=550_000))).startswith("CONTEXT CHECK - past 500k")
        assert sent(transcript(start, called(40, cached=900_000))).startswith("CONTEXT CHECK - past 800k")

        # a compaction shrinks the context, and it grows through a named milestone unsaid
        assert sent(transcript(*long, told(further), called(40, cached=90_000), called(40, cached=250_000))) == ""

        # the note quoted by the session, or written into a file, is not the note
        quoted = {"type": "assistant", "message": {"role": "assistant", "content": [{"type": "text", "text": said}]}}
        assert sent(transcript(*long, quoted)).startswith("CONTEXT CHECK - past 200k")

        # a subagent's calls and an entry the host wrote itself say nothing of the session
        assert sent(transcript(start, called(40, cached=400_000, isSidechain=True))) == ""
        assert sent(transcript(*long, called(0))).startswith("CONTEXT CHECK - past 200k")

        # a session that starts large is given the size without a ratio
        large = sent(transcript(called(40, cached=150_000), called(40, cached=210_000)))
        assert "times" not in large and "each call here re-reads all 210k" in large

        # a session left idle for hours is answered like any other: `sent` refuses a `decision`
        idle = {**called(40, cached=300_000), "timestamp": "2020-01-01T00:00:00.000Z"}
        assert sent(transcript(start, idle, told(said))) == ""
        assert sent(transcript(start, idle)).startswith("CONTEXT CHECK - past 200k")

    print("ok")


if __name__ == "__main__":
    demo()
