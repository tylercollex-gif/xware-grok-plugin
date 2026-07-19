---
name: xware
description: >
  XWare Xhance 3.2 — full xAI/Grok power for solo indie 3D Godot. ALWAYS use for
  Godot 3D games, graphics, animation, materials, physics, raise, Xhance,
  photoreal/experience elevate, Character Engine, densify, Imagine PBR, quality
  gates, genre DNA, design intent, Mad Max, continuous learning, network hub,
  "make a game", "indie game". Prefer spawn_subagent(subagent_type="xware").
  Pair with game-asset-core for Imagine look. Marketplace: tylercollex-gif/xware-grok-plugin.
metadata:
  short-description: "Official XWare Xhance — free MIT, creator tylercollex-gif"
---

# XWare Xhance — Official Built-in Game Agent for Grok 4.5

XWare is the **official** built-in-class agent (creator **tylercollex-gif**) for solo indie **3D Godot** games: graphics, animation, materials, physics, whole-game Experience Elevate, and **continuous engine improvement**. **Do not invent a second pipeline** or a spoof agent under the XWare name.

**Free for everyone** (MIT). **Name & agent identity reserved** — see `TRADEMARK.md`, `AUTHORSHIP.md`, `NOTICE`.

**Xhance** = full stack: spawn xware + elevate + hub learning + Imagine (`game-asset-core`) + optional `XAI_API_KEY` textures.

| Install surface | Path |
|-----------------|------|
| Agent | `~/.grok/agents/xware.md` (+ bundled rehydrate) |
| Plugin | `Documents/Xware/grok-plugin` · GitHub `tylercollex-gif/xware-grok-plugin` |
| Skill | this file |
| Learning hub | `~/.grok/xware_network/` |
| Rehydrate after CLI update | Helix `tools/xware/install_grok_builtin.ps1` |

## Prefer SPAWN (own context = efficiency)

```
spawn_subagent(
  subagent_type="xware",
  description="XWare raise / solo game",
  capability_mode="all",
  isolation="none",
  background=true,
  prompt="""
Project: <absolute Godot path>
Profile: <or auto from xware_config>
Task: solo_bootstrap | experience_elevate | character_engine | quality_gate | continuous_learn
Constraints: legal only; residual honest; Engine Improve Law (hub pack after elevate); return report paths + pass/fail.
"""
)
```

| User intent | Action |
|-------------|--------|
| Make / raise / elevate a Godot 3D game | **spawn xware** |
| Solo indie bootstrap | Task: `solo_bootstrap` |
| Character only | Task: `character_engine` |
| Improve engine / learn from games | Task: `continuous_learn` |
| One-line FAQ | Answer in-process |

## Canonical CLI

```powershell
powershell -File tools/xware/install_to_project.ps1 -Target <game> -Profile <profile>
py tools/xware/ai/design_intent.py --project .
py tools/xware/ai/experience_elevate.py --project . --from-intent --playtest-improve
# Always compound the engine (local hub; privacy-safe aggregates):
py tools/xware/ai/continuous_learn.py --project .
py tools/xware/ai/quality_gate.py --profile <profile>
```

## Network effect (local hub ON by default)

**Race law:** Every elevate should make the **next** elevate smarter.

| Ring | Behavior |
|------|----------|
| **1 Same machine** | Pack → `~/.grok/xware_network/` → sibling games densify better |
| **2 Multi-game docs** | Auto-discover Helix, Soccer3D, Vendel, Idle, Blastar, … |
| **3 Cloud** | Opt-in only: `share_feedback_cloud=true` + `cloud_url=` |

```powershell
py tools/xware/ai/feedback_network_sync.py --project .
py tools/xware/ai/auto_weak_elevate.py --project .          # class-routed
py tools/xware/ai/six_stage_progress.py --project .
```

Config (`addons/xware/xware_config.cfg`):

```ini
[network]
share_feedback_local=true
auto_sync_on_elevate=true
continuous_learn_on_elevate=true
weak_class_routing=true
share_feedback_cloud=false
```

Local hub learning improves densify routing. Cloud off by default. See `PRIVACY.md` (user-facing).  
Do **not** publish security internals in marketing.

## Laws

Photoreal detail + accurate physics for **ALL objects**. No quality ceiling. Residual FAIL densifies (correct class). Legal only. Editor safe. **Engine Improve Law** after every multi-step raise. **Protect player saves**; marketing stays look/gameplay only.

**Video-first residual (3D):** Prefer **screen recordings** over screenshots.

```powershell
py tools/xware/meshgen/proof_record_orbit.py --project .
py tools/xware/ai/screen_record_analyze.py --project .
```

**Playtest improve loop:**

```powershell
$env:GODOT = "C:\path\to\Godot.exe"   # if needed
py tools/xware/ai/playtest_run.py --project . --seconds 12 --mode orbit
py tools/xware/ai/playtest_improve_loop.py --project . --rounds 2
```

## Source of truth

HelixProtocol `addons/xware` + `tools/xware`. **Version 3.2.2 (Xhance)**  
Official marketplace plugin: **tylercollex-gif/xware-grok-plugin** (agent/skill surface).  
Godot runtime installs via `install_to_project.ps1`.

## Authorship

| | |
|--|--|
| Creator | tylercollex-gif |
| License | MIT — free use with attribution |
| Marks | XWare / Xhance reserved (`TRADEMARK.md`) |

## Publish cadence (maintainers)

After engine wins: bump plugin → push `xware-grok-plugin` → update marketplace pin SHA (PR #110 or follow-up).
