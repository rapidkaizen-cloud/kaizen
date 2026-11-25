#!/usr/bin/env node
// Prints rules.md into a session's or subagent's context. It never refuses, holds or blocks,
// and exits 0 on every path. Silent where `.kaizen-rules-off` sits in the project folder or
// one above it. Argument: the hook event name.
const fs = require('fs');
const path = require('path');

try {
  const event = process.argv[2] || 'SessionStart';
  // stdin is never read: on Windows a piped payload can leave it open and stall the session.
  let dir = path.resolve(process.env.CLAUDE_PROJECT_DIR || process.cwd());
  for (;;) {
    if (fs.existsSync(path.join(dir, '.kaizen-rules-off'))) process.exit(0);
    const up = path.dirname(dir);
    if (up === dir) break;
    dir = up;
  }
  const rules = fs.readFileSync(path.join(__dirname, 'rules.md'), 'utf8');
  process.stdout.write(JSON.stringify({ hookSpecificOutput: { hookEventName: event, additionalContext: rules } }));
} catch (e) {
  // Silent: a hook error must never reach the session.
}
process.exit(0);
