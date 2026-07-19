# xAI Plugin Marketplace — PR materials for XWare

**Plugin repo:** https://github.com/tylercollex-gif/xware-grok-plugin  
**Pinned SHA (main):** `435112fb632020ee256d46dd61644f71873a56c1`  
**Catalog:** https://github.com/xai-org/plugin-marketplace  

---

## Exact `marketplace.json` entry

Add this object to the `plugins` array in  
`.grok-plugin/marketplace.json`  
(same shape as vercel / sentry / chrome-devtools):

```json
{
  "name": "xware",
  "description": "XWare 3.0 — Grok agent for solo indie 3D Godot game creation. Experience Elevate, Character Engine, playtest improve loops, continuous learning. Spawn subagent_type=xware.",
  "category": "development",
  "source": {
    "source": "url",
    "url": "https://github.com/tylercollex-gif/xware-grok-plugin.git",
    "sha": "435112fb632020ee256d46dd61644f71873a56c1"
  },
  "homepage": "https://github.com/tylercollex-gif/xware-grok-plugin",
  "keywords": [
    "xware",
    "godot",
    "godot 3d",
    "game",
    "gamedev",
    "indie",
    "3d game",
    "graphics",
    "animation"
  ]
}
```

---

## PR title

```
Add xware plugin (Godot 3D game design agent)
```

---

## PR body (copy-paste)

```markdown
## Summary

Adds **xware** to the official Grok Build plugin marketplace.

XWare is a Grok agent + skill pack for **solo indie 3D Godot** game creation:

- `subagent_type="xware"` for elevates without thrashing parent context
- Experience Elevate (all object classes: characters, props, buildings, weapons, craft, env)
- Character Engine (form + dual-track motion)
- Screen-record residual + automated playtest improve loops
- Continuous local learning hub (anonymized aggregates)

## Source

| Field | Value |
|-------|--------|
| Repo | https://github.com/tylercollex-gif/xware-grok-plugin |
| Pin SHA | `435112fb632020ee256d46dd61644f71873a56c1` |
| Category | `development` |

## Install (after merge)

```bash
grok plugin install xware --trust
# or until catalog name resolves:
grok plugin install tylercollex-gif/xware-grok-plugin --trust
```

Confirm: `/config-agents` shows **xware**.

## Checklist

- [x] Public plugin repo
- [x] `plugin.json` validates (`grok plugin validate`)
- [x] Remote source pinned to full 40-char SHA
- [x] LICENSE (MIT)
- [ ] `python3 scripts/generate-plugin-index.py`
- [ ] `python3 scripts/validate-catalog.py`
- [ ] CI green / code-owner review

## Notes

- Plugin surface is lean (agent + skill + role only). Godot runtime (`addons/xware` + `tools/xware`) installs into games separately via the game SOT install script documented in the plugin README.
- No commercial asset rips; legal Imagine direction + generated/CC0 only.
```

---

## Step-by-step on GitHub

### 1. Fork

1. Open https://github.com/xai-org/plugin-marketplace  
2. Click **Fork** → your account (`tylercollex-gif`)  
3. Clone your fork:

```powershell
cd $env:USERPROFILE\Documents
git clone https://github.com/tylercollex-gif/plugin-marketplace.git
cd plugin-marketplace
git remote add upstream https://github.com/xai-org/plugin-marketplace.git
git fetch upstream
git checkout -b add-xware-plugin
git reset --hard upstream/main
```

### 2. Edit catalog

Open `.grok-plugin/marketplace.json`.  
Append the **xware** object (above) inside the `"plugins": [ ... ]` array  
(add a comma after the previous last plugin entry).

### 3. Regenerate index (required)

```powershell
# Needs Python 3
python scripts/generate-plugin-index.py
python scripts/validate-catalog.py
```

If scripts need network access to fetch the pinned SHA, that is expected.

### 4. Commit and PR

```powershell
git add .grok-plugin/marketplace.json .grok-plugin/plugin-index.json
git commit -m "Add xware plugin (Godot 3D game design agent)"
git push -u origin add-xware-plugin
```

Then on GitHub: **Compare & pull request** into `xai-org/plugin-marketplace` **main**.  
Paste the PR body from this file.

### 5. After merge

Users can install from the official marketplace. When you update the plugin later, bump only the `sha` field in a new PR.

---

## Verify pin still matches (before PR)

```powershell
cd C:\Users\winge\Documents\Xware\grok-plugin
git rev-parse HEAD
# Must equal: 435112fb632020ee256d46dd61644f71873a56c1
# If you pushed new commits, update the SHA in marketplace.json
```

