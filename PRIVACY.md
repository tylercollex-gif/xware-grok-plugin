# Privacy (user-facing)

XWare continuous improvement works **across Godot, Unity, and Unreal** on your machine while keeping your game data private.

## What we aim for

- Learning stays **on your machine** by default (`~/.grok/xware_network/`)
- Signals are **anonymized quality aggregates only** (residual rates, weak classes, profile, engine tag)
- **Never** shared by default: save games, meshes, textures, absolute paths, usernames
- Cloud sharing is **off** unless you deliberately turn it on
- Elevates/installs prefer **backups** so player work is not destroyed

## Multi-engine hub + “learn what Grok created”

Packs from Godot, Unity, and Unreal projects are validated before hub admission, then merged so the **next** elevate densifies smarter — regardless of which engine the pack came from.

`learn_probe` / `harvest_all_games` / `continuous_learn --all-projects` re-export aggregates from local Grok-created 3D projects (with or without full XWare install via presence packs). Report flags + residual rates only — never art or saves.

Optional multi-user fleet is **opt-in** (`fleet_learn.py`).

## What marketing will not do

Public posts talk about **game results and graphics**, not internal safety mechanics.

## Operators

Rehydrate after Grok CLI updates with `install_xhance.ps1` from your tools checkout.
