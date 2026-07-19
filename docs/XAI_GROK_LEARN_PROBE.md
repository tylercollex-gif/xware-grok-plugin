# Partnership proposal: Grok Build × XWare continuous improve probe

**To:** xAI Grok Build / Plugin Marketplace / Games tooling  
**From:** tylercollex-gif (XWare / Xhance)  
**Plugin:** https://github.com/tylercollex-gif/xware-grok-plugin  
**Status:** Public proposal · consent-first · privacy-preserving  
**Date:** 2026

---

## 1. Executive summary

**Grok Build is generating more 3D games.**  
**XWare** is a third-party marketplace agent specialized in **solo indie 3D elevate** (Godot 4 full path; Unity URP & Unreal 5 MVP).

**Ask:** Add an optional, **user-visible** post-task **learn probe** when Grok completes 3D game create/raise work, so quality signals can improve specialized game agents (including XWare) **without** ever sending meshes, source, saves, or paths.

**Outcome for xAI:** Better 3D game results in Grok Build over time, stronger marketplace ecosystem, clear privacy story.  
**Outcome for XWare:** Densify/residual routing improves as Grok’s game volume grows.  
**Outcome for users:** Opt-in only; transparent; their games stay private.

---

## 2. Problem

| Today | Gap |
|-------|-----|
| Grok creates many 3D projects | No standard, private signal that “a game was made / raised” |
| XWare can learn **locally** and via **opt-in fleet** | Cannot see other users’ work without a **platform** channel |
| Silent multi-user scraping | **Unacceptable** — not requested, not proposed |

A plugin cannot (and must not) silently read other users’ projects.  
A **platform probe** is the legitimate way for the ecosystem to learn at Grok scale.

---

## 3. Proposal (three delivery options)

### Option A — Preferred: Grok Build setting + event (first-party)

1. User setting (default **off** or first-run prompt):  
   **“Help improve Grok 3D game tools (anonymous aggregates only)”**
2. On task complete for 3D game bootstrap / elevate / densify-like work, emit one **aggregate event**.
3. xAI may:
   - store aggregates first-party to improve Grok game skills, and/or  
   - allow installed plugins that declare `learn_probe_v1` to receive the **same** event locally.

### Option B — Plugin-local write when XWare is installed

If the user has XWare installed **and** local learn is enabled:

- Grok writes a pack into the user’s XWare hub path  
  (`~/.grok/xware_network/`) via documented schema only.

No network call required for this option.

### Option C — Opt-in HTTPS to maintainer (already client-ready)

XWare already has an **opt-in** client (`fleet_learn.py`) that POSTs **validated** packs to a user-configured HTTPS URL.

Platform can document:

- event shape = XWare pack v2, and  
- users may point fleet URL at xAI or maintainer endpoints **after consent**.

---

## 4. Event schema (privacy-safe)

Compatible with XWare `xware_feedback_network_v2` (allowlisted fields only).

### Allowed fields (examples)

```json
{
  "schema": "xware_feedback_network_v2",
  "when": "2026-07-19T12:00:00Z",
  "engine": "godot",
  "profile": "space_arcade",
  "project_anon": "a1b2c3d4e5f6",
  "xware_version": "3.5.0",
  "pass": true,
  "registry_count": 12,
  "score_buckets": { "90_100": 10, "70_89": 2 },
  "role_weak_counts": { "prop": 1 },
  "residual_fail_keys": { "surface_read": 2 },
  "residual_key_means": { "surface_read": 0.72 },
  "kernel_weak_class": { "form": 1, "material": 1 },
  "gen_signals": {
    "has_design_intent": true,
    "has_elevate": true,
    "has_playtest": false,
    "has_character_engine": true,
    "elevate_pass": true,
    "registry_count": 12
  },
  "report_flags": { "design_intent": true, "experience_elevate": true },
  "source": "grok_platform_probe",
  "privacy": "anonymized_aggregates_only",
  "local_only": false,
  "engine_improve": true
}
```

### Explicitly forbidden

| Never include |
|---------------|
| Absolute paths, usernames, emails, account IDs |
| Meshes, textures, audio, screenshots, recordings |
| Full prompts that embed private IP or commercial rips |
| Save games, source trees, `.godot` / Assets dumps |
| Free-text fields that can carry PII |

`project_anon` = one-way hash (e.g. salted hash of stable project id), **not** reversible path.

---

## 5. When to fire the probe

Suggested triggers (any 3D game task):

| Trigger | Example user intent |
|---------|---------------------|
| New 3D game bootstrap | “Make a Godot 3D game”, “new Unity 3D project” |
| Experience elevate / raise | “Raise graphics”, “make it photoreal” |
| Asset densify / character pass | “Densify props”, “improve character” |
| Quality gate complete | Pass/fail known |

**Do not fire** on pure 2D pixel work, docs-only, or non-game tasks.

---

## 6. Consent & UX (non-negotiable)

1. **Visible** setting or first-run dialog — not buried.  
2. **Default:** conservative (off, or explicit one-time opt-in).  
3. **Plain language:**  
   > “Share anonymous quality signals (not your game files) to improve 3D tools.”  
4. **Revocable** anytime in settings.  
5. **No marketing of hidden collection** — only transparent improve-the-tools messaging.

---

## 7. What XWare already ships (so integration is small)

| Capability | Location |
|------------|----------|
| Marketplace agent/skills | `tylercollex-gif/xware-grok-plugin` |
| Local hub + harvest | `~/.grok/xware_network/`, `harvest_all_games.py` |
| Session learn probe | `learn_probe.py`, `register_grok_project.py` |
| Opt-in fleet client | `fleet_learn.py` (HTTPS, validate-before-POST) |
| Densify hints merge | `feedback_network_merge.py` → `global_hints.json` |
| Privacy validation | allowlisted pack schema; reject path/username leaks |

Platform work is mainly: **event + consent UI**, not a new ML pipeline.

---

## 8. Benefits to xAI / Grok Build

| Benefit | Detail |
|---------|--------|
| **Better 3D game quality** | Aggregates show which residual classes fail most across real sessions |
| **Marketplace flywheel** | Specialist plugins (XWare and others) get better without users uploading games |
| **Privacy leadership** | Public schema, opt-in, no content exfiltration |
| **Open harness synergy** | Aligns with open Grok Build ecosystem growth |
| **Low implementation cost** | One event type + setting; reuse existing pack shape |

---

## 9. Benefits to users

- Games and assets stay on their machine (or under their control)  
- Clear choice to help improve tools  
- Better elevates over time for everyone who opts in  
- Solo indies especially benefit from shared residual/densify knowledge  

---

## 10. Non-goals (for clarity)

| Not proposed |
|--------------|
| Silent multi-user project access |
| Training on private game content |
| Required telemetry for marketplace install |
| Sharing absolute paths or identities |
| Claiming XWare “sees all Grok projects” without platform + consent |

---

## 11. Suggested pilot

| Phase | Scope |
|-------|--------|
| **Pilot 1** | Local pack write when XWare installed (Option B) — 2–4 weeks |
| **Pilot 2** | First-party opt-in setting + aggregate dashboard for xAI games team (Option A) |
| **Pilot 3** | Optional fleet POST for plugins that declare the schema (Option C) |

Success metrics (aggregates only):

- residual fail rates on key classes trend down over releases  
- densify class-routing hit rate up  
- opt-in rate measurable; zero path/PII incidents  

---

## 12. Contact & links

| | |
|--|--|
| **Maintainer** | tylercollex-gif |
| **Plugin** | https://github.com/tylercollex-gif/xware-grok-plugin |
| **Marketplace PR** | https://github.com/xai-org/plugin-marketplace/pull/110 |
| **Schema / client** | XWare tools: `fleet_learn.py`, feedback pack v2 |

---

## 13. Closing

**Principle:** As Grok gets better at *making* 3D games, specialized agents should get better at *elevating* them — through **consent, aggregates, and open schema**, not silent surveillance.

We’re ready to align on event shape, pilot scope, and ownership (first-party vs plugin-local).  

Thank you for considering a privacy-first learn probe for Grok Build games.
