#!/usr/bin/env python3
"""XWare doctor: read-only shipping-bar + tools-locator check for a Godot 4 game (stdlib only, seconds).

  py xware_doctor.py --project <game root> [--tools <XWare tools/xware>] [--reports] [--godot <exe>] [--json-out <file>]

Finds the official XWare tools (never writes or generates them), then checks the game against the
Godot 4 Forward+ -> Steam bar: renderer, addons allowlist (xware + godotsteam only), third-party
asset markers, XWare config that runs Python on editor open, machine-local paths, version drift,
export presets (tools / AI inbox / feedback excluded, no steam_appid.txt in the depot).
--reports re-reads assets/xware_reports so a studio_raise "pass" can't hide a FAIL, SOFT QA or
missing video evidence. --godot runs ship_probe.gd headless (-s, no editor, no import) to read the
engine's effective settings.

Prints XWARE_DOCTOR <id> PASS|INFO|WARN|FAIL <detail>, then TOOLS_OK <path> or TOOLS_MISSING, then
one XWARE_DOCTOR_VERDICT line. Exit 0 = PASS/WARN, 1 = FAIL, 2 = not a Godot project.
Writes nothing unless --json-out is given (put that file outside the game).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ALLOWED_ADDONS = {"xware", "godotsteam"}
REQUIRED_TOOLS = [
    "ai/xware_raise.py",
    "ai/studio_raise.py",
    "ai/material_pack.py",
    "ai/quality_gate.py",
    "ai/continuous_learn.py",
    "install_to_project.ps1",
]
EXPORT_EXCLUDES = ["tools/*", "addons/xware/ai/*", "addons/xware/feedback/*"]
PACK_MARKERS = re.compile(
    r"kenney|quaternius|synty|polypizza|poly_pizza|sketchfab|turbosquid|cgtrader|mixamo|unity_?asset|fab_com|megascans|kitbash3d",
    re.I,
)
LOCAL_PATH = re.compile(r"[A-Za-z]:[\\/]{1,2}Users[\\/]{1,2}[A-Za-z]|/home/[a-z][a-z0-9_-]+/|/Users/[A-Za-z][^/\s\"']*/")
TEXT_EXT = {".gd", ".py", ".cfg", ".json", ".tscn", ".tres", ".md", ".ps1", ".gdshader", ".txt", ".godot"}
SKIP_DIRS = {".godot", ".git", ".import", "__pycache__", "node_modules", "build", "export"}

lines: list[dict] = []


def emit(cid: str, level: str, detail: str = "") -> None:
    lines.append({"id": cid, "level": level, "detail": detail})
    print(f"XWARE_DOCTOR {cid} {level} {detail}".rstrip())


def parse_cfg(text: str) -> dict[str, dict[str, str]]:
    """Godot project.godot / ConfigFile subset: [section], key=value, values may span lines."""
    out: dict[str, dict[str, str]] = {"": {}}
    sec, key, buf, depth = "", None, "", 0
    for raw in text.splitlines():
        line = raw.strip()
        if key is not None:
            buf += "\n" + raw
            depth += _depth(raw)
            if depth <= 0:
                out[sec][key] = buf.strip()
                key = None
            continue
        if not line or line.startswith((";", "#")):
            continue
        m = re.match(r"^\[([^\]]+)\]$", line)
        if m:
            sec = m.group(1).strip()
            out.setdefault(sec, {})
            continue
        if "=" in line:
            k, v = line.split("=", 1)
            d = _depth(v)
            if d > 0:
                key, buf, depth = k.strip(), v, d
            else:
                out[sec][k.strip()] = v.strip()
    return out


def _depth(s: str) -> int:
    s = re.sub(r'"(\\.|[^"\\])*"', "", s)
    return s.count("(") + s.count("[") + s.count("{") - s.count(")") - s.count("]") - s.count("}")


def unq(v: str | None) -> str:
    v = (v or "").strip()
    return v[1:-1] if len(v) >= 2 and v[0] == v[-1] == '"' else v


def truthy(v: str | None) -> bool:
    return unq(v).lower() in ("true", "1", "yes", "on")


def read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return ""


def walk(root: Path, max_files: int = 20000):
    n = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for f in filenames:
            n += 1
            if n > max_files:
                return
            yield Path(dirpath) / f


def locate_tools(project: Path, cli: str | None) -> tuple[Path | None, list[str]]:
    tried = []
    cands = []
    if cli:
        cands.append(Path(cli))
    if os.environ.get("XWARE_TOOLS"):
        cands.append(Path(os.environ["XWARE_TOOLS"]))
    cands.append(project / "tools" / "xware")
    for c in cands:
        c = c.expanduser()
        if (c / "tools" / "xware").is_dir() and not (c / "ai").is_dir():
            c = c / "tools" / "xware"
        missing = [r for r in REQUIRED_TOOLS if not (c / r).is_file()]
        tried.append(f"{c} (missing {len(missing)})" if missing else str(c))
        if not missing:
            return c.resolve(), tried
    return None, tried


def check_project(project: Path, args) -> str:
    pg = project / "project.godot"
    cfg = parse_cfg(read(pg))
    app = cfg.get("application", {})
    feats = re.findall(r'"([^"]+)"', app.get("config/features", ""))
    ver = next((f for f in feats if re.match(r"^\d+\.\d+$", f)), "")
    cv = unq(cfg.get("", {}).get("config_version"))
    if ver.startswith("4.") or (not ver and cv == "5"):
        emit("godot_version", "PASS", f"features={','.join(feats) or '-'} config_version={cv}")
    else:
        emit("godot_version", "FAIL", f"not Godot 4 (features={feats} config_version={cv})")
    rend = cfg.get("rendering", {})
    method = unq(rend.get("renderer/rendering_method")) or "forward_plus"
    emit("renderer", "PASS" if method == "forward_plus" else "FAIL",
         f"rendering_method={method}" + ("" if method == "forward_plus" else " (bar is Forward+)"))
    extra = {k: unq(v) for k, v in rend.items() if k.startswith("renderer/rendering_method.")}
    if extra:
        emit("renderer_overrides", "INFO", ",".join(f"{k.split('.', 1)[1]}={v}" for k, v in extra.items()))
    phys = unq(cfg.get("physics", {}).get("3d/physics_engine")) or "default"
    emit("physics", "INFO", f"3d/physics_engine={phys} (leave as the game ships it)")

    # Addons allowlist.
    addons = sorted(p.name for p in (project / "addons").iterdir() if p.is_dir()) if (project / "addons").is_dir() else []
    other = [a for a in addons if a.lower() not in ALLOWED_ADDONS]
    emit("addons", "WARN" if other else "PASS",
         f"addons={','.join(addons) or '-'}" + (f" third-party needs owner OK: {','.join(other)}" if other else ""))
    enabled = re.findall(r'"([^"]+)"', cfg.get("editor_plugins", {}).get("enabled", ""))
    emit("editor_plugins", "INFO", ",".join(enabled) or "-")

    # Third-party asset markers (outside XWare's own catalog and GodotSteam).
    marks = []
    for p in walk(project):
        rel = p.relative_to(project).as_posix()
        if rel.startswith(("addons/xware/", "addons/godotsteam/", "tools/")):
            continue
        low = p.name.lower()
        if PACK_MARKERS.search(rel) or (low.startswith(("license", "credits", "attribution")) and "/" in rel):
            marks.append(rel)
    emit("third_party_assets", "WARN" if marks else "PASS",
         (f"review {len(marks)}: " + ",".join(marks[:8])) if marks else "no pack names or stray license files")

    # XWare config (section-aware).
    xc = project / "addons" / "xware" / "xware_config.cfg"
    if xc.is_file():
        x = parse_cfg(read(xc))
        auto = x.get("auto", {})
        risky = [k for k in ("auto_raise_on_open", "on_low_score") if truthy(auto.get(k))]
        emit("xware_editor_python", "WARN" if risky else "PASS",
             ("[auto] " + ",".join(f"{k}=true" for k in risky) + " -> XWare runs blocking Python raises when the editor opens; set false, raise manually")
             if risky else "[auto] no raise on editor open")
        cloud = truthy(x.get("network", {}).get("share_feedback_cloud"))
        emit("xware_cloud_share", "WARN" if cloud else "PASS", "share_feedback_cloud=" + str(cloud).lower())
        gen = x.get("generation", {})
        look = [k for k in ("photoreal_all_objects", "no_quality_ceiling") if truthy(gen.get(k))]
        emit("xware_look_flags", "INFO", (",".join(look) + " on: confirm they match the game's art direction") if look else "photoreal/no-ceiling off")
        prof = unq(x.get("profile", {}).get("active"))
        emit("xware_profile", "INFO", f"active={prof or '-'}")
    else:
        emit("xware_config", "INFO", "addons/xware/xware_config.cfg not found (XWare runtime not installed in this game)")

    # Version drift: runtime addon vs project-local agent card.
    pc = parse_cfg(read(project / "addons" / "xware" / "plugin.cfg")).get("plugin", {})
    addon_v = unq(pc.get("version"))
    agent = read(project / ".grok" / "agents" / "xware.md")
    m = re.search(r"\|\s*Version\s*\|\s*\**\s*(\d+\.\d+(?:\.\d+)?)", agent)
    agent_v = m.group(1) if m else ""
    if addon_v and agent_v and addon_v != agent_v:
        emit("version_drift", "WARN", f"addons/xware {addon_v} vs .grok/agents/xware.md {agent_v}: re-run the official rehydrate")
    else:
        emit("version_drift", "PASS", f"addon={addon_v or '-'} agent_card={agent_v or '-'}")

    # Machine-local absolute paths (break on other PCs, leak usernames into builds).
    hits = []
    for sub in ("addons/xware", "tools/xware", "scripts", "scenes", ".grok"):
        base = project / sub
        if not base.is_dir():
            continue
        for p in walk(base):
            if p.suffix.lower() in TEXT_EXT and p.stat().st_size < 2_000_000 and LOCAL_PATH.search(read(p)):
                hits.append(p.relative_to(project).as_posix())
    emit("local_paths", "WARN" if hits else "PASS",
         (f"{len(hits)} files: " + ",".join(sorted(hits)[:6])) if hits else "none")

    # Export presets / Steam depot hygiene.
    ep = project / "export_presets.cfg"
    if not ep.is_file():
        emit("export_presets", "WARN", "export_presets.cfg missing: no reproducible Steam build (add Windows/Linux presets)")
    else:
        e = parse_cfg(read(ep))
        presets = [s for s in e if re.match(r"^preset\.\d+$", s)]
        probs = []
        for s in presets:
            name = unq(e[s].get("name")) or s
            exc = unq(e[s].get("exclude_filter"))
            inc = unq(e[s].get("include_filter"))
            miss = [f for f in EXPORT_EXCLUDES if f not in exc]
            if miss:
                probs.append(f"{name}: exclude_filter lacks {' '.join(miss)}")
            if "steam_appid.txt" in inc:
                probs.append(f"{name}: include_filter ships steam_appid.txt")
        emit("export_presets", "WARN" if probs or not presets else "PASS",
             ("; ".join(probs) if probs else f"{len(presets)} presets") if presets else "no [preset.N] sections")
    if (project / "steam_appid.txt").is_file():
        emit("steam_appid", "INFO", "steam_appid.txt present: fine for local runs, keep it out of the Steam depot")
    gs = project / "addons" / "godotsteam"
    if gs.is_dir():
        gx = next(iter(sorted(gs.glob("*.gdextension"))), None)
        emit("godotsteam", "INFO", f"GodotSteam present ({gx.name if gx else 'module/plugin'}); keep it the only Steam binding")
    else:
        emit("godotsteam", "INFO", "no GodotSteam yet (LAN/offline builds only)")
    return method


def check_reports(project: Path) -> None:
    rep = project / "assets" / "xware_reports"
    sr = rep / "studio_raise_latest.json"
    if not sr.is_file():
        emit("report_studio_raise", "INFO", "no studio_raise_latest.json (no raise yet)")
    else:
        try:
            d = json.loads(read(sr))
        except json.JSONDecodeError:
            d = {}
            emit("report_studio_raise", "WARN", "studio_raise_latest.json unreadable")
        deps = d.get("departments") or []
        fail = [x.get("role") for x in deps if x.get("status") == "FAIL"]
        soft_qa = [x.get("role") for x in deps if x.get("role") == "qa" and x.get("status") == "SOFT"]
        missing = [x.get("role") for x in deps if "missing" in str(x.get("note", "")).lower() or "skipped" in str(x.get("note", "")).lower()]
        hidden = bool(d.get("pass")) and bool(fail or soft_qa or missing)
        emit("report_studio_raise", "WARN" if hidden or not d.get("pass") else "PASS",
             f"pass={d.get('pass')} fail={fail} soft_qa={soft_qa} missing_or_skipped={missing}"
             + (" -> overall pass hides these; report NOT PASS" if hidden else ""))
    vid = rep / "screen_record_analyze_latest.json"
    pt = rep / "playtest_improve_latest.json"
    have = [p.name for p in (vid, pt) if p.is_file()]
    emit("report_video_evidence", "PASS" if vid.is_file() else "WARN",
         ("have " + ",".join(have)) if have else "no screen_record_analyze / playtest report: 3D residual is UNVERIFIED (stills can't PASS)")


def run_probe(project: Path, godot: str, method: str) -> None:
    probe = Path(__file__).resolve().parent / "ship_probe.gd"
    try:
        r = subprocess.run([godot, "--headless", "--path", str(project), "-s", str(probe)],
                           capture_output=True, text=True, timeout=90)
        out = r.stdout + r.stderr
    except (OSError, subprocess.TimeoutExpired) as e:
        emit("godot_probe", "WARN", f"probe did not run: {type(e).__name__}")
        return
    m = re.search(r"^XWARE_PROBE (.*)$", out, re.M)
    if not m:
        emit("godot_probe", "WARN", f"no XWARE_PROBE line (exit {r.returncode})")
        return
    kv = dict(re.findall(r"(\w+)=(\S*)", m.group(1)))
    eff = kv.get("renderer", "")
    lvl = "PASS" if eff == "forward_plus" and eff == method else ("FAIL" if eff != "forward_plus" else "WARN")
    emit("godot_probe", lvl, m.group(1))


def main() -> int:
    ap = argparse.ArgumentParser(description="XWare doctor (read-only)")
    ap.add_argument("--project", required=True)
    ap.add_argument("--tools", default=None, help="XWare tools/xware checkout (else $XWARE_TOOLS, else <project>/tools/xware)")
    ap.add_argument("--reports", action="store_true", help="re-read assets/xware_reports for honest PASS")
    ap.add_argument("--godot", default=None, help="Godot 4 executable for the headless settings probe")
    ap.add_argument("--json-out", default=None)
    a = ap.parse_args()
    project = Path(a.project).expanduser().resolve()
    if not (project / "project.godot").is_file():
        kind = "unity" if (project / "Assets").is_dir() and (project / "ProjectSettings").is_dir() else (
            "unreal" if any(project.glob("*.uproject")) else "unknown")
        emit("engine", "INFO", f"engine={kind}: the doctor covers Godot 4 only (ask the user if unknown)")
        print(f"XWARE_DOCTOR_VERDICT NOT_GODOT engine={kind}")
        return 2
    emit("engine", "PASS", "godot")
    tools, tried = locate_tools(project, a.tools)
    method = check_project(project, a)
    if a.reports:
        check_reports(project)
    if a.godot:
        run_probe(project, a.godot, method)
    if tools:
        emit("tools", "PASS", str(tools))
        print(f"TOOLS_OK {tools}")
    else:
        emit("tools", "WARN", "official XWare tools not found; tried: " + " | ".join(tried))
        print("TOOLS_MISSING install the official runtime from your XWare tools checkout: "
              "powershell -File <checkout>\\tools\\xware\\install_to_project.ps1 -Target <game> -Profile <profile> "
              "(or set XWARE_TOOLS=<checkout>\\tools\\xware). Never write replacement tools.")
    fails = sum(1 for x in lines if x["level"] == "FAIL")
    warns = sum(1 for x in lines if x["level"] == "WARN")
    verdict = "FAIL" if fails else ("WARN" if warns else "PASS")
    print(f"XWARE_DOCTOR_VERDICT {verdict} fails={fails} warns={warns} tools={tools or 'TOOLS_MISSING'}")
    if a.json_out:
        Path(a.json_out).write_text(json.dumps({"verdict": verdict, "tools": str(tools or ""), "checks": lines}, indent=2), encoding="utf-8")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
