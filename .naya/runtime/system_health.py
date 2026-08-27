#!/usr/bin/env python3
"""Deterministic NayaPOWER system-health/master-node acceptance contract.

This composes existing canonical contracts; it does not replace boot, memory,
continuity, evidence, or Smart Brain runtimes. The receipt is a current-state
assessment, not a permanent health claim and not a live deployment probe.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / ".naya" / "naya-context-manifest.json"
START = ROOT / "SUPERBRAIN" / "AI-BOOT" / "START-HERE.md"
BOOT = ROOT / ".naya" / "NAYA-CONTEXT-BOOT-PROTOCOL.md"
POLICY = ROOT / ".naya" / "codex" / "HUMAN-CAPABILITY-AND-MASTERY-OPERATING-PROTOCOL.md"
MEMORY_BOOT = ROOT / ".naya" / "memory" / "BOOTSTRAP.md"
COLD_START = ROOT / ".naya" / "runtime" / "cold_start_activation.py"
COLD_CONTRACT = ROOT / ".naya" / "runtime" / "COLD-START-ACTIVATION-ACCEPTANCE.md"
CONTINUITY = ROOT / ".naya" / "runtime" / "continuity_enforcement.py"
EVIDENCE = ROOT / ".naya" / "runtime" / "evidence_runtime.py"
ACTIVATION_CONTRACT = ROOT / ".naya" / "runtime" / "activation_contract.py"
EVENT_INDEX = ROOT / ".naya" / "memory" / "events" / "INDEX.json"
MASTER_NOTE = ROOT / "SUPERBRAIN" / "MASTER-NOTES" / "SN-20260827-CONTINUOUS-BLOCK-EXECUTION-AND-ONE-NET.md"

REQUIRED_FILES = {
    "governance": ROOT / ".naya" / "codex" / "11-RUNTIME-CONSTITUTION.md",
    "context_manifest": MANIFEST,
    "boot_entry": START,
    "context_boot": BOOT,
    "human_capability_policy": POLICY,
    "memory_boot": MEMORY_BOOT,
    "cold_start_acceptance": COLD_START,
    "cold_start_contract": COLD_CONTRACT,
    "continuity_runtime": CONTINUITY,
    "evidence_runtime": EVIDENCE,
    "activation_contract": ACTIVATION_CONTRACT,
    "event_index": EVENT_INDEX,
    "master_note": MASTER_NOTE,
}


def load(path: Path) -> str:
    if not path.is_file():
        raise RuntimeError(f"missing canonical artifact: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def check(results: list[dict[str, Any]], name: str, ok: bool, evidence: str, detail: str = "") -> None:
    results.append({"name": name, "status": "PASS" if ok else "FAIL", "evidence": evidence, "detail": detail})


def run_contract(results: list[dict[str, Any]], name: str, command: list[str]) -> None:
    proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    output = (proc.stdout + ("\n" + proc.stderr if proc.stderr else "")).strip()
    check(results, name, proc.returncode == 0, output[-4000:], f"exit_code={proc.returncode}")


def check_derived_index(results: list[dict[str, Any]]) -> None:
    """Rebuild the canonical derived index, compare it, then restore the checkout."""
    if not EVENT_INDEX.is_file():
        check(results, "derived event/index integrity", False, "INDEX.json missing")
        return
    with tempfile.NamedTemporaryFile(prefix="naya-index-", suffix=".json", delete=False) as tmp:
        backup = Path(tmp.name)
    try:
        shutil.copyfile(EVENT_INDEX, backup)
        proc = subprocess.run(["python", ".naya/memory/smart_notes_v3.py", "index"], cwd=ROOT, text=True, capture_output=True)
        generated = EVENT_INDEX.read_bytes() if EVENT_INDEX.exists() else b""
        expected = backup.read_bytes()
        output = (proc.stdout + ("\n" + proc.stderr if proc.stderr else "")).strip()
        check(results, "derived event/index integrity", proc.returncode == 0 and generated == expected, output[-4000:] or "byte-for-byte comparison", f"exit_code={proc.returncode}")
    finally:
        shutil.copyfile(backup, EVENT_INDEX)
        backup.unlink(missing_ok=True)


def git_head() -> str:
    env_sha = os.environ.get("GITHUB_SHA")
    if env_sha:
        return env_sha
    proc = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, capture_output=True, check=True)
    return proc.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", default="", help="optional path for the JSON receipt")
    args = parser.parse_args()

    started = datetime.now(timezone.utc).isoformat()
    results: list[dict[str, Any]] = []
    manifest = json.loads(load(MANIFEST))
    start = load(START)
    boot = load(BOOT)
    policy = load(POLICY)
    memory_boot = load(MEMORY_BOOT)
    cold_contract = load(COLD_CONTRACT)
    master_note = load(MASTER_NOTE)

    policy_lower = policy.lower()
    boot_lower = boot.lower()
    memory_lower = memory_boot.lower()
    start_lower = start.lower()
    boot_order = {str(item).lower() for item in manifest.get("boot_order", [])}

    check(results, "canonical artifacts documented", all(path.is_file() for path in REQUIRED_FILES.values()), ", ".join(str(p.relative_to(ROOT)) for p in REQUIRED_FILES.values()))
    check(results, "canonical repository", manifest.get("repository") == "SoulSchoolAcademy/NayaPOWER", str(manifest.get("repository")))
    check(results, "canonical governance", manifest.get("governance_branch") == "main" and manifest.get("status") == "CANONICAL", f"branch={manifest.get('governance_branch')} status={manifest.get('status')}")
    check(results, "canonical boot", ".naya/codex/human-capability-and-mastery-operating-protocol.md" in start_lower and ".naya/naya-context-boot-protocol.md" in boot_order, "START-HERE + manifest boot_order")
    registered_ok = manifest.get("subjects", {}).get("human_capability_and_mastery", {}).get("canonical") == ".naya/codex/HUMAN-CAPABILITY-AND-MASTERY-OPERATING-PROTOCOL.md" and all("human_capability_and_mastery" in route for route in manifest.get("task_routes", {}).values())
    check(results, "human capability policy registered", registered_ok, "manifest subject owner + all task routes")
    operating_ok = "execute → verify → oscar → score → integrate → capture → check network → identify next block" in policy_lower and "continuous block execution" in start_lower
    check(results, "operating method", operating_ok, "policy + START-HERE")
    check(results, "block completion evidence", "**complete** only when" in policy_lower and "unknown is never success" in start_lower, "completion/evidence contract")
    check(results, "unfinished-block continuity", "ready-to-run **next execution**" in policy_lower and "same block" in policy_lower, "policy handoff contract")
    check(results, "master scorecard", "after every **1–3 substantive blocks**" in policy_lower and "why is this not a 10?" in policy_lower, "review cadence")
    next_execution_ok = "every meaningful naya execution output must end with a **next execution**" in policy_lower and "every meaningful execution output must end" in start_lower
    check(results, "next execution", next_execution_ok, "policy + START-HERE")
    one_net_ok = "every naya is a specialized node in one governed naya network" in start_lower and "nayapower is the shared governance, continuity, verification, and compounding intelligence substrate" in start_lower
    check(results, "one-network", one_net_ok, "One-Network law")
    authority_ok = "does not override platform/safety constraints" in boot_lower and "human safety & agency → truth & evidence → governing law" in policy_lower
    check(results, "authority", authority_ok, "conduct precedence")
    provenance_ok = "provenance-aware" in policy_lower and "authority" in boot_lower
    check(results, "provenance", provenance_ok, "policy provenance + context authority model")
    human_control_ok = "the human may" in policy_lower and "stop the interaction" in policy_lower
    check(results, "human control", human_control_ok, "agency + explicit stop boundary")
    future_handoff_ok = "next naya" in policy_lower and "next execution" in start_lower
    check(results, "future handoff", future_handoff_ok, "continuity/handoff language")
    specialized_ok = all(token.lower() in policy_lower for token in ("Naya:", "NayaPOWER:", "MAXIS:", "MAXESS:", "Oscar:")) and "competing governance" in policy_lower
    check(results, "specialized node boundaries", specialized_ok, "system role boundary")
    memory_ok = "cis" in memory_lower and "compounding intelligence" in memory_lower and "current reality" in memory_lower
    check(results, "memory/CIS", memory_ok, "memory bootstrap")
    check(results, "canonical event/index", EVENT_INDEX.is_file() and "derived indexes must be rebuildable" in memory_lower, str(EVENT_INDEX.relative_to(ROOT)))
    check_derived_index(results)
    cold_present_ok = COLD_START.is_file() and "unknown is never success" in cold_contract.lower()
    check(results, "cold-start contract present", cold_present_ok, "cold-start runtime + acceptance contract")
    verification_ok = EVIDENCE.is_file() and CONTINUITY.is_file() and ACTIVATION_CONTRACT.is_file()
    check(results, "verification mechanisms", verification_ok, "evidence + continuity + activation contracts")

    # Reuse existing deterministic runtimes rather than reimplementing their checks.
    run_contract(results, "cold-start activation", ["python", str(COLD_START.relative_to(ROOT))])
    run_contract(results, "continuity self-test", ["python", str(CONTINUITY.relative_to(ROOT)), "self-test"])
    run_contract(results, "Smart Brain validation", ["python", ".naya/memory/smart_notes_v3.py", "validate"])
    run_contract(results, "Smart Brain tests", ["python", ".naya/memory/test_smart_brain_v3.py", "-v"])

    by_name = {item["name"]: item["status"] == "PASS" for item in results}
    all_checks_ok = all(by_name.values())
    activation_ok = by_name.get("cold-start activation", False)
    context_ok = all(by_name.get(name, False) for name in ("canonical repository", "canonical governance", "canonical boot", "human capability policy registered", "authority", "provenance", "human control"))
    method_ok = all(by_name.get(name, False) for name in ("operating method", "block completion evidence", "unfinished-block continuity", "master scorecard", "next execution", "future handoff"))
    verification_run_ok = all(by_name.get(name, False) for name in ("derived event/index integrity", "verification mechanisms", "continuity self-test", "Smart Brain validation", "Smart Brain tests"))
    network_ok = all(by_name.get(name, False) for name in ("one-network", "specialized node boundaries", "provenance", "human control"))
    receipt = {
        "schema": "naya/system-health-receipt/v1",
        "status": "HEALTHY" if all_checks_ok else "DEGRADED",
        "generated_at": started,
        "repository": manifest.get("repository"),
        "head": git_head(),
        "governance_branch": manifest.get("governance_branch"),
        "states": {
            "documented": "PASS" if by_name.get("canonical artifacts documented", False) else "FAIL",
            "registered": "PASS" if all(by_name.get(name, False) for name in ("canonical repository", "canonical governance", "human capability policy registered")) else "PARTIAL",
            "activated": "PASS" if activation_ok else "FAIL",
            "context_established": "PASS" if context_ok else "PARTIAL",
            "operating_method_established": "PASS" if method_ok else "PARTIAL",
            "verified": "PASS" if verification_run_ok and all_checks_ok else ("PARTIAL" if verification_run_ok else "FAIL"),
            "network_connected": "PASS" if network_ok else "PARTIAL",
            "healthy": "HEALTHY" if all_checks_ok else "DEGRADED",
        },
        "checks": results,
        "network": {
            "model": "one governed Naya network",
            "substrate": "NayaPOWER",
            "specialized_nodes": ["Naya", "MAXIS", "MAXESS", "Oscar"],
            "privacy_boundary": "private memory is not merged merely because another Naya exists",
            "live_federation": "NOT_PROVEN_BY_THIS_CONTRACT",
        },
        "limitations": [
            "This is a current repository/system contract, not a live external LLM execution proof.",
            "Network-connected means governed architectural integration is verified; live federation is not claimed.",
            "Deployment/Vercel health is intentionally separate from Smart Brain/system health.",
        ],
        "evidence": {
            "canonical_artifacts": [str(p.relative_to(ROOT)) for p in REQUIRED_FILES.values()],
            "runtime_commands": [
                "python .naya/runtime/cold_start_activation.py",
                "python .naya/runtime/continuity_enforcement.py self-test",
                "python .naya/memory/smart_notes_v3.py validate",
                "python .naya/memory/test_smart_brain_v3.py -v",
            ],
        },
    }
    if args.receipt:
        path = (ROOT / args.receipt).resolve() if not Path(args.receipt).is_absolute() else Path(args.receipt)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, ensure_ascii=False))
    return 0 if all_checks_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
