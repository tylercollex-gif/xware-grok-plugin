---
name: xware-elevate
description: >
  One-shot XWare Experience Elevate for a Godot 3D project: design intent, densify,
  materials, motion, residual, continuous_learn. Prefer when user says raise, elevate,
  photoreal pass, or XWare improve this game.
metadata:
  short-description: "XWare Experience Elevate one-shot"
---

# XWare Elevate

```powershell
$proj = "<Godot project root>"
# tools from game or Helix SOT
py tools/xware/ai/design_intent.py --project $proj
py tools/xware/ai/experience_elevate.py --project $proj --from-intent --quality ultra --detail 10
py tools/xware/ai/continuous_learn.py --project $proj --skip-elevate
py tools/xware/ai/quality_gate.py --project $proj
```

Spawn `subagent_type="xware"` with Task `experience_elevate` when the loop is multi-file.
