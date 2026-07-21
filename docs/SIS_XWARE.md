# SIS ↔ XWare (10-step plan bridge)

**Local only.** SIS is the product improvement / epoch dashboard, not marketing.

| Surface | URL |
|---------|-----|
| Public landing | http://127.0.0.1:8765/ |
| Health | http://127.0.0.1:8765/api/health |
| Operator app | http://127.0.0.1:8765/app?token=… |
| Token file | `~/.sis/access_tokens.json` |

## Policy map

| Plan step | SIS allowed |
|-----------|-------------|
| 1–4 product work | `--smoke` only (connectivity) |
| **5 QA (G1)** | Evaluate QA → **`POST /api/epoch` only if pass** |
| 6–8 marketing drafts | No requirement to post epochs; drafts stay offline |
| 9 human review | Optional re-list epochs; no market |
| 10 market push | **Human G3 only** — SIS does not post to X/marketplace |

Product epochs are **token-gated product views** (`public_only: false`), not public marketing.

## CLI

```powershell
# Evaluate Step 5 gate (writes step5_qa_latest.md)
py tools/xware/ai/sis_product_epoch.py --project . --check-only

# Connectivity (always OK with token)
py tools/xware/ai/sis_product_epoch.py --project . --smoke

# After Step 5 QA green — log real product epoch into SIS
py tools/xware/ai/sis_product_epoch.py --project . --post-if-pass

# Operator override (logs forced=true)
py tools/xware/ai/sis_product_epoch.py --project . --post-if-pass --force
```

## QA criteria (default)

- Mean prop avg ≥ 90  
- ≥4 games prop avg ≥ 90  
- Immersion plan majority pass  
- Prop vision ≥ 4 of games with data (Idle wear soft-fail OK unless signoff requires all)  

Optional human signoff file:

`assets/xware_reports/step5_qa_signoff.json`

```json
{
  "step5_approved": true,
  "require_human_signoff": true,
  "require_all_prop_vision": false,
  "note": "I reviewed residual honesty for release candidate"
}
```

## Reports

| File | Meaning |
|------|---------|
| `step5_qa_latest.json` | Gate evaluation |
| `sis_epoch_log.jsonl` | Local audit (no tokens) |
| `step5_sis_product_epoch.json` | Last product epoch id after successful post |

## Secrets

Never commit `SIS_API_TOKEN` or put tokens in marketing copy / hub packs.
