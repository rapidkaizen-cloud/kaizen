#!/usr/bin/env node
// Prints rules.md into a session's or subagent's context. It never refuses, holds or blocks,
// and exits 0 on every path. Silent where `.kaizen-rules-off` sits in the project folder or
// one above it. Argument: the hook event name — `SessionStart` or `SubagentStart` on Claude
// Code, `PreInvocation` on Antigravity.
const fs = require('fs');
const path = require('path');

const MARK = '## kaizen working rules';

function turnedOff(dir) {
  for (dir = path.resolve(dir); ; dir = path.dirname(dir)) {
    if (fs.existsSync(path.join(dir, '.kaizen-rules-off'))) return true;
    if (path.dirname(dir) === dir) return false;
  }
}

try {
  const event = process.argv[2] || 'SessionStart';
  const rules = fs.readFileSync(path.join(__dirname, 'rules.md'), 'utf8');
  if (event === 'PreInvocation') {
    // Antigravity runs this before every model call: hand the rules over once per conversation,
    // before its first call, as a user step that stays in the conversation.
    const p = JSON.parse(fs.readFileSync(0, 'utf8').replace(/^﻿/, '') || '{}');
    const root = (p.workspacePaths && p.workspacePaths[0]) || process.cwd();
    let seen = false;
    try { seen = fs.readFileSync(p.transcriptPath, 'utf8').includes(MARK); } catch (e) {}
    if (!p.invocationNum && !seen && !turnedOff(root)) {
      process.stdout.write(JSON.stringify({ injectSteps: [{ userMessage: rules }] }));
    }
  } else if (!turnedOff(process.env.CLAUDE_PROJECT_DIR || process.cwd())) {
    // stdin is never read here: on Windows a piped payload can leave it open and stall the session.
    process.stdout.write(JSON.stringify({ hookSpecificOutput: { hookEventName: event, additionalContext: rules } }));
  }
} catch (e) {
  // Silent: a hook error must never reach the session.
}
process.exit(0);
