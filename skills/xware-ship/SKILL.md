---
name: xware-ship
description: >
  Read-only XWare ship check for a Godot 4 game headed to Steam: Forward+ renderer,
  addons allowlist (xware + godotsteam only), third-party asset markers, XWare config
  that runs Python on editor open, machine-local paths, export presets, honest
  studio_raise reports, and whether the official XWare tools are installed. Use before
  a release, a Steam build or a Grok Build push file. Never writes or regenerates tools.
metadata:
  short-description: "XWare doctor: Godot 4 Forward+ to Steam bar, read-only"
---

# XWare Ship (doctor)

Read-only. Stdlib Python plus an optional headless Godot probe. Takes seconds. It finds the
official XWare tools and checks the game. It never writes, installs or regenerates anything.

```powershell
# from the plugin checkout (or ~/.grok plugin cache): skills/xware-ship/scripts/
py skills/xware-ship/scripts/xware_doctor.py --project <game> --reports
# + the engine's effective settings (headless, no editor, no import, about a second):
py skills/xware-ship/scripts/xware_doctor.py --project <game> --reports --godot $env:GODOT
```

Output: `XWARE_DOCTOR <id> PASS|INFO|WARN|FAIL <detail>`, then `TOOLS_OK <path>` or
`TOOLS_MISSING ...`, then one `XWARE_DOCTOR_VERDICT PASS|WARN|FAIL ...` line.
Exit 0 = PASS or WARN, 1 = FAIL, 2 = not a Godot project.

## The bar it checks (Godot 4 Forward+ to Steam)

| Check | PASS when |
|-------|-----------|
| `godot_version` / `renderer` | Godot 4 and `forward_plus` (FAIL otherwise) |
| `addons` | only `addons/xware` and `addons/godotsteam` (anything else needs the owner's OK) |
| `third_party_assets` | no asset-pack names or stray license files outside xware/godotsteam (bundled Poly Haven CC0 is fine: keep its notice in the credits) |
| `xware_editor_python` | `[auto] auto_raise_on_open` and `on_low_score` are false (else the editor runs blocking Python and writes into `assets/`) |
| `xware_cloud_share` | `share_feedback_cloud=false` unless the owner opted in |
| `version_drift` | `addons/xware/plugin.cfg` version = `.grok/agents/xware.md` version |
| `local_paths` | no `C:\Users\...` / `/home/...` paths in xware, scripts, scenes, `.grok` |
| `export_presets` | presets exist, exclude `tools/*`, `addons/xware/ai/*`, `addons/xware/feedback/*`, never ship `steam_appid.txt` |
| `report_studio_raise` (`--reports`) | overall pass with no FAIL department, no SOFT QA, nothing missing or skipped |
| `report_video_evidence` (`--reports`) | a screen-record or playtest report exists (stills can't PASS 3D residual) |
| `godot_probe` (`--godot`) | the engine's effective renderer is `forward_plus` |

## Rules

- **Tools missing:** print the `TOOLS_MISSING` line and stop. Install from the owner's XWare tools
  checkout (`install_to_project.ps1`). Never write replacement tools (AI_USE_POLICY).
- **Look path:** the official look is Imagine + `material_pack` + residual. The doctor only reports.
  It never generates assets.
- **Tests stay short:** the doctor, `--check-only`, a few headless `-s` checks, ONE ~1-minute Forward+
  smoke. Never open the editor in an automated run (XWare runs Python on open). Anything not run
  goes under UNVERIFIED and is never marked PASS.
- **Push files:** one paste, numbered sections, one commit per section, Step 0 skips sections
  already committed, and a single push only with the owner's OK. If a game carries
  `addons/xware/import/FLAGFALL_LESSONS.md`, follow it (push template, test standard, fairness).
- **Never publish** (Steam, GitHub release, marketplace pin, posts) without the owner's OK.
