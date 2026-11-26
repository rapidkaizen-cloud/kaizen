# Update the plugin

A new version reaches a session only after the machine has pulled it and the host has restarted.

## On Claude Code

- **With `autoUpdate` on**, the machine picks up a new version at its next start. Nothing else is needed. The setting is described in [Install](../start/install.md).
- **Without it**, ask a session to update the plugin, or run:

  ```
  claude plugin marketplace update kaizen
  claude plugin update kaizen@kaizen
  ```

Then restart Claude Code. Nothing reaches a session before the restart.

## On Antigravity

```
agy plugin uninstall kaizen
agy plugin install https://github.com/rapidkaizen-cloud/kaizen
```

The install is a copy, and nothing refreshes it.

## Moving to 1.0.0

Version 1.0.0 removed every guard and the rules a session used to be handed at its start. Nothing breaks on update, but an app repo is under no rule until you give it one.

1. **Update to 2.0.0 or later.** Its hook prints the working rules into every session; nothing is written into a repo for them. See [Working rules](../concepts/working-rules.md).
2. **Protect what the guards protected, yourself.** Nothing holds a push, a merge or a destructive SQL statement any more: turn on branch protection, keep database backups, and give sessions a database login that is not the owner.
3. **Say where your files go, if you used the output folder.** Update to 2.2.0 or later and set `KAIZEN_OUTPUT_DIR`: the hook prints one folder per repo, worktree and workspace under it, as in [Rules hook](../reference/rules-hook.md#the-output-folder). Delete a `CLAUDE.md` line, yours or a repo's, that sends files to `<output>\<topic>\`, or make it name the same folders, so it does not contradict the hook.
4. **Leave or delete the old settings.** `switches.json` and the marker `onboarded-output` in the plugin's data folder, and `.claude/destructive-gate.off` in a repo, are read by nothing.
5. **Stop asking for what is gone**: `logic-settle`, and `app-settle`'s modes `migrate`, `align`, `rework` and `seed`. `app-settle` now writes documents only — it scaffolds no app.

[Maintain app repos](maintain-app-repos.md) lists what a repo from an older version still carries.

## Moving from an earlier name

An update in place keeps a machine on the marketplace it was installed from, under the name it had then. A machine that installed this plugin under an earlier name moves once:

1. **Remove the old marketplace.** `claude plugin marketplace list` names it; `claude plugin marketplace remove <name>` uninstalls its plugin with it.
2. **Add the new one and install:** `claude plugin marketplace add rapidkaizen-cloud/kaizen`, then `claude plugin install kaizen@kaizen`.
3. **Turn `autoUpdate` back on**, for `kaizen` this time, as in [Install](../start/install.md). The old entry's setting left with it.
4. **In every app repo whose `.claude/settings.json` names the old plugin key**, change it to `kaizen@kaizen` and commit it, so a teammate's machine enables the plugin there too.
5. **On Antigravity:** `agy plugin list` names the old copy; uninstall it, then install from the new URL as above.
6. **Change the old prefix to `/kaizen:`** in anything of yours that invokes a skill: notes, aliases, scripts.

Then restart the host. The new clone fetches `main`, so the move also mends a clone that still fetches `master`, where updates stop without an error.

## Check what you are running

1. **Run `/kaizen:norms-help`** in any session. The first line is the version of the copy that session loaded.
2. **Read `LAST CHANGE` on the same card**: the newest changelog entry, with its `To act on` lines — what an installed app must do because of that version.
3. **For older versions**, open `CHANGELOG.md` at the repo root.

> [!NOTE]
> `norms-help` reports the copy the session runs, not the newest one on the machine. A plugin installed at project scope updates separately from the user-scope one and falls behind — install at user scope only.

## If you change the plugin yourself

- **Every commit that changes the plugin bumps its version**, because the update compares version numbers only. `.githooks/pre-commit` refuses the commit otherwise: run `git config core.hooksPath .githooks` once per clone.
- **A version bump carries its `CHANGELOG.md` entry** in the same commit.
- **A commit reaches app sessions only after it is pushed.**

## Related

- [norms-help](../reference/norms-help.md)
- [Hosts](../concepts/hosts.md)
