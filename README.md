# XWare — Grok Build Plugin

**XWare** is a Grok 4.5 / Grok Build **agent + skill** for **solo indie 3D Godot** game creation.

Spawn `subagent_type="xware"` for graphics, animation, materials, physics, Experience Elevate, Character Engine, playtest improve loops, and continuous learning — without inventing a second asset pipeline.

| Component | Path |
|-----------|------|
| Agent | [`agents/xware.md`](agents/xware.md) |
| Skill | [`skills/xware/SKILL.md`](skills/xware/SKILL.md) |
| Role | [`roles/xware.toml`](roles/xware.toml) |
| Manifest | [`plugin.json`](plugin.json) |

## Install

### From GitHub (after you publish)

```powershell
grok plugin install YOURUSER/xware-grok-plugin --trust
# pin a commit (recommended for teams):
# grok plugin install YOURUSER/xware-grok-plugin@COMMIT_SHA --trust
```

### From local path

```powershell
grok plugin install "C:\Users\winge\Documents\Xware\grok-plugin" --trust
```

### Rehydrate after Grok CLI updates

```powershell
powershell -File "C:\Users\winge\Documents\HelixProtocol\tools\xware\install_grok_builtin.ps1"
```

Confirm in TUI: `/config-agents` → **xware**

## Use

```
spawn_subagent(
  subagent_type="xware",
  description="Raise my Godot game",
  capability_mode="all",
  isolation="none",
  prompt="""
Project: <absolute path to Godot project>
Profile: open_world_rpg_slice | strategy_tactics | factory_sim | space_arcade | …
Task: solo_bootstrap | experience_elevate | character_engine | playtest_improve_loop | quality_gate
Constraints: legal only; residual honest; return report paths + pass/fail.
"""
)
```

Or ask Grok: *“Spawn XWare and experience-elevate this Godot project.”*

### Godot project CLI (when XWare tools are installed in the game)

```powershell
$env:GODOT = "C:\Path\To\Godot_v4.exe"   # for playtest
py tools/xware/ai/design_intent.py --project .
py tools/xware/ai/experience_elevate.py --project . --from-intent --playtest-improve
py tools/xware/ai/quality_gate.py --project . --profile <profile>
```

Install the **Godot runtime** (meshgen, elevate scripts, addon) from your XWare SOT (e.g. HelixProtocol):

```powershell
powershell -File tools\xware\install_to_project.ps1 -Target <YourGame> -Profile open_world_rpg_slice
```

## Keywords

`godot` · `game` · `3d` · `indie` · `graphics` · `animation` · `xware` · `gamedev` · `grok-build`

## Marketplace (xAI)

To list in the official catalog, open a PR on  
[xai-org/plugin-marketplace](https://github.com/xai-org/plugin-marketplace)  
with a remote entry pointing at this repo + a pinned commit `sha`.

See [xAI Plugin Marketplace announcement](https://x.ai/news/grok-plugin-marketplace).

## Privacy

Local continuous learning uses **anonymized aggregates** only (profile, role weak counts, score buckets). No meshes or personal paths. Optional cloud requires an explicit `cloud_url`.

## License

MIT — see [LICENSE](LICENSE).

## Version

**3.0.0**
