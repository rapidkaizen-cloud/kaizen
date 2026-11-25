#!/usr/bin/env python3
"""Self-check rules.js and both hooks.json files: the rules are printed in every project,
whatever its CLAUDE.md holds, once per conversation on Antigravity, and nothing is printed,
with exit 0, where the repo turned the hook off or where Node is missing. Every folder name
holds a space.
Run directly: python3 test_rules.py
"""
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

HOOKS = Path(__file__).parent
# Raw bytes: a Windows checkout may hold CRLF, and the hook prints the file as it is.
RULES = (HOOKS / "rules.md").read_bytes().decode("utf-8")


def run(project, *args, cwd=None, script=HOOKS / "rules.js"):
    env = {k: v for k, v in os.environ.items() if k != "CLAUDE_PROJECT_DIR"}
    if project is not None:
        env["CLAUDE_PROJECT_DIR"] = str(project)
    p = subprocess.run(["node", str(script), *args], capture_output=True, text=True, encoding="utf-8", env=env, cwd=cwd)
    assert p.returncode == 0 and p.stderr == "", (p.returncode, p.stderr)
    return p.stdout


def printed(out, event="SessionStart"):
    o = json.loads(out)["hookSpecificOutput"]
    assert o == {"hookEventName": event, "additionalContext": RULES}, o
    return True


def main():
    assert RULES.startswith("## kaizen working rules")
    assert len(RULES) < 9000, "hook stdout is cut at 10,000 characters"
    with tempfile.TemporaryDirectory(prefix="kaizen rules ") as t:
        t = Path(t)
        bare = t / "no claude md"
        bare.mkdir()
        assert printed(run(bare))
        assert printed(run(bare, "SubagentStart"), "SubagentStart")
        assert printed(run(None, cwd=bare)), "no CLAUDE_PROJECT_DIR: the working folder is read"

        old = t / "old block"
        old.mkdir()
        (old / "CLAUDE.md").write_text("# App\n\n<!-- kaizen:rules 1.6.1 -->\n## Working rules\n<!-- /kaizen:rules -->\n", encoding="utf-8")
        assert printed(run(old)), "a block an older version wrote does not silence the hook"

        off = t / "turned off"
        (off / "sub dir").mkdir(parents=True)
        (off / ".kaizen-rules-off").write_text("", encoding="utf-8")
        assert run(off) == "" and run(off / "sub dir") == ""

        # A copy without the rules file stays silent instead of failing.
        lone = t / "lone hook"
        lone.mkdir()
        shutil.copy(HOOKS / "rules.js", lone / "rules.js")
        assert run(bare, script=lone / "rules.js") == ""

        # Antigravity: once per conversation, before its first model call.
        def agy(root, num=0, transcript=None):
            payload = json.dumps({"workspacePaths": [str(root)], "invocationNum": num, "transcriptPath": str(transcript or t / "none.jsonl")})
            p = subprocess.run(["node", str(HOOKS / "rules.js"), "PreInvocation"], input=payload, capture_output=True, text=True, encoding="utf-8")
            assert p.returncode == 0 and p.stderr == "", (p.returncode, p.stderr)
            return p.stdout

        assert json.loads(agy(bare)) == {"injectSteps": [{"userMessage": RULES}]}
        assert agy(bare, num=1) == "", "a later call of the turn"
        seen = t / "seen.jsonl"
        seen.write_text(json.dumps({"userMessage": RULES}) + "\n", encoding="utf-8")
        assert agy(bare, transcript=seen) == "", "this conversation already holds the rules"
        assert agy(off / "sub dir") == ""
        root_hooks = json.loads((HOOKS.parent / "hooks.json").read_text(encoding="utf-8"))
        assert root_hooks["kaizen"]["PreInvocation"][0]["command"] == "node hooks/rules.js PreInvocation"

        # The commands as the host runs them, from a plugin folder whose path holds a space.
        bash = shutil.which("bash")
        if not bash:
            print("skipped: the hooks.json commands, no bash on PATH")
        else:
            plugin = t / "plugin root"
            shutil.copytree(HOOKS, plugin / "hooks")
            hooks = json.loads((HOOKS / "hooks.json").read_text(encoding="utf-8"))["hooks"]
            assert hooks["SessionStart"][0]["matcher"] == "startup|resume|clear|compact"
            for event in ("SessionStart", "SubagentStart"):
                cmd = hooks[event][0]["hooks"][0]["command"]
                env = dict(os.environ, CLAUDE_PLUGIN_ROOT=str(plugin), CLAUDE_PROJECT_DIR=str(bare))
                p = subprocess.run([bash, "-c", cmd], capture_output=True, text=True, encoding="utf-8", env=env)
                assert p.returncode == 0 and printed(p.stdout, event), (p.returncode, p.stderr)
                env["PATH"] = str(t / "no node here")
                p = subprocess.run([bash, "-c", cmd], capture_output=True, text=True, encoding="utf-8", env=env)
                assert (p.returncode, p.stdout, p.stderr) == (0, "", ""), "Node missing: silent"
    print("ok")


if __name__ == "__main__":
    main()
