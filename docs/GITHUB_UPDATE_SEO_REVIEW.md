# GitHub update — SEO review (do not publish yet)

**Status:** draft only. Nothing is committed or pushed. Edit this file, then say **publish** (or paste a revised README) and I will apply it to `README.md` + `plugin.json` and wait for your push OK.

**Repo:** https://github.com/tylercollex-gif/xware-grok-plugin  
**This file:** public landing copy only. Street-slice runtime (scatter HLOD, `quality_gate` UNKNOWN, Godot scene) lives in the tools/addon SOT, not this plugin zip.

---

## GitHub About (sidebar, ~160 characters)

Proposed:

```
XWare Xhance — Godot 4 3D elevate for Grok. studio_raise, 360-class street density, residual honesty. MIT. Spawn subagent_type=xware.
```

Character count: 141.

Alt if you want “Xbox” in the snippet:

```
Godot 4 Xhance for Grok Build. 360-class 3D density, studio_raise, local learning hub. Official XWare. Free MIT.
```

---

## GitHub Topics (repo Settings → Topics)

Proposed replace/add (searchable):

`xware` `xhance` `godot` `godot4` `godot-4` `3d` `gamedev` `indie-game` `grok` `grok-build` `xai` `studio-raise` `forward-plus` `continuous-learning`

Drop from topics if present: `photoreal` `nanite` (we do not claim those).

Keep `unity` / `unreal` only if you still want marketplace discovery for MVP engines — **do not** put them in the H1 or first paragraph.

---

## plugin.json (marketplace + `grok plugin install` blurb)

Proposed `description` (leads with Godot + studio_raise, not leftover elevate):

```
XWare Xhance 4.0.2 — Godot 4 3D elevate for Grok. Default studio_raise, 360-class density, scatter after immersion_plan, residual recordings. Spawn subagent_type=xware. Free MIT.
```

Proposed `keywords` (SEO for plugin search; no photoreal lead):

```json
[
  "xware",
  "xhance",
  "godot",
  "godot4",
  "godot 4",
  "godot 3d",
  "3d",
  "gamedev",
  "indie",
  "graphics",
  "studio_raise",
  "grok",
  "grok-build",
  "xai",
  "continuous-learning",
  "forward-plus"
]
```

Unity/Unreal keywords omitted from this draft on purpose so Google/GitHub rank **Godot 4 XWare**. Add them back under a “Also MVP” line in README if you want.

---

## Proposed commit (after you approve copy)

```
Release notes: Godot 4 Xhance landing — studio_raise default, 360-class density SEO
```

Body:

```
Public README + plugin.json: Godot 4 first, studio_raise default, 360-class street bar.
Does not claim photoreal, Nanite, or leftover experience_elevate as the path.
```

---

## Proposed README.md

Copy below the line is the file GitHub will index. Edit freely.

---

```markdown
# XWare Xhance for Godot 4

**Godot 4 3D elevate on Grok Build.** Official **XWare / Xhance** agent: `studio_raise`, 360-class street density, residual honesty, local learning hub.

**Creator:** [tylercollex-gif](https://github.com/tylercollex-gif) · **License:** MIT · **Marks:** [TRADEMARK.md](TRADEMARK.md)

Install:

```powershell
grok plugin install tylercollex-gif/xware-grok-plugin --trust
```

Then `/config-agents` → **xware** ON. Spawn `subagent_type="xware"`.

## What XWare is

Xhance is the efficient path to raise a **Godot 4** (Forward+) indie 3D game from Grok CLI — not a render-engine swap.

| Default raise | Look law | Residual |
|---------------|----------|----------|
| `studio_raise` (`xware_raise.py`) | Direction card `gta_v_360` — 360-class density, grit, readable silhouettes | Editor **recording** on a real GPU window (Movie Maker / playtest). Stills do not pass. |

Quality gate stays **UNKNOWN** until the Godot project has a **playable scene** and a **recording**.

## Install and raise (Grok CLI)

Cwd = your Godot project (plugin enabled):

```powershell
grok plugin install tylercollex-gif/xware-grok-plugin --trust
# Runtime from your XWare tools checkout:
powershell -File tools\xware\install_to_project.ps1 -Target <GodotGame> -Profile street_slice
py tools/xware/ai/studio_raise.py --project . --with-vlm
```

```
spawn_subagent(
  subagent_type="xware",
  prompt="""
Project: <absolute Godot path>
Engine: godot
Profile: street_slice
Task: studio_raise
Look: gta_v_360
Constraints: legal only; residual is a recording; no photoreal claim.
"""
)
```

Ask engine only when the game is **new** or the engine is **unknown**.

**Use official XWare — do not regenerate** ([AI_USE_POLICY.md](AI_USE_POLICY.md)).

## 360-class street bar (honest wrap)

**XWare wraps**

- Scatter after `immersion_plan` (budget for a city block, `visibility_range` HLOD on spawned props)
- Playtest / quality_gate
- Movie Maker residual on a real GPU window

**Godot’s — leave them**

Jolt · Forward+ · Generate LODs (importer).

**Extra, not what makes a street read**

FaceKit · Motion OS.

**Not wired for this bar**

SDFGI · Poly Haven API fill · interior VoxelGI / Lightmap bake.

Fog and camera far/visibility End on a street slice are Godot Environment + Camera3D.

## Runtime CLIs (tools checkout)

Marketplace zip = **agent + skills**. Meshgen / elevate live in your tools SOT:

```powershell
py tools/xware/ai/immersion_plan.py --project <path> --apply-generate
py tools/xware/ai/studio_raise.py --project <path> --with-vlm
py tools/xware/ai/quality_gate.py --project <path> --profile street_slice
py tools/xware/ai/continuous_learn.py --project <path>
```

Godot after plan: `XWare.apply_immersion_scatter(scene)`.

See [XHANCE.md](XHANCE.md) · [MULTI_ENGINE.md](MULTI_ENGINE.md)

## Continuous learning

Privacy-safe aggregates so the next raise is smarter. Hub: `~/.grok/xware_network/`. Cloud **opt-in**.  
[LEARN_NETWORK.md](LEARN_NETWORK.md) · [PRIVACY.md](PRIVACY.md)

| Shared | Never shared |
|--------|----------------|
| Profile, residual rates, weak classes | Paths, usernames, saves |
| Score buckets, version | Meshes, textures, source |

## Showcase

Clips under [`marketing/`](marketing/) — look and gameplay only.

## Authorship

| | |
|--|--|
| Creator | tylercollex-gif |
| License | MIT — free use with attribution |
| Marks | XWare / Xhance reserved ([TRADEMARK.md](TRADEMARK.md)) |
| Plugin | [`plugin.json`](plugin.json) **4.0.2** |

## Keywords

`xware` · `xhance` · `godot 4` · `godot 3d` · `gamedev` · `indie` · `studio_raise` · `grok-build` · `forward-plus` · `continuous-learning`
```

---

## SEO notes (for your edit)

1. **H1 is “Godot 4”** so GitHub + Google match “godot 4 3d grok” / “xware xhance”.
2. **First sentence** repeats XWare, Xhance, Godot 4, Grok, 360-class, studio_raise.
3. **No “photoreal”** in title, About, or keywords (card forbids it).
4. **“GTA”** appears only as internal card id `gta_v_360`, not in H1 (trademark-safe public language: “360-class”).
5. **Install command** is in the first screenful (GitHub conversion + marketplace).
6. Unity/Unreal are not in the lead; they stay in MULTI_ENGINE.md if you still ship MVP.

When this copy is right, reply with edits or **publish README**. I will not `git push` until you say so.
