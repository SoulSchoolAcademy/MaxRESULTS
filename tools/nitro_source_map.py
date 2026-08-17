#!/usr/bin/env python3
"""Deterministic local source mapper for the MAXESS working HTML."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "20260817 912am RESULTS PAGE CODE"
OUT = ROOT / "V21-SOURCE-MAP.md"

MARKERS = [
    "MAXESS_RESULT", "maxess-results-10", "v13-shell", "v13-naya-introduction",
    "v13-report", "v13-dimensions", "v13-pattern", "v13-strengths", "v13-lever",
    "v13-next", "v13-masters", "naya-playground", "v18-flow", "v20-stage",
    "v15-results", "naya-report", "print", "PDF", "Listen", "audio"
]

def line_no(text, pos):
    return text.count("\n", 0, pos) + 1

def main():
    if not SOURCE.exists():
        print(f"ERROR: source not found: {SOURCE}")
        return 2
    text = SOURCE.read_text(encoding="utf-8")
    lines = text.splitlines()
    scripts = list(re.finditer(r"<script(?:\\s[^>]*)?>(.*?)</script>", text, re.I | re.S))
    styles = list(re.finditer(r"<style(?:\\s[^>]*)?>(.*?)</style>", text, re.I | re.S))
    out = ["# MAXESS V21 — DETERMINISTIC SOURCE MAP", "", f"Source: `{SOURCE.name}`", f"Lines: `{len(lines)}`", f"Bytes: `{len(text.encode('utf-8'))}`", "", "## Inline scripts"]
    for i, m in enumerate(scripts, 1):
        body = m.group(1)
        first = next((ln.strip() for ln in body.splitlines() if ln.strip()), "")[:140]
        out.append(f"- Script {i}: source line {line_no(text, m.start())}; chars {len(body)}; first code: `{first}`")
    out += ["", "## Inline styles"]
    for i, m in enumerate(styles, 1):
        body = m.group(1)
        first = next((ln.strip() for ln in body.splitlines() if ln.strip()), "")[:140]
        out.append(f"- Style {i}: source line {line_no(text, m.start())}; chars {len(body)}; first rule: `{first}`")
    out += ["", "## Marker locations"]
    for marker in MARKERS:
        hits = []
        for m in re.finditer(re.escape(marker), text, re.I):
            hits.append(str(line_no(text, m.start())))
            if len(hits) >= 12:
                break
        out.append(f"- `{marker}`: " + (", ".join(hits) if hits else "ABSENT"))
    out += ["", "## Root mutations", f"- `innerHTML` assignments: `{len(re.findall(r'\\.innerHTML\\s*=', text))}`", f"- `insertAdjacent` calls: `{len(re.findall(r'insertAdjacent', text))}`", f"- `appendChild` calls: `{len(re.findall(r'appendChild', text))}`", f"- `querySelector` calls: `{len(re.findall(r'querySelector', text))}`", "", "## Gate", "This map is descriptive only. No production source is modified by this tool."]
    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(OUT.name)
    print(f"Scripts: {len(scripts)}")
    print(f"Styles: {len(styles)}")
    print(f"Lines: {len(lines)}")
    print("SOURCE MAP COMPLETE")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
