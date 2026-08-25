#!/usr/bin/env python3
"""Cold-start and next-day CIS acceptance checks."""
from __future__ import annotations
import json, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/".naya"/"runtime")); sys.path.insert(0,str(ROOT/".naya"/"memory"))
from cis_state import build

def run_restore(root:Path):
    script=root/".naya"/"runtime"/"restore_context.py"
    return subprocess.run([sys.executable,str(script),"restore","Superbrain","--limit","5"],cwd=root,text=True,capture_output=True)

def assert_restored(proc):
    if proc.returncode!=0: raise SystemExit(f"cold-start restore must be VERIFIED; exit={proc.returncode}: {proc.stderr or proc.stdout}")
    data=json.loads(proc.stdout)
    required=["current_state","repository_reality","memory","validation","next_best_action"]
    missing=[k for k in required if k not in data]
    if missing: raise SystemExit("cold-start missing: "+", ".join(missing))
    assert data["status"]=="VERIFIED"
    assert data["repository_reality"]["available"] is True
    assert data["repository_reality"]["clean"] is True
    assert data["validation"]["passed"] is True
    assert data["current_state"]
    assert data["next_best_action"]
    return data

def main():
    # Positive: the live repository must restore with a verified status, not a permissive UNKNOWN.
    live=assert_restored(run_restore(ROOT))
    # Strong cold-start: reconstruct the runtime from repository files in a fresh temporary checkout.
    with tempfile.TemporaryDirectory() as tmp:
        fresh=Path(tmp)
        shutil.copytree(ROOT/".naya",fresh/".naya")
        subprocess.run(["git","init","-q"],cwd=fresh,check=True)
        subprocess.run(["git","config","user.email","naya-test@example.invalid"],cwd=fresh,check=True)
        subprocess.run(["git","config","user.name","Naya Cold Start Test"],cwd=fresh,check=True)
        subprocess.run(["git","add",".naya"],cwd=fresh,check=True)
        subprocess.run(["git","commit","-qm","cold-start fixture"],cwd=fresh,check=True)
        cold=assert_restored(run_restore(fresh))
    state=build("2026-08-25")
    assert state["source_period"]=="2026-08-25" and state["next_day"]=="2026-08-26"
    assert state["verification_required"] is True
    print(json.dumps({"status":"GREEN","restore_status":live["status"],"fresh_checkout_restore_status":cold["status"],"head_sha":live["repository_reality"].get("head_sha"),"required_fields_verified":["current_state","repository_reality","memory","validation","next_best_action"],"next_day_state":"DERIVED_PENDING_VERIFICATION","source_event_count":state["source_event_count"]},indent=2))
if __name__=="__main__": main()
