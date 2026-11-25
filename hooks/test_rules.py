#!/usr/bin/env python3
"""Self-check rules.js and the commands in hooks.json: the block is printed where the repo
has none, and nothing is printed, with exit 0, where it has one, where the repo turned the
hook off, or where Node is missing. Every folder name holds a space.
Run directly: python3 test_rules.py
"""
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

HOOKS = Path(__file__).parent
ROOT = HOOKS.parent
# Raw bytes: a Windows checkout may hold CRLF, and the hook prints the file as it is.
RULES = (ROOT / "skills" / "norms-config" / "rules.md").read_bytes().decode("utf-8")
BLOCK = "# App\n\n<!-- kaizen:rules 1.4.0 -->\n" + RULES.split("\n", 1)[1]


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
    assert RULES.startswith("<!-- kaizen:rules ") and RULES.rstrip().endswith("<!-- /kaizen:rules -->")
    assert len(RULES) < 9000, "hook stdout is cut at 10,000 characters"
    with tempfile.TemporaryDirectory(prefix="kaizen rules ") as t:
        t = Path(t)
        bare = t / "no claude md"
        bare.mkdir()
        assert printed(run(bare))
        assert printed(run(bare, "SubagentStart"), "SubagentStart")
        assert printed(run(None, cwd=bare)), "no CLAUDE_PROJECT_DIR: the working folder is read"

        other = t / "other claude md"
        other.mkdir()
        (other / "CLAUDE.md").write_text("# App\n\nThe block starts with `<!-- kaizen:rules`.\n", encoding="utf-8")
        assert printed(run(other)), "the marker quoted in prose is not a block"

        has = t / "has block"
        (has / "sub dir").mkdir(parents=True)
        (has / "CLAUDE.md").write_text(BLOCK, encoding="utf-8")
        assert run(has) == "", "an older block in the repo wins"
        assert run(has, "SubagentStart") == ""
        assert run(has / "sub dir") == "", "a block one folder up counts"

        off = t / "turned off"
        (off / "sub dir").mkdir(parents=True)
        (off / ".kaizen-rules-off").write_text("", encoding="utf-8")
        assert run(off) == "" and run(off / "sub dir") == ""

        # A copy without the rules file stays silent instead of failing.
        lone = t / "lone hook"
        lone.mkdir()
        shutil.copy(HOOKS / "rules.js", lone / "rules.js")
        assert run(bare, script=lone / "rules.js") == ""

        # The commands as the host runs them, from a plugin folder whose path holds a space.
        bash = shutil.which("bash")
        if not bash:
            print("skipped: the hooks.json commands, no bash on PATH")
        else:
            plugin = t / "plugin root"
            shutil.copytree(HOOKS, plugin / "hooks")
            (plugin / "skills" / "norms-config").mkdir(parents=True)
            shutil.copy(ROOT / "skills" / "norms-config" / "rules.md", plugin / "skills" / "norms-config")
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
