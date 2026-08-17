#!/usr/bin/env python3
"""Granular, read-only V21 preflight for the complete MAXESS Groove source."""
from __future__ import annotations
from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "20260817 912am RESULTS PAGE CODE"
REPORT = ROOT / "V21-PACKET2-PREFLIGHT.md"

MARKERS = [
    "v13", "v15", "v18", "v20", "v21", "maxess-results-10",
    "MAXESS_RESULT", "DOMContentLoaded", "maxess:result-ready",
    "Listen", "PDF", "audio", "print", "innerHTML", "outerHTML",
    "insertAdjacent", "appendChild", "addEventListener"
]


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def line_no(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def extract_blocks(text: str, tag: str):
    pat = re.compile(rf"<{tag}\\b[^>]*>(.*?)</{tag}>", re.I | re.S)
    return list(pat.finditer(text))


def id_value(opening: str) -> str:
    m = re.search(r'\\bid=["\']([^"\']+)["\']', opening, re.I)
    return m.group(1) if m else "(none)"


def summarize_block(kind: str, idx: int, m: re.Match, text: str):
    start = line_no(text, m.start())
    end = line_no(text, m.end())
    raw = m.group(0)
    body = m.group(1)
    first_lines = [ln.strip() for ln in body.splitlines() if ln.strip()][:5]
    marker_hits = [x for x in MARKERS if re.search(re.escape(x), body, re.I)]
    funcs = sorted(set(re.findall(r'\\bfunction\\s+([A-Za-z_$][\\w$]*)\\s*\\(', body)))[:40]
    listeners = len(re.findall(r'addEventListener\\s*\\(', body))
    mutations = {name: len(re.findall(re.escape(name), body)) for name in ["innerHTML", "outerHTML", "insertAdjacent", "appendChild", "querySelector", "createElement"]}
    return {
        "kind": kind,
        "index": idx,
        "id": id_value(raw.split(">", 1)[0] + ">") if kind in {"script", "style"} else "(none)",
        "start": start,
        "end": end,
        "lines": end - start + 1,
        "markers": marker_hits,
        "functions": funcs,
        "listeners": listeners,
        "mutations": mutations,
        "first_lines": first_lines,
        "sha256": sha256(body),
    }


def main() -> int:
    if not SOURCE.exists():
        print(f"ERROR: source not found: {SOURCE}")
        return 2
    text = SOURCE.read_text(encoding="utf-8")
    scripts = extract_blocks(text, "script")
    styles = extract_blocks(text, "style")
    if len(scripts) != 5 or len(styles) != 5:
        print(f"ERROR: expected 5 scripts and 5 styles; found {len(scripts)} scripts / {len(styles)} styles")
        return 3

    sb = [summarize_block("script", i + 1, m, text) for i, m in enumerate(scripts)]
    st = [summarize_block("style", i + 1, m, text) for i, m in enumerate(styles)]

    out = [
        "# MAXESS V21 — PACKET 2 GRANULAR PREFLIGHT",
        "",
        f"- Source lines: `{text.count(chr(10)) + 1}`",
        f"- Source bytes: `{len(text.encode('utf-8'))}`",
        f"- Source SHA-256: `{sha256(text)}`",
        "- Mode: READ-ONLY",
        "",
        "## Script blocks",
    ]
    for b in sb:
        out += [
            f"### Script {b['index']} — `{b['id']}` — lines {b['start']}-{b['end']} ({b['lines']} lines)",
            f"SHA-256: `{b['sha256']}`",
            f"Markers: {', '.join(b['markers']) or 'NONE'}",
            f"Functions: {', '.join(b['functions']) or 'NONE'}",
            f"Event listeners: `{b['listeners']}`",
            "Mutations: " + ", ".join(f"{k}={v}" for k,v in b['mutations'].items()),
            "Opening lines:",
            *[f"- `{x}`" for x in b['first_lines']],
            "",
        ]
    out.append("## Style blocks")
    for b in st:
        out += [
            f"### Style {b['index']} — `{b['id']}` — lines {b['start']}-{b['end']} ({b['lines']} lines)",
            f"SHA-256: `{b['sha256']}`",
            f"Markers: {', '.join(b['markers']) or 'NONE'}",
            "",
        ]
    out += [
        "## Execution interpretation",
        "",
        "Packet 2 must establish one authoritative active controller before product-facing redesign.",
        "No production/Groove publication is authorized from this report alone.",
    ]
    REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(REPORT.name)
    for b in sb:
        print(f"SCRIPT {b['index']}: {b['id']} lines={b['start']}-{b['end']} listeners={b['listeners']} markers={len(b['markers'])}")
    for b in st:
        print(f"STYLE {b['index']}: {b['id']} lines={b['start']}-{b['end']} markers={len(b['markers'])}")
    print("PACKET 2 PREFLIGHT COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
