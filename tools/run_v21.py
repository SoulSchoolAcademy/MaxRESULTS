#!/usr/bin/env python3
"""Safely prepare the V21 transformer, execute it, validate it, and publish the working branch."""
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
if proc.returncode != 0:
    raise SystemExit(proc.returncode)

# Publish only the files created/changed by this controlled release operation.
paths = [
    "20260817 912am RESULTS PAGE CODE",
    "MAXESS-RESULTS-GROOVE.html",
    "BASELINE-V20-WORKING.html",
    "V21-QA-REPORT.md",
    "tools/apply_v21.py",
    "tools/run_v21.py",
]
subprocess.run(["git", "add", "--"] + paths, cwd=str(ROOT), check=True)
status = subprocess.run(["git", "status", "--short"], cwd=str(ROOT), capture_output=True, text=True, check=True)
if not status.stdout.strip():
    print("No publishable changes remain; branch is already current.")
    raise SystemExit(0)

subprocess.run(["git", "commit", "-m", "Complete MAXESS Results V21 transformation"], cwd=str(ROOT), check=True)
subprocess.run(["git", "push", "origin", "maxess-results-v21-working"], cwd=str(ROOT), check=True)
print("V21 transformation committed and pushed to maxess-results-v21-working.")
