# Blastar3D × XWare — marketing recordings

Legal-only **from-scratch** 3D Blastar (1984 arcade homage) built with **XWare 3.0** `space_arcade` profile.  
No commercial rips — generated hero GLBs + GDScript gameplay.

## Clips

| File | Duration (approx) | What it shows |
|------|-------------------|---------------|
| `01_xware_craft_fighter_orbit.mp4` | ~4–8s | Blender orbit turntable of **blastar_ship** ultra hero (fighter) |
| `02_xware_craft_freighter_orbit.mp4` | ~4–8s | Orbit turntable of **blastar_freighter** (enemy cargo craft) |
| `playtest_orbit_engine.mp4` | ~12s | In-engine XWare playtest scene (orbit mode, 1280×720 @ 24fps) |
| `playtest_main_showcase.mp4` | ~10s | Live **main.tscn** — CRT green-phosphor HUD / deep-space arena boot |
| `03_xware_plugin_trailer.mp4` | ~25s | Plugin trailer: title → craft orbits → play footage → end card |

Copies also live under:

- `C:\Users\winge\Documents\Xware\grok-plugin\marketing\`
- `addons/xware/ai/inbox_recordings/` (for residual harvest)

## How XWare built this game

| Stage | Tool | Result |
|-------|------|--------|
| Design Intent | `design_intent.py --profile space_arcade` | Pillars: craft mastery, readable threats, arcade pace |
| Hero craft | `blastar_models.py --quality ultra` | ship, freighter, rocket, beam, debris GLBs |
| Gameplay | GDScript under `scenes/` + `scripts/` | Classic Blastar loop from empty project |
| Experience Elevate | `experience_elevate.py --from-intent --playtest-improve` | World objects densified, materials, motion OS, presentation |
| Quality Gate | `quality_gate.py --profile space_arcade` | **PASS rc=0** (hero avg 100, gate graphics met) |
| Residual video | `proof_record_orbit.py` + `screen_record_analyze.py` | motion≈0.14, pass=True |

**Profile:** `space_arcade`  
**Project:** `C:\Users\winge\Documents\Blastar3D`  
**Godot:** 4.7.1

## Suggested social / marketplace captions

**Short**

> Empty Godot folder → playable 3D Blastar with XWare 3.0.  
> `spawn_subagent(subagent_type="xware")` · profile `space_arcade`

**Medium**

> XWare is the solo-indie 3D Godot OS: design intent, ultra craft heroes, materials, motion, physics audit, playtest improve loop — then a quality gate that actually means something.  
> This trailer is a from-scratch Blastar homage (legal generated meshes only).

**Technical**

> Pipeline: design_intent → blastar_models ultra → experience_elevate --playtest-improve → quality_gate space_arcade → proof_record_orbit + write-movie.  
> Residual honesty is video-first (orbits + playtest recordings).

## Controls (game)

- **WASD / Arrows** — move  
- **Space** — fire  
- **Y / N** — menus (instructions / play again)

## Legal

Homage to Elon Musk’s 1984 Blastar listing only. No commercial asset rips. CC0 / generated meshes and XWare PBR inbox textures.
