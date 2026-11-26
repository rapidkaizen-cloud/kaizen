
## Output folder: {dir}

The user set an output folder, so this one, which belongs to this repo, worktree or workspace alone, is mandatory, for subagents too.

- **What goes there** — every file made for the user and not part of the repo: report, export, capture, download, log, one-off script, a backup they asked for. One subfolder per topic. Temporary files go to the scratchpad.
- **Writing** — give a script the full output path, and make it stop when that path is empty.
- **Checking** — after it runs, see that the file is there. Find one that is not, then move it, or delete it if temporary, before the next step.
- **Closing** — list each file with its full path.
