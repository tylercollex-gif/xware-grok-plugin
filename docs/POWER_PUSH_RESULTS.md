# XWare power push results

Local commits only. Nothing was pushed.

## Step 0

- HEAD `c9245f046b2a661a2ede024f518aa22832a5911d`. No `xware-power` commits, so no SKIP and no WIP.
- Python 3.14.6. Godot 4.7.1.stable.official (console exe). Logs: `%TEMP%\xware_power\s0\`.
- The paste file sits next to this checkout, not inside it, so `git status --porcelain` was empty.
- `XWARE_POWER_EXTRACT PASS files=6 bad=0` (`%TEMP%\xware_power\s0\extract.log`).

## Acceptance

- AC1.1 PASS — `POWER_PATCH PASS section=1 edits=2 mirror=.grok-plugin/plugin.json`
- AC1.2 PASS — `XWARE_PLUGIN_VERDICT FAIL version=4.0.2 checks=12 fails=2` (`version_sync`, `spawn_contract` only; manifest checks PASS)
- AC1.3 PASS — status was `.gitignore`, `.grok-plugin/`, `plugin.json`, `scripts/`
- AC2.1 PASS — `POWER_PATCH PASS section=2 edits=13 mirror=.grok-plugin/plugin.json`
- AC2.2 PASS — `XWARE_PLUGIN_VERDICT PASS version=4.0.2 checks=12 fails=0`
- AC2.3 PASS — the seven doc paths only
- AC3.1 PASS — `POWER_PATCH PASS section=3 edits=1 mirror=.grok-plugin/plugin.json`; plugin verdict PASS
- AC3.2 PASS — exit 0; `XWARE_DOCTOR godot_probe PASS renderer=forward_plus`; `XWARE_DOCTOR_VERDICT WARN fails=0 warns=1` (tools)
- AC3.3 PASS — exit 1; `renderer FAIL rendering_method=mobile`; `godot_probe FAIL renderer=mobile`; addons / editor-python / studio_raise WARNs; `XWARE_DOCTOR_VERDICT FAIL fails=2 warns=5`
- AC3.4 PASS — status was `.grok-plugin/plugin.json`, `plugin.json`, `skills/xware-ship/`
- AC4.1 PASS — `POWER_PATCH PASS section=4 edits=5 mirror=.grok-plugin/plugin.json`; plugin verdict PASS
- AC4.2 PASS — `agents/xware.md`, `docs/DECISIONS_4.0.md`, `skills/xware/SKILL.md`
- Sweep a PASS — four `POWER_PATCH PASS` lines, every edit `PATCH_SKIP`, status empty (`%TEMP%\xware_power\s5\idempotent.log`)
- Sweep b PASS — `XWARE_PLUGIN_VERDICT PASS version=4.0.2 checks=12 fails=0`
- Sweep c PASS — same doctor verdicts as AC3.2 / AC3.3 (`%TEMP%\xware_power\s5\good.log`, `%TEMP%\xware_power\s5\bad.log`)
- Sweep d PASS — the 16 paths named in the prompt, no others

## UNVERIFIED (not tested before ship)

- Grok Build actually installing the plugin from `.grok-plugin/plugin.json` and listing `xware-ship`.
- The marketplace index for this commit (`generate-plugin-index.py` was not run against it on this PC).
- The doctor on a real game, and `ship_probe.gd` on a game with autoloads (the probe quits in `_init`, but autoload `_ready` behaviour under `-s` was not tested).
- The agent-card changes changing agent behaviour in a real spawn.

## Gated on Tyler

- Pushing.
- A version bump (4.0.2 to 4.0.3 or 4.1.0) before any push, because this is new content under the released 4.0.2 number.
- Updating PR #110 `source.sha` (it pins `27ed734` today) and regenerating its index.
- Replacing the 3.6.0 PR text.

## Commits

- `xware-power: 1/5` `bbc0c95`
- `xware-power: 2/5` `1cc7360`
- `xware-power: 3/5` `d0d373a`
- `xware-power: 4/5` `945f01d`
- `xware-power: 5/5` is the commit that adds this file
