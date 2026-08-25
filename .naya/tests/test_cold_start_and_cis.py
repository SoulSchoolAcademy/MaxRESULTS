#!/usr/bin/env python3
"""Cold-start and next-day CIS acceptance checks."""
from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/".naya"/"runtime")); sys.path.insert(0,str(ROOT/".naya"/"memory"))
from cis_state import build

def main():
    script=ROOT/".naya"/"runtime"/"restore_context.py"
    proc=subprocess.run([sys.executable,str(script),"restore","Superbrain","--limit","5"],cwd=ROOT,text=True,capture_output=True)
    if proc.returncode not in (0,2): raise SystemExit(f"restore runtime failed: {proc.stderr}")
    data=json.loads(proc.stdout)
    required=["current_state","repository_reality","memory","validation","next_best_action"]
    missing=[k for k in required if k not in data]
    if missing: raise SystemExit("cold-start missing: "+", ".join(missing))
    state=build("2026-08-25")
    assert state["source_period"]=="2026-08-25" and state["next_day"]=="2026-08-26"
    assert state["verification_required"] is True
    print(json.dumps({"status":"GREEN","restore_status":data["status"],"head_sha":data["repository_reality"].get("head_sha"),"required_fields_verified":required,"next_day_state":"DERIVED_PENDING_VERIFICATION","source_event_count":state["source_event_count"]},indent=2))
if __name__=="__main__": main()
