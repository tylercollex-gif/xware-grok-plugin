# Multi-engine (product)

XWare elevate tools support:

| Engine | Status |
|--------|--------|
| **Godot 4** | Full Experience Elevate |
| **Unity (URP)** | MVP — densify meshes + PBR stage; Editor import menus |
| **Unreal Engine 5** | MVP — stage GLB/PBR under Content/XWare; import in editor |

## Agent

```
spawn_subagent(subagent_type="xware", …)
# Prompt may include: Engine: auto | godot | unity | unreal
```

## CLI (from XWare SOT tools, not this plugin repo alone)

```powershell
py tools/xware/ai/experience_elevate.py --project <path> --engine auto --from-intent
```

## Honesty

- FaceKit / full Motion OS / automated playtest: **Godot-first**  
- No Nanite/Lumen claims  
- Engine licenses (Unity, Epic) remain the user’s responsibility; XWare tools are MIT  

Marketing: look/gameplay only — not internal safety mechanics.
