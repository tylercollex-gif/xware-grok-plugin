# XWare Studio Agents — “team of 50” leverage without 50 chatbots

**Product line:** Xhance 3.7 → 4.0 Studio Power  
**Law:** Every role must bind to a **real kernel** (CLI/runtime). Personas without tools are forbidden.

## Thesis

A 50-developer studio is a **graph of specialists + tools + QA + memory**.  
XWare maps that graph onto Grok Build:

| Studio idea | XWare implementation |
|-------------|----------------------|
| Departments | Specialist roles (below) |
| DCC / tools | Kernels (`meshgen`, Imagine, Motion OS, …) |
| Leads / TD | Director orchestrator |
| QA | Residual + quality_gate + playtest |
| Institutional knowledge | Hub packs `~/.grok/xware_network` |
| External contractors | Optional mesh APIs (4.1), legal + residual re-check |

**Concurrency cap (default):** 4 parallel specialists. Sequential fallback when context/cost tight.

---

## Role matrix (12 core + 6 optional)

### Core (automate in 3.7–4.0)

| ID | Role | Kernel / CLI | Residual keys owned | Spawn default |
|----|------|--------------|---------------------|---------------|
| `director` | Technical Director | `experience_elevate.py`, `studio_raise` (future) | overall PASS | always |
| `form` | Tech artist — form | `generate_models.py`, PH-first, `form_analyze.py` | geo_density, anti_kitbash, prop_silhouette_not_box, lod_companion | auto |
| `look` | Lookdev | `imagine_raise.py`, `apply_ai_textures.py`, `material_pack.py` | surface_read, prop_surface_read, pbr_triple, wear_layer_present | auto |
| `character` | Character lead | `character_engine.py`, hierarchy | human residual suite, FaceKit keys | if expects_humans |
| `motion` | Animator | `motion_os.py`, bake, `anim_quality_gate.py` | motion residual suite | if motion_critical_roles |
| `env` | Environment TD | `presentation_pass.py --apply`, light_kit, env_builder | contact_shadow, ambient, prop_contact_ground | auto |
| `setdress` | Set dresser | `immersion_plan.py`, scatter API | setdress_density_ok, wear | auto |
| `physics` | Physics TD | physics_audit in elevate, `physics_util.gd` | collision, mass, surface coverage | auto |
| `qa` | QA lead | `quality_gate.py`, `object_analyze --prop-vision`, playtest | all gates; blocks PASS | always last |
| `learn` | Learning officer | `continuous_learn.py`, harvest, learn_probe | hub pack validity | always after qa |
| `safety` | Legal / safety | `xware_safety`, no-copycat skill | pack allowlist, no paths | always |
| `engine` | Multi-engine lead | unity/unreal elevate, stage | engine tag, stage reports | if engine ≠ godot |

### Optional (4.0+ / profile-triggered)

| ID | Role | When |
|----|------|------|
| `craft` | Craft/vehicle specialist | space_arcade / racing |
| `ui` | UI pack | profile has UI packs |
| `audio` | Audio stub | out of core 4.0 |
| `narrative` | Inspiration/direction only | never invent IP rips |
| `perf` | Performance / LOD | mobile or factory_safe |
| `vlm` | Perceptual residual judge | 3.7+ when VLM enabled |

---

## Spawn contract (Director)

```
spawn_subagent(
  subagent_type="xware",
  description="XWare studio raise",
  isolation="none",
  prompt="""
Project: <path>
Engine: godot|unity|unreal|ASK
Profile: <or auto>
Mode: studio_raise
Roles: director,form,look,setdress,env,physics,qa,learn,safety
  + character if expects_humans
  + motion if motion_critical_roles
  + engine if not godot
Concurrency: 4
Constraints: legal only; residual honest; PH-first heroes; hub pack after qa;
  never invent second graphics OS; never market unless approved.
Return: department pass/fail table + report paths.
"""
)
```

### Execution order (DAG)

```text
safety (policy load)
   │
director (intent + DNA + budget)
   │
   ├── form ────────┐
   ├── look ────────┤  (parallel up to 4)
   ├── character ───┤
   ├── motion ──────┤
   ├── setdress ────┤
   ├── env ─────────┤
   └── physics ─────┘
           │
          qa  (blocks overall PASS)
           │
         learn
```

Rework loop: QA FAIL → only the owning department re-runs (class routing via `weak_key_taxonomy.json`).

---

## Department exit codes (proposal)

| Code | Meaning |
|------|---------|
| 0 | Department PASS |
| 1 | Soft residual (advisory) |
| 2 | Hard residual FAIL |
| 3 | Missing evidence (e.g. no video for human residual) |

Overall elevate PASS only if all **required** departments are 0 or 1, and **no** required department is 2/3.

---

## What “50 developers” maps to

| Headcount fiction | Real XWare coverage |
|-------------------|---------------------|
| 8 tech artists | form + look + PH + Blender guidelines + optional mesh API |
| 5 character artists | character_engine + residual video |
| 4 animators | Motion OS + bake + gate |
| 5 environment | env + setdress + light residual |
| 4 QA | quality_gate + prop-vision + playtest + CI goldens |
| 4 tools/CI | install scripts + golden suite + SIS gate |
| 3 multi-engine | one deep path + stage other |
| 2 producers | director role + genre DNA |
| 5 juniors / fill | hub learn + auto_weak_elevate |
| 10 specialists (audio, netcode, …) | **out of core** until profile-critical |

**~50 leverage units** ≈ **12 automated roles × deep kernels × multi-game hub memory**, not 50 empty agents.

---

## Non-goals

- 48 persona agents that only write markdown  
- Departments without residual ownership  
- Silent multi-user learning  

---

## Implementation track

| Version | Deliverable |
|---------|-------------|
| 3.7 | Role matrix + **`studio_raise.py`**; kitbash hard gates; CI goldens; **`vlm_residual.py` measure**; Unity Phase 2 menus |
| 4.0 | Deeper parallel graph; place graph v2; VLM hard-gate after calibration |
| 4.1 | External mesh contractor adapters |

### CLI (3.7)

```powershell
py tools/xware/ai/studio_raise.py --project . --with-vlm
py tools/xware/ai/vlm_residual.py --project . --measure --calibrate
py tools/xware/ai/unity_elevate.py --project <Unity> --phase2
```

Related: `AGENT.md`, `IMMERSION.md`, `SIS_XWARE.md`, `MULTI_ENGINE.md`, decision record `import/DECISIONS_4.0.md`.
