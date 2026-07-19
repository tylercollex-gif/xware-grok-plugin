# xAI Plugin Marketplace — XWare pin + Engine Improve

**Plugin repo:** https://github.com/tylercollex-gif/xware-grok-plugin  
**Marketplace PR:** https://github.com/xai-org/plugin-marketplace/pull/110  
**Catalog:** https://github.com/xai-org/plugin-marketplace  

## Why pin bumps matter (race)

The marketplace entry is a **fixed SHA**. New densify laws, residual floors, and continuous-learning agent contracts only reach marketplace installers after you:

1. Push this plugin repo  
2. Update `source.sha` on the marketplace entry  

Local multi-game hub learning still works on each machine without a pin bump; **new** installs only get the new agent laws after pin update.

## After each engine win

```powershell
# 1) Sync agent/skill from SOT if needed, bump plugin.json version
# 2) Commit + push tylercollex-gif/xware-grok-plugin
# 3) Get full SHA:
#    git rev-parse HEAD
# 4) Edit marketplace.json plugins[] entry for "xware":
```

```json
{
  "name": "xware",
  "description": "XWare Xhance 3.2 — full xAI/Grok power for solo indie 3D Godot. Experience Elevate, Character Engine, playtest loops, continuous learning hub, Imagine look skills. Spawn subagent_type=xware. Slash: /xware-xhance /xware-elevate.",
  "category": "development",
  "source": {
    "source": "url",
    "url": "https://github.com/tylercollex-gif/xware-grok-plugin.git",
    "sha": "REPLACE_WITH_FULL_40_CHAR_SHA"
  },
  "homepage": "https://github.com/tylercollex-gif/xware-grok-plugin",
  "keywords": [
    "xware",
    "xhance",
    "godot",
    "godot 3d",
    "game",
    "gamedev",
    "indie",
    "3d game",
    "graphics",
    "animation",
    "continuous-learning",
    "xai"
  ]
}
```

## Install (users)

```bash
grok plugin install tylercollex-gif/xware-grok-plugin --trust
```

Confirm: `/config-agents` shows **xware**.

## Privacy

Continuous learning packs are **anonymized aggregates only** (profile, weak role counts, residual key rates). No meshes, paths, or textures. Cloud share is opt-in.
