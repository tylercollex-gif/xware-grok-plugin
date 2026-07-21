# Immersion — Props, set dressing, place density

**Internal product readiness.** Do not market until explicit approval.

## Goal

Games elevated by XWare should feel **lived-in**: props, clutter, contact, and density — not empty stages with a few crates.

## Loop

```powershell
# Baseline (multi-game)
py tools/xware/ai/immersion_baseline.py --project .

# Plan place density from genre DNA (+ optional meshgen)
py tools/xware/ai/immersion_plan.py --project . --profile factory_sim
py tools/xware/ai/immersion_plan.py --project . --apply-generate --detail 10

# Prop residual (includes prop-vision keys)
py tools/xware/ai/object_analyze.py --project . --prop-vision --write-report

# Presentation residual apply recipe (Godot runtime consumes)
py tools/xware/ai/presentation_pass.py --project . --apply

# Full elevate (World Object → Immersion → Look → Presentation --apply)
py tools/xware/ai/experience_elevate.py --project . --from-intent --immersion-generate
```

## Godot runtime

```gdscript
const XWare = preload("res://addons/xware/api/xware.gd")

# After immersion_plan wrote immersion_spawn_recipe.json:
XWare.apply_immersion_scatter(self)  # or get_tree().current_scene
XWare.apply_presentation_residual(self)
# Contact-only (shadows + SSAO + soft fill):
XWare.apply_contact_light_fix(self, {"ensure_fill": true})
```

Editor dock: **Immersion plan + scatter recipe** · **Apply immersion scatter (scene)** · **Presentation residual apply**

## Prop-vision residual keys

| Key | Routes to | Meaning |
|-----|-----------|---------|
| `prop_silhouette_not_box` | form | Anti-kitbash / multi-part read |
| `prop_surface_read` | material | PBR / surface readability |
| `prop_contact_ground` | light / physics | Grounded contact proxy |
| `setdress_density_ok` | form / immersion_plan | Place density vs genre target |
| `wear_layer_present` | material | Wear / grit / rust read (soft unless DNA requires `wear`) |

Taxonomy: `addons/xware/form/weak_key_taxonomy.json`.

## Setdress layers

| Layer | Examples |
|-------|----------|
| L0 heroes | dumpster, pallet, barrier, sign, pipe stack |
| L1 industrial | cable spool, crate stack, barrel cluster, tool cart |
| L2 smalls | traffic cone (+ PH smalls) |

Generate: `py tools/xware/meshgen/generate_models.py --setdressing --quality ultra --detail 10 --copy-generated`

## PH-first elevate

World Object densify prefers **Poly Haven `ph_*` meshes** when a keyword sibling exists (e.g. `prop_barrier` → `ph_concrete_barrier`) before procedural meshgen, then SOT-copy.

## Scatter + wear contact

| Piece | Path |
|-------|------|
| Scatter runtime | `addons/xware/environment/setdress_scatter.gd` |
| Recipe | `assets/xware_reports/immersion_spawn_recipe.json` |
| Contact decals | `XWare.spawn_floor_decal` under each instance (budget 36) |
| Root node | `XWareImmersionRoot` (replaced on re-apply) |

## Genre DNA

```json
"immersion": {
  "place_types": ["factory_floor"],
  "clutter_density": 6,
  "required_layers": ["hero", "industrial", "smalls", "wear"],
  "default_prop_surface": "painted_metal"
}
```

Shipped first: `factory_sim`, `open_world_rpg_slice`, `space_arcade`.

## Config (`xware_config.cfg`)

```ini
[immersion]
enabled=true
scatter_on_elevate=true
contact_decals=true
wear_decals=true
presentation_residual_apply=true
max_instances=48
```

## Multi-game immersion surge

```powershell
# All local XWare games: sync policies + setdress generate + plan + prop vision + learn
py tools/xware/ai/immersion_surge.py --project .
py tools/xware/ai/immersion_surge.py --project . --game IdleFoodFactory
py tools/xware/ai/immersion_surge.py --project . --skip-generate   # plan only
py tools/xware/ai/immersion_surge.py --project . --stage-engines   # + Unity/Unreal stage
py tools/xware/ai/immersion_surge.py --project . --dry-run
```

Report: `assets/xware_reports/immersion_surge_latest.md`

## Unity / Unreal prop staging (MVP)

Full scatter is **Godot-first**. Engine MVP stages densified setdress GLBs + PBR into Generated:

```powershell
# Discover under Documents, or pass paths
py tools/xware/ai/immersion_stage_engines.py --project . --discover --generate
py tools/xware/ai/immersion_stage_engines.py --unity C:\path\to\UnityProject
py tools/xware/ai/immersion_stage_engines.py --unreal C:\path\to\UEProject

# Via elevate entrypoints
py tools/xware/ai/unity_elevate.py --project C:\UnityGame --immersion
py tools/xware/ai/unreal_elevate.py --project C:\UEGame --immersion
```

| Engine | Output |
|--------|--------|
| Unity | `Assets/XWare/Generated/Meshes` + `Reports/immersion_stage_latest.md` |
| Unreal | `Content/XWare/Generated/Meshes` + import todo |

Then import in Editor (XWare menus / Content Browser). No runtime scatter on Unity/Unreal yet.

## Continuous learn

Hub packs may include aggregates only:

- `setdress_density_mean`
- `immersion_pass`
- `prop_vision_pass`
- residual fail keys for prop_* (no paths / no mesh names)

## Reports

| File | Purpose |
|------|---------|
| `immersion_baseline.md` | Phase 0 multi-game |
| `immersion_plan_latest.json` | Dress budget + instances |
| `immersion_spawn_recipe.json` | Spawn list for Godot scatter |
| `object_analyze_latest.json` | Includes `prop_vision` |
| `presentation_apply_latest.json` | Residual light/presentation apply recipe |

## Marketing gate

No trailers, marketplace pin bumps, or public promo for immersion until maintainer approval.
