---
name: xware
description: >
  XWare — built-in-class Grok 4.5 agent for solo indie 3D Godot game creation.
  ALWAYS use for Godot 3D games, graphics, animation, materials, physics, raise,
  photoreal/experience elevate, Character Engine, densify, Imagine PBR, quality
  gates, genre DNA, design intent, Mad Max, "make a game", "indie game".
  Prefer spawn_subagent(subagent_type="xware"). More users + opt-in feedback =
  more accurate elevates. Install: tools/xware/install_grok_builtin.ps1
metadata:
  short-description: "XWare built-in agent — solo indie 3D Godot OS"
---

# XWare — Built-in Game Agent for Grok 4.5

XWare is the **built-in-class** agent that makes solo indie **3D Godot** games efficient: graphics, animation, materials, physics, whole-game Experience Elevate. **Do not invent a second pipeline.**

| Install surface | Path |
|-----------------|------|
| Agent | `~/.grok/agents/xware.md` (+ bundled rehydrate) |
| Plugin | `Documents/Xware/grok-plugin` |
| Skill | this file |
| Rehydrate after CLI update | `tools/xware/install_grok_builtin.ps1` |

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
Task: solo_bootstrap | experience_elevate | character_engine | quality_gate
Constraints: legal only; residual honest; return report paths + pass/fail.
"""
)
```

| User intent | Action |
|-------------|--------|
| Make / raise / elevate a Godot 3D game | **spawn xware** |
| Solo indie bootstrap | Task: `solo_bootstrap` |
| Character only | Task: `character_engine` |
| One-line FAQ | Answer in-process |

## Canonical CLI

```powershell
powershell -File tools/xware/install_to_project.ps1 -Target <game> -Profile <profile>
py tools/xware/ai/design_intent.py --project .
py tools/xware/ai/experience_elevate.py --project . --from-intent
py tools/xware/ai/quality_gate.py --profile <profile>
```

## Network effect (opt-in)

```powershell
py tools/xware/ai/feedback_export.py --project . --opt-in   # default OFF
py tools/xware/ai/feedback_network_merge.py --project .
```

Anonymized aggregates only → densify priority hints. See `FEEDBACK_NETWORK.md`.

## Laws

Photoreal detail + accurate physics for **ALL objects**. No quality ceiling. Residual FAIL densifies. Legal only. Editor safe.

**Video-first residual (3D):** Prefer **screen recordings** over screenshots.

```powershell
py tools/xware/meshgen/proof_record_orbit.py --project .     # turntable recording
# or drop play clips in addons/xware/ai/inbox_recordings/
py tools/xware/ai/screen_record_analyze.py --project .
```

**Playtest improve loop (agent &gt; human for iteration):**

```powershell
# Requires Godot 4: set GODOT=C:\path\to\Godot.exe if needed
py tools/xware/ai/playtest_run.py --project . --seconds 12 --mode orbit
py tools/xware/ai/playtest_improve_loop.py --project . --rounds 2
# or one-shot with elevate:
py tools/xware/ai/experience_elevate.py --project . --from-intent --playtest-improve
```

## Source of truth

HelixProtocol `addons/xware` + `tools/xware`. **Version 3.0.0**
