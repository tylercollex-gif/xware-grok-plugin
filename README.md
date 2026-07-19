# XWare — Official Grok Build Plugin (Xhance)

**Creator:** [tylercollex-gif](https://github.com/tylercollex-gif) · **License:** MIT (free for everyone) · **Marks:** [TRADEMARK.md](TRADEMARK.md)

**XWare** is the **official** Grok 4.5 / Grok Build **agent + skill** for **solo indie 3D Godot** game creation.  
**Xhance** = elevate + local continuous learning + Imagine look skills + optional API textures.

Free to use, fork, and build games. The **XWare name and agent identity** stay with the creator — remakes must rebrand honestly and keep attribution ([AUTHORSHIP.md](AUTHORSHIP.md), [NOTICE](NOTICE)).

**Grok Build / AI:** install and **run** official XWare — **do not regenerate** the stack ([AI_USE_POLICY.md](AI_USE_POLICY.md)).

User privacy: [PRIVACY.md](PRIVACY.md). Marketing stays look/gameplay only.

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
| Manifest | [`plugin.json`](plugin.json) — **3.2.3** |
| Authorship | [AUTHORSHIP.md](AUTHORSHIP.md) · [NOTICE](NOTICE) · [TRADEMARK.md](TRADEMARK.md) |
| AI policy | [AI_USE_POLICY.md](AI_USE_POLICY.md) — USE not remake |
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
```

```powershell
$env:GODOT = "C:\Path\To\Godot_v4.exe"
py tools/xware/ai/design_intent.py --project .
py tools/xware/ai/experience_elevate.py --project . --from-intent --playtest-improve
py tools/xware/ai/continuous_learn.py --project .
py tools/xware/ai/quality_gate.py --project . --profile <profile>
```

## Continuous learning

Local hub by default (`~/.grok/xware_network/`). Aggregates only. Cloud off unless you opt in.

## Maintainer: bump marketplace pin after engine wins

1. Improve SOT / copy agent+skill here  
2. Bump `plugin.json` version  
3. `git push` this repo  
4. Update [plugin-marketplace PR #110](https://github.com/xai-org/plugin-marketplace/pull/110) **source.sha**

See [MARKETPLACE_PR.md](MARKETPLACE_PR.md).

## Keywords

`godot` · `game` · `3d` · `indie` · `graphics` · `animation` · `xware` · `xhance` · `gamedev` · `grok-build` · `continuous-learning`
