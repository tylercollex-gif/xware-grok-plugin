# XWare learns as Grok creates games

**Goal:** As Grok 4.5 / Grok Build generates more 3D games, XWare gets smarter at elevating them.

## What runs on your machine (now)

After every multi-step game create/elevate:

```powershell
py tools/xware/ai/learn_probe.py --project <GamePath> --engine auto --full-harvest
```

Or:

```powershell
py tools/xware/ai/register_grok_project.py --project <GamePath>
py tools/xware/ai/continuous_learn.py --project <GamePath> --all-projects --skip-elevate
```

- **Watchlist** â€” remembers Grok-created paths (local only)  
- **Presence packs** â€” projects without XWare still count engine volume (aggregates only)  
- **Hub** â€” `~/.grok/xware_network/` shared across Godot / Unity / Unreal  
- **Global hints** â€” densify priorities rebuilt from all packs  

## Opt-in multi-user fleet (optional)

```powershell
py tools/xware/ai/fleet_learn.py --status
# enable: set XWARE_LEARN_URL=https://your.server/v1/packs
py tools/xware/ai/fleet_learn.py --push
```

Default **off**. HTTPS + validated aggregates only.

## Privacy

Never shared: paths, saves, meshes, textures, usernames.  
See [PRIVACY.md](PRIVACY.md).

## True â€œevery Grok project worldwideâ€

Requires an xAI/Grok Build platform learn probe (partnership). Local + fleet cover everything XWare can reach without platform access.

## Platform partnership (public)

See [docs/XAI_GROK_LEARN_PROBE.md](docs/XAI_GROK_LEARN_PROBE.md) and [docs/XAI_OUTREACH_SHORT.md](docs/XAI_OUTREACH_SHORT.md).
