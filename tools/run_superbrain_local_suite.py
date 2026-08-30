#!/usr/bin/env python3
"""Run the NayaPOWER Superbrain acceptance suite without GitHub Actions.

This is an execution harness, not a substitute for the authoritative runtime
plane. It runs only local, deterministic checks and records stdout/stderr,
exit codes, elapsed time, and the exact Git HEAD observed at execution start.
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECEIPT_DIR = ROOT / ".naya" / "receipts" / "local-superbrain"
COMMANDS = [
    [sys.executable, "tools/qa_naya_context_boot.py"],
    [sys.executable, "tools/qa_superbrain_continuity.py"],
    [sys.executable, ".naya/runtime/restore_context.py", "restore", "--pretty"],
    [sys.executable, "tools/test_superbrain_a_b_c_compounding.py"],
    [sys.executable, "tools/test_superbrain_adversarial.py"],
]


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def main() -> int:
    RECEIPT_DIR.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc)
    head = git("rev-parse", "HEAD")
    clean_before = git("status", "--porcelain") == ""
    results = []
    overall = 0

    for command in COMMANDS:
        t0 = time.monotonic()
        proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        elapsed_ms = round((time.monotonic() - t0) * 1000, 2)
        result = {
            "command": command,
            "exit_code": proc.returncode,
            "elapsed_ms": elapsed_ms,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
        }
        results.append(result)
        print(f"[{proc.returncode}] {' '.join(command)} ({elapsed_ms} ms)")
        if proc.stdout:
            print(proc.stdout.rstrip())
        if proc.stderr:
            print(proc.stderr.rstrip(), file=sys.stderr)
        if proc.returncode != 0:
            overall = 1
            break

    receipt = {
        "schema": "naya-power-local-superbrain-suite/v1",
        "started_at": started.isoformat(),
        "finished_at": datetime.now(timezone.utc).isoformat(),
        "observed_head": head,
        "clean_worktree_before": clean_before,
        "github_actions_used": False,
        "commands": results,
        "overall": "PASS" if overall == 0 else "FAIL",
    }
    stamp = started.strftime("%Y%m%dT%H%M%SZ")
    path = RECEIPT_DIR / f"suite-{stamp}.json"
    path.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"RECEIPT: {path.relative_to(ROOT)}")
    print(f"SUPERBRAIN LOCAL SUITE: {receipt['overall']}")
    return overall


if __name__ == "__main__":
    raise SystemExit(main())
