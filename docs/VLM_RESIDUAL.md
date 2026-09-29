# VLM residual (3.7) — measure before hard gate

## Policy

| Mode | Meaning |
|------|---------|
| **heuristic** | Frame metrics from `screen_record_analyze.py` (always) |
| **vlm_advisory** | Multimodal or offline_proxy scores — **do not** flip elevate PASS |
| **hard_gate** | Only after `vlm_calibration_latest.json` → `hard_gate_recommended=true` |

Dual residual (DECISIONS_4.0 D5).

## CLI

```powershell
# Harvest frames + advisory scores
py tools/xware/ai/vlm_residual.py --project . --measure

# Force offline proxy (no XAI call)
py tools/xware/ai/vlm_residual.py --project . --measure --no-api

# Queue frames for Grok agent vision review
py tools/xware/ai/vlm_residual.py --project . --write-agent-jobs

# Compare heuristic vs VLM
py tools/xware/ai/vlm_residual.py --project . --calibrate
```

Optional: `XAI_API_KEY` + vision model for live scores (`provider=xai_vision`).

## Keys

- `vlm_silhouette_not_primitive`
- `vlm_surface_read`
- `vlm_contact_ground`
- `vlm_motion_readable`
- `vlm_photoreal_overall`
- `vlm_kitbash_risk` (high = bad)

## Reports

- `assets/xware_reports/vlm_residual_latest.json`
- `assets/xware_reports/vlm_calibration_latest.json`
- `addons/xware/ai/vlm_job_queue.json` (agent jobs)

## Hard-gate checklist

1. Measure on ≥20 internal clips  
2. Calibrate mean_abs_err &lt; 0.15 vs heuristic on shared keys  
3. Prefer real provider (xai_vision or agent_multimodal), not offline_proxy alone  
4. Only then set hard_gate in config (future flag)
