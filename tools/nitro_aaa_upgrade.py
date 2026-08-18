#!/usr/bin/env python3
"""MAXESS Nitro ownership guard.

Nitro is an enhancement lane, not an authoritative product reset lane.
A verified product mutation must survive subsequent Nitro executions.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "20260817 912am RESULTS PAGE CODE"
BASELINE = ROOT / "BASELINE-NITRO-20260817.html"
START = "<!-- MAXESS-NITRO-AAA-UPGRADE v3 -->"
END = "<!-- /MAXESS-NITRO-AAA-UPGRADE -->"


def main() -> int:
    if not SOURCE.exists():
        raise SystemExit("NITRO: authoritative product source missing")

    source = SOURCE.read_text(encoding="utf-8")

    required = ("<html", "window.MAXESS_RESULT", "#maxess-results-10")
    missing = [token for token in required if token not in source]
    if missing:
        raise SystemExit("NITRO: source integrity failed: " + ", ".join(missing))

    if re.search(r"(^|\n)(<<<<<<<|=======|>>>>>>>)( |\n|$)", source):
        raise SystemExit("NITRO: unresolved merge-conflict marker in authoritative source")

    # Critical ownership rule:
    # NEVER reset the authoritative product source from BASELINE-NITRO.
    # Doing so destroys verified product work created by other governed lanes.
    if START in source and END in source:
        print("NITRO OWNERSHIP GUARD: PASS")
        print("Existing Nitro layer preserved in place.")
        print("No baseline reset performed.")
        print("Verified product mutations outside the Nitro layer remain authoritative.")
        print("Source bytes:", len(source.encode("utf-8")))
        print("Source lines:", len(source.splitlines()))
        return 0

    # A clean current source is allowed to lack the Nitro layer, but Nitro must
    # not invent or regenerate product content from an obsolete baseline.
    if BASELINE.exists():
        print("NITRO OWNERSHIP GUARD: SAFE STOP")
        print("Nitro layer is absent; refusing destructive baseline reconstruction.")
        print("A governed product/build lane must create the next authoritative layer.")
        return 0

    raise SystemExit("NITRO: safe source state but no governed Nitro layer or baseline")


if __name__ == "__main__":
    raise SystemExit(main())
