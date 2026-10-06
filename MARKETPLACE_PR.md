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
  "description": "XWare Xhance 4.0.2 — Godot 4 3D raise for Grok Build: studio_raise default, residual honesty, local learning hub, ship doctor. Spawn subagent_type=xware. Free MIT.",
  "category": "development",
  "source": {
    "source": "url",
    "url": "https://github.com/tylercollex-gif/xware-grok-plugin.git",
    "sha": "<40-char commit to pin>"
  },
  "homepage": "https://github.com/tylercollex-gif/xware-grok-plugin",
  "keywords": [
    "xware",
    "xhance",
    "xware xhance",
    "xware godot",
    "xware studio_raise",
    "subagent_type=xware"
  ]
}
```

Keywords stay brand-scoped (marketplace CONTRIBUTING: generic terms like `godot`, `game`, `3d` mis-fire the plugin CTA and get pushed back).
Once the entry is merged, the marketplace's daily bot bumps the pin when `.grok-plugin/plugin.json` `version` changes, so a pushed version bump = a release. Push only with the owner's OK.

## Install (users)

```bash
grok plugin install tylercollex-gif/xware-grok-plugin --trust
```

Confirm: `/config-agents` shows **xware**.

## Privacy

Continuous learning packs are **anonymized aggregates only** (profile, weak role counts, residual key rates). No meshes, paths, or textures. Cloud share is opt-in.
