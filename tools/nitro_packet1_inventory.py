#!/usr/bin/env python3
"""MAXESS Naya Nitro Packet 1 — safe architecture inventory.

Read-only against the working HTML. Produces a deterministic inventory before
any consolidation is allowed.
"""
from __future__ import annotations
from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "20260817 912am RESULTS PAGE CODE"
BASELINE = ROOT / "BASELINE-WORKING.html"
REPORT = ROOT / "V21-PACKET1-INVENTORY.md"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    if not SOURCE.exists():
        print(f"ERROR: source not found: {SOURCE}")
        return 2
    if not BASELINE.exists():
        print(f"ERROR: baseline not found: {BASELINE}")
        return 2

    text = SOURCE.read_text(encoding="utf-8")
    baseline_hash = sha256(BASELINE)
    source_hash = sha256(SOURCE)
    scripts = re.findall(r'<script(?:\\s[^>]*)?>(.*?)</script>', text, re.I | re.S)
    script_ids = re.findall(r'<script[^>]*\\bid=["\']([^"\']+)["\']', text, re.I)
    style_ids = re.findall(r'<style[^>]*\\bid=["\']([^"\']+)["\']', text, re.I)
    ids = re.findall(r'\\bid=["\']([^"\']+)["\']', text)
    dup_ids = sorted({x for x in ids if ids.count(x) > 1})

    generation_ids = [
        x for x in script_ids
        if re.search(r'v(?:11|12|13|14|15|16|17|18|19|20|21)|maxess-results', x, re.I)
    ]
    critical_markers = [
        "window.MAXESS_RESULT", "#maxess-results-10", ".v18-flow", ".v20-stage",
        "v13-shell", "v15-results", "naya-playground", "naya-report",
        "v13-dimensions", "v13-strengths", "v13-lever", "v13-next", "v13-masters"
    ]

    lines = text.count("\n") + 1
    report = [
        "# MAXESS V21 — PACKET 1 INVENTORY",
        "",
        "## Integrity",
        f"- Source: `{SOURCE.name}`",
        f"- Source lines: `{lines}`",
        f"- Source bytes: `{len(text.encode('utf-8'))}`",
        f"- Source SHA-256: `{source_hash}`",
        f"- Baseline SHA-256: `{baseline_hash}`",
        f"- Baseline equals source: `{'YES' if source_hash == baseline_hash else 'NO'}`",
        f"- Inline script blocks: `{len(scripts)}`",
        f"- Script IDs: `{len(script_ids)}`",
        f"- Style IDs: `{len(style_ids)}`",
        f"- Duplicate HTML IDs: `{len(dup_ids)}`",
        "",
        "## Generation/controller markers",
    ]
    report.extend(f"- `{x}`" for x in generation_ids)
    report += ["", "## Critical architecture markers"]
    report.extend(f"- `{m}`: {'PRESENT' if m in text else 'ABSENT'}" for m in critical_markers)
    duplicate_lines = [f"- `{x}`" for x in dup_ids] if dup_ids else ["- NONE"]
    report += [
        "",
        "## Duplicate IDs",
        *duplicate_lines,
        "",
        "## Next gate",
        "Packet 1 may proceed to transformation only if the baseline is intact and this inventory is reviewed by the execution controller.",
        "No production/Groove publication is authorized from this packet.",
    ]
    REPORT.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(REPORT.name)
    print(f"Source: {lines} lines / {len(text.encode('utf-8'))} bytes")
    print(f"Inline scripts: {len(scripts)}")
    print(f"Duplicate IDs: {len(dup_ids)}")
    print(f"Baseline SHA-256: {baseline_hash}")
    print(f"Source SHA-256:   {source_hash}")
    print("READ-ONLY INVENTORY COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
