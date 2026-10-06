# Decision record — XWare 4.0 Studio Power

**Date:** 2026-07-21  
**Baseline:** 3.6.0 soft launch  
**Plan:** Research “team of 50” powerhouse  

## D1 — Phase 2 multi-engine depth

| Choice | **Unity URP** |
|--------|----------------|
| Status | **Accepted (default)** |
| Why | Existing Editor menus + GLB postprocessor; faster path to auto-import + materials than UE Content Browser |
| Unreal | Remains stage MVP until 4.1+ |
| Godot | Remains full reference depth |

## D2 — External mesh APIs (Meshy/Tripo/Rodin-class)

| Choice | **4.1** (not 4.0 core) |
|--------|-------------------------|
| Status | **Accepted (default)** |
| Why | Residual honesty + legal gates first; avoid coupling 4.0 to third-party SLA |
| 4.0 | Design adapter interface only (stub OK) |

## D3 — Scope intensity

| Choice | **3.7 residual + CI first → 4.0 studio graph** |
|--------|-----------------------------------------------|
| Status | **Accepted (default)** |
| Why | Measure perceptual residual before parallel agent complexity |

## D4 — Genre proofs for next release train

| Choice | **factory_sim deepen + sports** |
|--------|----------------------------------|
| Status | **Accepted (default)** |
| Why | Idle already factory-proven; Soccer3D sports profile field-tested; expands immersion recipes without new architecture |

## D5 — Vision residual approach

| Choice | Dual residual: **heuristic primary + optional VLM advisory → hard after calibration** |
|--------|----------------------------------------------------------------------------------------|
| Status | **Accepted** |
| Why | Industry score-theater risk; VLM flaky until measured on internal clips |

## D6 — Marketing

| Choice | No public market push until product bar + human G3 |
|--------|-----------------------------------------------------|
| Status | **Standing policy** |
| Soft launch 3.6 | GitHub + marketplace pin only (done) |

## D7 — Ship bar + test standard (from Flagfall)

| Choice | **Godot 4 Forward+ to Steam; lean tests; owner OK before publish** |
|--------|-------------------------------------------------------------------|
| Status | **Accepted (owner rules)** |
| Why | Addons xware + GodotSteam only; Imagine + material_pack + residual look path; bundled Poly Haven CC0 only. Tests: ~1-minute smoke + fast headless checks; anything untested is UNVERIFIED. Checked by `skills/xware-ship` (doctor). |

## Open decisions (revisit)

- VLM provider binding (Grok multimodal vs offline)  
- Nightly CI host (local scheduler vs GitHub Actions self-hosted)  
- ~~Whether `studio_raise` is a new CLI or experience_elevate flag~~ Resolved in 4.0.2: `xware_raise.py` runs `studio_raise` by default; `--legacy` runs experience_elevate.  

## Change log

| When | Change |
|------|--------|
| 2026-07-21 | Initial record from research plan approval defaults |
| 2026-10 | D7 ship bar + xware-ship doctor; studio_raise CLI question resolved (power push) |
