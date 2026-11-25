#!/usr/bin/env node
// Prints the working-rules block into a session's or subagent's context. It never refuses,
// holds or blocks, and exits 0 on every path. Silent where a CLAUDE.md in the project folder
// or one above it already holds the block (the repo's own version wins), or where
// `.kaizen-rules-off` sits in one of those folders. Argument: the hook event name.
const fs = require('fs');
const path = require('path');

try {
  const event = process.argv[2] || 'SessionStart';
  // stdin is never read: on Windows a piped payload can leave it open and stall the session.
  let dir = path.resolve(process.env.CLAUDE_PROJECT_DIR || process.cwd());
  for (;;) {
    if (fs.existsSync(path.join(dir, '.kaizen-rules-off'))) process.exit(0);
    const claude = path.join(dir, 'CLAUDE.md');
    if (fs.existsSync(claude) && /^<!-- kaizen:rules\b/m.test(fs.readFileSync(claude, 'utf8'))) process.exit(0);
    const up = path.dirname(dir);
    if (up === dir) break;
    dir = up;
  }
  const rules = fs.readFileSync(path.join(__dirname, '..', 'skills', 'norms-config', 'rules.md'), 'utf8');
  process.stdout.write(JSON.stringify({ hookSpecificOutput: { hookEventName: event, additionalContext: rules } }));
} catch (e) {
  // Silent: a hook error must never reach the session.
}
process.exit(0);
