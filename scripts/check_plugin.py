#!/usr/bin/env python3
"""XWare Grok Build plugin check (read-only, stdlib only, about a second).

  py scripts/check_plugin.py            # human lines + verdict
  py scripts/check_plugin.py --json     # same, plus one JSON line at the end

Checks the plugin package itself (not a game): manifest where the xAI marketplace
tooling looks for it (.grok-plugin/plugin.json), root plugin.json mirror, no control
characters, declared components exist and are complete, SKILL/agent frontmatter,
one version everywhere, spawn contract (studio_raise default, no capability_mode,
no ASK in child prompts), no machine-local paths or secrets, relative links resolve.
Prints XWARE_PLUGIN_CHECK <id> PASS|FAIL <detail> and one XWARE_PLUGIN_VERDICT line.
Exit 0 only on PASS. Writes nothing.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".grok-plugin" / "plugin.json"
MIRROR = ROOT / "plugin.json"
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
CONTROL = re.compile(r"[\x00-\x1f\x7f]")
# (file, regex with one group = version). Every anchor must exist and equal the manifest version.
VERSION_ANCHORS = [
    ("plugin.json", r'"description":\s*"XWare Xhance (\d+\.\d+\.\d+)'),
    ("agents/xware.md", r"\| Version \| \*\*(\d+\.\d+\.\d+)"),
    ("agents/xware.md", r"- \*\*Version:\*\* (\d+\.\d+\.\d+)"),
    ("skills/xware/SKILL.md", r"\*\*Version (\d+\.\d+\.\d+)"),
    ("README.md", r"\[`plugin\.json`\]\(plugin\.json\) \*\*(\d+\.\d+\.\d+)\*\*"),
]
LOCAL_PATH = re.compile(r"[A-Za-z]:[\\/]{1,2}Users[\\/]{1,2}[A-Za-z]|/home/[a-z][a-z0-9_-]+/|/Users/[A-Za-z][^/\s]*/")
SECRET = re.compile(
    r"xai-[A-Za-z0-9]{20,}|gh[pousr]_[A-Za-z0-9]{30,}|sk-[A-Za-z0-9]{32,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----"
)
SKIP_TEXT = re.compile(r"^docs/GROK-BUILD-.*\.md$")  # local paste files (never committed)
TEXT_EXT = {".md", ".json", ".toml", ".py", ".gd", ".txt", ".yml", ".yaml", ".cfg", ".ps1", ""}

checks = 0
fails = 0
results: list[dict] = []


def ok(cid: str, cond: bool, detail: str = "") -> None:
    global checks, fails
    checks += 1
    if not cond:
        fails += 1
    results.append({"id": cid, "pass": bool(cond), "detail": detail})
    print(f"XWARE_PLUGIN_CHECK {cid} {'PASS' if cond else 'FAIL'} {detail}".rstrip())


def tracked_files() -> list[str]:
    try:
        out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
        files = [f for f in out.splitlines() if f]
    except (OSError, subprocess.CalledProcessError):
        files = [p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]
    # Include new, not-yet-staged files too (so the check works mid-section), minus ignored ones.
    try:
        extra = subprocess.run(["git", "ls-files", "--others", "--exclude-standard"], cwd=ROOT,
                               capture_output=True, text=True, check=True).stdout.splitlines()
        files += [f for f in extra if f]
    except (OSError, subprocess.CalledProcessError):
        pass
    return sorted({f for f in files if (ROOT / f).is_file()})


def frontmatter(path: Path) -> dict[str, str]:
    """Same subset the marketplace index generator reads (key: value and folded > / | blocks)."""
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    out: dict[str, str] = {}
    i = 1
    while i < len(lines):
        line = lines[i]
        if line.strip() in ("---", "..."):
            break
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not m:
            i += 1
            continue
        key, val = m.group(1), m.group(2).strip()
        if re.match(r"^[|>][+-]?$", val):
            block = []
            j = i + 1
            while j < len(lines) and (lines[j].startswith((" ", "\t")) or not lines[j].strip()):
                if lines[j].strip():
                    block.append(lines[j].strip())
                j += 1
            val, i = " ".join(block), j
        else:
            if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
                val = val[1:-1]
            i += 1
        out[key] = val
    return out


def strings_in(obj, path="$"):
    if isinstance(obj, str):
        yield path, obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from strings_in(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from strings_in(v, f"{path}[{i}]")


def strip_fences(text: str) -> str:
    return re.sub(r"^(```|~~~).*?^\1[^\n]*$", "", text, flags=re.S | re.M)


def main() -> int:
    as_json = "--json" in sys.argv[1:]
    files = tracked_files()

    # 1. Manifest where marketplace tooling reads it.
    man: dict = {}
    try:
        man = json.loads(MANIFEST.read_text(encoding="utf-8"))
        ok("manifest_present", isinstance(man, dict), ".grok-plugin/plugin.json")
    except (OSError, json.JSONDecodeError) as e:
        ok("manifest_present", False, f".grok-plugin/plugin.json: {type(e).__name__}")
    if MIRROR.is_file():
        ok("manifest_mirror", MANIFEST.is_file() and MIRROR.read_bytes() == MANIFEST.read_bytes(),
           "root plugin.json must be byte-identical to .grok-plugin/plugin.json")
    ver = str(man.get("version", ""))
    ok("manifest_fields", man.get("name") == "xware" and bool(SEMVER.match(ver)) and bool(man.get("license"))
       and bool(man.get("homepage")) and bool(man.get("description")), f"name={man.get('name')} version={ver}")
    bad = [p for p, s in strings_in(man) if CONTROL.search(s)]
    if not man and MIRROR.is_file():
        try:
            bad = [p for p, s in strings_in(json.loads(MIRROR.read_text(encoding="utf-8"))) if CONTROL.search(s)]
        except json.JSONDecodeError:
            bad = ["$ (invalid JSON)"]
    ok("no_control_chars", not bad, ",".join(bad)[:120])

    # 2. Components.
    src = man or (json.loads(MIRROR.read_text(encoding="utf-8")) if MIRROR.is_file() else {})
    missing = []
    for a in src.get("agents", []):
        if not (ROOT / a).is_file():
            missing.append(a)
    for s in src.get("skills", []):
        if not (ROOT / s / "SKILL.md").is_file():
            missing.append(s)
    for r in src.get("roles", []):
        if not (ROOT / r).is_file():
            missing.append(r)
    for c in src.get("commands", []) if isinstance(src.get("commands"), list) else []:
        if not (ROOT / c).is_file():
            missing.append(c)
    ok("components_exist", not missing, ",".join(missing))
    on_disk = sorted(p.parent.relative_to(ROOT).as_posix() for p in (ROOT / "skills").glob("*/SKILL.md"))
    unlisted = [d for d in on_disk if d not in src.get("skills", [])]
    ok("skills_listed", not unlisted, ",".join(unlisted))

    # 3. Frontmatter (marketplace index reads name + description).
    fm_bad = []
    for d in on_disk:
        fm = frontmatter(ROOT / d / "SKILL.md")
        if fm.get("name") != Path(d).name or not (1 <= len(fm.get("description", "")) <= 1024):
            fm_bad.append(d)
    for a in sorted((ROOT / "agents").glob("*.md")):
        fm = frontmatter(a)
        if fm.get("name") != a.stem or not fm.get("description"):
            fm_bad.append(a.relative_to(ROOT).as_posix())
    for c in sorted((ROOT / "commands").glob("*.md")) if (ROOT / "commands").is_dir() else []:
        if not frontmatter(c).get("description"):
            fm_bad.append(c.relative_to(ROOT).as_posix())
    ok("frontmatter", not fm_bad, ",".join(fm_bad))

    # 4. One version everywhere.
    drift = []
    for rel, rx in VERSION_ANCHORS:
        p = ROOT / rel
        text = p.read_text(encoding="utf-8", errors="replace") if p.is_file() else ""
        found = re.findall(rx, text)
        if not found:
            drift.append(f"{rel}:missing")
        drift += [f"{rel}:{v}" for v in found if v != ver]
    ok("version_sync", not drift, f"manifest={ver} " + ",".join(drift))

    # 5. Spawn contract (child prompts; studio_raise default; experience_elevate only as legacy).
    contract = []
    for rel in files:
        if not rel.endswith(".md") or rel.startswith("marketing/") or SKIP_TEXT.match(rel):
            continue
        for n, line in enumerate((ROOT / rel).read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            code = line.split("#", 1)[0] if line.lstrip().startswith(("Engine:", "Task:")) else line
            if re.search(r"(?<!default_)capability_mode\s*=", code):
                contract.append(f"{rel}:{n}:capability_mode")
            if re.match(r"\s*Engine:.*\bASK(_IF_UNKNOWN)?\b", code):
                contract.append(f"{rel}:{n}:Engine ASK")
            if line.lstrip().startswith("#"):
                continue
            if (re.search(r"experience_elevate(\.py)?\s+--", line) or re.match(r"\s*Task:.*experience_elevate", line)) \
                    and "legacy" not in line.lower():
                contract.append(f"{rel}:{n}:experience_elevate not legacy")
    ok("spawn_contract", not contract, ",".join(contract)[:300])

    # 6. Hygiene: no machine-local paths or secrets in anything tracked.
    hits, secrets = [], []
    for rel in files:
        if SKIP_TEXT.match(rel) or Path(rel).suffix.lower() not in TEXT_EXT:
            continue
        text = (ROOT / rel).read_text(encoding="utf-8", errors="replace")
        if LOCAL_PATH.search(text):
            hits.append(rel)
        if SECRET.search(text):
            secrets.append(rel)
    ok("no_local_paths", not hits, ",".join(hits))
    ok("no_secrets", not secrets, ",".join(secrets))

    # 7. Relative markdown links resolve (fenced code ignored).
    broken = []
    for rel in files:
        if not rel.endswith(".md") or SKIP_TEXT.match(rel):
            continue
        text = strip_fences((ROOT / rel).read_text(encoding="utf-8", errors="replace"))
        for m in re.finditer(r"\]\(([^)#\s]+)(#[^)]*)?\)", text):
            link = m.group(1)
            if re.match(r"^[a-z][a-z0-9+.-]*:", link):
                continue
            if not ((ROOT / rel).parent / link).exists():
                broken.append(f"{rel}->{link}")
    ok("links_resolve", not broken, ",".join(broken)[:300])

    verdict = "PASS" if fails == 0 else "FAIL"
    print(f"XWARE_PLUGIN_VERDICT {verdict} version={ver or 'none'} checks={checks} fails={fails}")
    if as_json:
        print(json.dumps({"verdict": verdict, "version": ver, "checks": checks, "fails": fails, "results": results}))
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
