# XWare Xhance (full xAI power)

## Install / rehydrate

```powershell
powershell -ExecutionPolicy Bypass -File Documents\HelixProtocol\tools\xware\install_xhance.ps1
# or from Helix:
powershell -File tools\xware\install_xhance.ps1
```

## Surfaces

| Surface | Use |
|---------|-----|
| Agent | `subagent_type="xware"` · `/config-agents` |
| Skills | `/xware` `/xware-xhance` `/xware-elevate` |
| Plugin path | `Documents/Xware/grok-plugin` in config `[plugins].paths` |
| Hub | `~/.grok/xware_network` |
| Unattended textures | set `XAI_API_KEY` + `xai_api_enabled=true` in game config |
| Privacy (user-facing) | [PRIVACY.md](PRIVACY.md) — local learning; marketing stays look/gameplay only |
| AI policy | [AI_USE_POLICY.md](AI_USE_POLICY.md) — Grok Build must not regenerate XWare |

## After Grok CLI update

Re-run `install_xhance.ps1` (bundled agents get wiped on CLI update).
