#!/usr/bin/env node
// Prints rules.md into a session's or subagent's context, and output.md after it where
// `KAIZEN_OUTPUT_DIR` names a folder: each repo, linked worktree and Orca folder workspace has
// its own folder there. It never refuses, holds or blocks, and exits 0 on every path. Silent
// where `.kaizen-rules-off` sits in the project folder or one above it. Argument: the hook event
// name — `SessionStart`, `SubagentStart` or `PostToolUse` on Claude Code, `PreInvocation` on
// Antigravity. `PostToolUse` names a new file written outside the session's own folder.
const fs = require('fs');
const os = require('os');
const path = require('path');
const { execFileSync } = require('child_process');

const MARK = '## kaizen working rules';
const OUTPUT = (process.env.KAIZEN_OUTPUT_DIR || '').trim();

function turnedOff(dir) {
  for (dir = path.resolve(dir); ; dir = path.dirname(dir)) {
    if (fs.existsSync(path.join(dir, '.kaizen-rules-off'))) return true;
    if (path.dirname(dir) === dir) return false;
  }
}

function inside(file, dir) {
  const rel = path.relative(dir, file);
  return rel !== '..' && !rel.startsWith('..' + path.sep) && !path.isAbsolute(rel);
}

function ownFolder(dir) {
  let name = '';
  try {
    const [common, gitDir, top] = execFileSync('git',
      ['-C', dir, 'rev-parse', '--path-format=absolute', '--git-common-dir', '--git-dir', '--show-toplevel'],
      { encoding: 'utf8', timeout: 5000, stdio: ['ignore', 'pipe', 'ignore'] }).split(/\r?\n/);
    const base = path.basename(top);
    const repo = path.basename(path.dirname(common));
    name = path.relative(common, gitDir) === '' || base.toLowerCase().startsWith(`${repo.toLowerCase()}-`) ? base : `${repo}-${base}`;
  } catch (e) {
    // An Orca folder workspace has no repo: its folder is the workspace.
    const orca = Object.keys(process.env).some((key) => key.startsWith('ORCA_'));
    if (orca && path.relative(os.homedir(), dir) !== '') name = path.basename(path.resolve(dir));
  }
  return path.join(OUTPUT, name || '_general');
}

function strayFile(p) {
  const file = p.tool_input && p.tool_input.file_path;
  if (!OUTPUT || !file || !p.tool_response || p.tool_response.type !== 'create') return null;
  const project = process.env.CLAUDE_PROJECT_DIR || p.cwd || process.cwd();
  if (turnedOff(project)) return null;
  const own = ownFolder(project);
  const allowed = [own, project, p.cwd, os.tmpdir(), path.join(os.homedir(), '.claude')];
  return allowed.some((dir) => dir && inside(path.resolve(file), path.resolve(dir))) ? null : { file, own };
}

try {
  const event = process.argv[2] || 'SessionStart';
  const rules = fs.readFileSync(path.join(__dirname, 'rules.md'), 'utf8');
  const output = (dir) => !OUTPUT ? '' : fs.readFileSync(path.join(__dirname, 'output.md'), 'utf8').replace('{dir}', () => ownFolder(dir));
  if (event === 'PostToolUse') {
    const stray = strayFile(JSON.parse(fs.readFileSync(0, 'utf8').replace(/^﻿/, '') || '{}'));
    if (stray) {
      const note = `${stray.file} is a new file outside the output folder ${stray.own}. If it was made for the user, move it there now. If it belongs to another repo or to an app's own folder, leave it and say so.`;
      process.stdout.write(JSON.stringify({ hookSpecificOutput: { hookEventName: event, additionalContext: note } }));
    }
  } else if (event === 'PreInvocation') {
    // Antigravity runs this before every model call: hand the rules over once per conversation,
    // before its first call, as a user step that stays in the conversation.
    const p = JSON.parse(fs.readFileSync(0, 'utf8').replace(/^﻿/, '') || '{}');
    const root = (p.workspacePaths && p.workspacePaths[0]) || process.cwd();
    let seen = false;
    try { seen = fs.readFileSync(p.transcriptPath, 'utf8').includes(MARK); } catch (e) {}
    if (!p.invocationNum && !seen && !turnedOff(root)) {
      process.stdout.write(JSON.stringify({ injectSteps: [{ userMessage: rules + output(root) }] }));
    }
  } else if (!turnedOff(process.env.CLAUDE_PROJECT_DIR || process.cwd())) {
    // stdin is never read here: on Windows a piped payload can leave it open and stall the session.
    process.stdout.write(JSON.stringify({ hookSpecificOutput: { hookEventName: event, additionalContext: rules + output(process.env.CLAUDE_PROJECT_DIR || process.cwd()) } }));
  }
} catch (e) {
  // Silent: a hook error must never reach the session.
}
process.exit(0);
