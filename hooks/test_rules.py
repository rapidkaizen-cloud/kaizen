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

os.environ.pop("KAIZEN_OUTPUT_DIR", None)
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


def output_text(folder):
    return (HOOKS / "output.md").read_bytes().decode("utf-8").replace("{dir}", str(folder))


def agy_output(hook, root):
    return hook("PreInvocation", json.dumps({"workspacePaths": [str(root)], "invocationNum": 0, "transcriptPath": ""}))


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

        # The output folder: nothing while unset; once set, printed and checked.
        out = t / "my output"
        outside = t / "elsewhere" / "report.md"
        # The check allows the system temp folder, and this test runs inside it: point temp elsewhere.
        base = dict({k: v for k, v in os.environ.items() if not k.startswith("ORCA_")}, **{k: str(t / "temp") for k in ("TEMP", "TMP", "TMPDIR")})

        def hook(event, payload="", output=out, project=bare, **extra):
            env = dict(base, CLAUDE_PROJECT_DIR=str(project), **extra)
            if output:
                env["KAIZEN_OUTPUT_DIR"] = str(output)
            p = subprocess.run(["node", str(HOOKS / "rules.js"), event], input=payload, capture_output=True, text=True, encoding="utf-8", env=env)
            assert p.returncode == 0 and p.stderr == "", (p.returncode, p.stderr)
            return p.stdout

        def wrote(file, kind="create"):
            return json.dumps({"cwd": str(bare), "tool_input": {"file_path": str(file)}, "tool_response": {"type": kind}})

        for event in ("SessionStart", "SubagentStart"):
            assert printed(hook(event, output=None), event)
            text = json.loads(hook(event))["hookSpecificOutput"]["additionalContext"]
            assert text.startswith(RULES) and f"## Output folder: {out / '_general'}\n" in text.replace("\r\n", "\n") and len(text) < 9000
        assert hook("SessionStart", project=off) == ""
        assert hook("PostToolUse", wrote(outside), output=None) == "", "unset: free"
        note = json.loads(hook("PostToolUse", wrote(outside)))["hookSpecificOutput"]
        assert note["hookEventName"] == "PostToolUse" and str(outside) in note["additionalContext"]
        assert hook("PostToolUse", wrote(t / "my output 2" / "a.md")) != "", "a sibling with the same prefix"
        for file in (out / "_general" / "topic" / "a.md", out / "_general" / "..a.md", bare / "a.md", t / "temp" / "a.md", Path.home() / ".claude" / "a.md"):
            assert hook("PostToolUse", wrote(file)) == "", file
        assert hook("PostToolUse", wrote(outside, "update")) == "", "an existing file"
        assert hook("PostToolUse", wrote(outside), project=off) == ""
        for bad in ("", "not json", "{}"):
            assert hook("PostToolUse", bad) == "", bad

        # Each repo, linked worktree and Orca folder workspace has a folder of its own.
        def folder(project, **extra):
            text = json.loads(hook("SessionStart", project=project, **extra))["hookSpecificOutput"]["additionalContext"]
            return Path(text.split("## Output folder: ")[1].splitlines()[0])

        def git(*args):
            subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *args], check=True, capture_output=True)

        repo = t / "my app"
        (repo / "sub").mkdir(parents=True)
        git("init", "-q", str(repo))
        git("-C", str(repo), "commit", "-q", "--allow-empty", "-m", "x")
        git("-C", str(repo), "worktree", "add", "-q", str(t / "wt" / "fix"))
        git("-C", str(repo), "worktree", "add", "-q", "-b", "two", str(t / "wt" / "my app-two"))
        assert folder(repo) == folder(repo / "sub") == out / "my app"
        assert folder(t / "wt" / "fix") == out / "my app-fix"
        assert folder(t / "wt" / "my app-two") == out / "my app-two"
        assert folder(bare) == out / "_general"
        assert folder(bare, ORCA_APP_VERSION="1") == out / "no claude md"
        assert folder(repo, ORCA_APP_VERSION="1") == out / "my app"
        assert folder(Path.home(), ORCA_APP_VERSION="1") == out / "_general"
        assert json.loads(agy_output(hook, repo)) == {"injectSteps": [{"userMessage": RULES + output_text(out / "my app")}]}
        assert hook("PostToolUse", wrote(out / "my app" / "a.md"), project=repo) == ""
        assert "my app-fix" in hook("PostToolUse", wrote(out / "my app" / "a.md"), project=t / "wt" / "fix"), "another checkout's folder"
        assert hook("PostToolUse", wrote(out / "a.md"), project=repo) != "", "the root of the output folder"
        if bash:
            cmd = hooks["PostToolUse"][0]["hooks"][0]["command"]
            for value, says in ((str(out), True), ("", False)):
                env = dict(base, CLAUDE_PLUGIN_ROOT=str(plugin), CLAUDE_PROJECT_DIR=str(bare), KAIZEN_OUTPUT_DIR=value)
                p = subprocess.run([bash, "-c", cmd], input=wrote(outside), capture_output=True, text=True, encoding="utf-8", env=env)
                assert (p.returncode, bool(p.stdout), p.stderr) == (0, says, ""), (value, p)
    print("ok")


if __name__ == "__main__":
    main()
