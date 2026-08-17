#!/usr/bin/env python3
"""Safely prepare the V21 transformer, then execute it once."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
tool = ROOT / "tools" / "apply_v21.py"
if not tool.exists():
    raise SystemExit("Missing tools/apply_v21.py")

s = tool.read_text(encoding="utf-8")

# Rescue the legacy V20/V18 sections before the transformer removes their shells.
s = s.replace(
    "removeNode('.v20-stage,.v18-flow,.v13-shell');",
    "legacyStage=root.querySelector('.v20-stage,.v18-flow');\n  /* Keep legacy containers alive until their real sections are moved into V21. */"
)

# Search both the root and legacy generated stage while harvesting preserved sections.
s = s.replace(
    "function first(selList){for(var i=0;i<selList.length;i++){var e=root.querySelector(selList[i]);if(e)return e}return null}",
    "function first(selList){for(var i=0;i<selList.length;i++){var e=root.querySelector(selList[i]);if(e)return e;if(legacyStage){e=legacyStage.querySelector(selList[i]);if(e)return e}}return null}"
)

# Also correct the tiny mobile CSS typo in the generated V21 layer.
s = s.replace(
    ".#maxess-results-10 .v21-letter",
    "#maxess-results-10 .v21-letter"
)

tool.write_text(s, encoding="utf-8")

print("V21 transformer safety correction applied.")
print("Executing full V21 transformation now...\n")
proc = subprocess.run([sys.executable, str(tool)], cwd=str(ROOT))
raise SystemExit(proc.returncode)
