#!/usr/bin/env python3
"""Diagnose JavaScript syntax failures in the V21 candidate without modifying the source."""
from pathlib import Path
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "20260817 912am RESULTS PAGE CODE"


def main():
    if not SOURCE.exists():
        print("ERROR: working source file not found:", SOURCE)
        return 2
    node = shutil.which("node")
    if not node:
        print("ERROR: Node.js is not available in this Codespace.")
        return 3
    text = SOURCE.read_text(encoding="utf-8")
    blocks = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", text, re.I | re.S)
    print(f"Found {len(blocks)} inline script blocks.")
    for idx, block in enumerate(blocks, 1):
        if not block.strip():
            continue
        tmp = ROOT / f".v21_diag_{idx}.js"
        tmp.write_text(block, encoding="utf-8")
        p = subprocess.run([node, "--check", str(tmp)], capture_output=True, text=True)
        tmp.unlink(missing_ok=True)
        if p.returncode:
            print(f"\nSYNTAX FAILURE: script block {idx}\n")
            print(p.stderr.strip())
            m = re.search(r":(\d+)(?::(\d+))?", p.stderr)
            if m:
                line = int(m.group(1))
                lines = block.splitlines()
                lo = max(1, line - 5)
                hi = min(len(lines), line + 5)
                print("\nCONTEXT:")
                for n in range(lo, hi + 1):
                    marker = " >>>" if n == line else "    "
                    print(f"{marker} {n}: {lines[n-1]}")
            return 1
    print("ALL INLINE JAVASCRIPT BLOCKS PASS NODE SYNTAX.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
