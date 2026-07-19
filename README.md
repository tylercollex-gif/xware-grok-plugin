# XWare — Grok Build Plugin (Xware 3.2)

**XWare** is a Grok 4.5 / Grok Build **agent + skill** for **solo indie 3D Godot** game creation.  
**Xwanre 3.2** = full xAI power: elevate + local continuous learning + Imagine look skills + optional API textures.  


```powershell
# Full power rehydrate (run after Grok CLI updates)
powershell -ExecutionPolicy Bypass -File "$env:USERPROFILE\Documents\HelixProtocol\tools\xware\install_xhance.ps1"
```

See [XHANCE.md](XHANCE.md).

Spawn `subagent_type="xware"` for graphics, animation, materials, physics, Experience Elevate, Character Engine, playtest improve loops, and **continuous learning** — without inventing a second asset pipeline.

**Engine Improve Law:** every multi-step raise writes anonymized weak signals into a local hub so the **next** game elevate densifies smarter. Privacy-safe aggregates only.

| Component | Path |
|-----------|------|
| Agent | [`agents/xware.md`](agents/xware.md) |
| Skill | [`skills/xware/SKILL.md`](skills/xware/SKILL.md) |
| Role | [`roles/xware.toml`](roles/xware.toml) |
| Manifest | [`plugin.json`](plugin.json) — **3.2.1 (Xhance)** |
| Skills | `/xware` · `/xware-xhance` · `/xware-elevate` |

## Install

### From marketplace / GitHub

```powershell
grok plugin install tylercollex-gif/xware-grok-plugin --trust
# pin a commit (recommended after each engine win):
# grok plugin install tylercollex-gif/xware-grok-plugin@COMMIT_SHA --trust
```

### From local path

```powershell
grok plugin install "C:\Users\winge\Documents\Xware\grok-plugin" --trust
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
Profile: open_world_rpg_slice | sports | factory_sim | space_arcade | …
Task: solo_bootstrap | experience_elevate | continuous_learn | quality_gate
Constraints: legal only; residual honest; Engine Improve Law (hub pack after elevate).
"""
)
```

### Godot runtime (required for elevate CLI)

The marketplace plugin is the **agent**. Meshgen / elevate scripts install into the game from an XWare SOT (e.g. HelixProtocol):

```powershell
powershell -File tools\xware\install_to_project.ps1 -Target <YourGame> -Profile open_world_rpg_slice
# Stamps [network] share_feedback_local=true so elevates feed ~/.grok/xware_network/
```

```powershell
$env:GODOT = "C:\Path\To\Godot_v4.exe"
py tools/xware/ai/design_intent.py --project .
py tools/xware/ai/experience_elevate.py --project . --from-intent --playtest-improve
py tools/xware/ai/continuous_learn.py --project .
py tools/xware/ai/quality_gate.py --project . --profile <profile>
```

## Continuous learning (race to stay ahead)

| Ring | What |
|------|------|
| Same machine | Packs in `~/.grok/xware_network/` improve densify order across games |
| Multi-game | Sibling discovery under Documents |
| Cloud | Opt-in only (`share_feedback_cloud` + `cloud_url`) |

Never shares meshes, paths, or textures — only anonymized role/residual aggregates.

## Maintainer: bump marketplace pin after engine wins

1. Improve Helix SOT / copy agent+skill here  
2. Bump `plugin.json` version  
3. `git push` this repo  
4. Update [plugin-marketplace PR #110](https://github.com/xai-org/plugin-marketplace/pull/110) (or follow-up) **source.sha** to the new full 40-char commit  

See [MARKETPLACE_PR.md](MARKETPLACE_PR.md).

## Keywords

`godot` · `game` · `3d` · `indie` · `graphics` · `animation` · `xware` · `xhance` · `gamedev` · `grok-build` · `continuous-learning`
