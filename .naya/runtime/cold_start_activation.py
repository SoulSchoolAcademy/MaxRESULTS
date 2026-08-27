#!/usr/bin/env python3
"""Deterministic cold-start acceptance test for the canonical Naya boot contract.

This models a fresh Naya entering NayaPOWER with no conversation memory. It proves
repository-level activation state: authority, boot order, task routing, policy
content, operating-method contract, and explicit state transitions. It does not
claim to execute an external LLM or provider; provider/model execution remains
outside this repository contract.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / ".naya" / "naya-context-manifest.json"
BOOT = ROOT / ".naya" / "NAYA-CONTEXT-BOOT-PROTOCOL.md"
START = ROOT / "SUPERBRAIN" / "AI-BOOT" / "START-HERE.md"
POLICY = ROOT / ".naya" / "codex" / "HUMAN-CAPABILITY-AND-MASTERY-OPERATING-PROTOCOL.md"
CONSTITUTION = ROOT / ".naya" / "codex" / "11-RUNTIME-CONSTITUTION.md"
MASTER_NOTE = ROOT / "SUPERBRAIN" / "MASTER-NOTES" / "SN-20260827-CONTINUOUS-BLOCK-EXECUTION-AND-ONE-NET.md"

EXPECTED_POLICY = ".naya/codex/HUMAN-CAPABILITY-AND-MASTERY-OPERATING-PROTOCOL.md"
EXPECTED_CONSTITUTION = ".naya/codex/11-RUNTIME-CONSTITUTION.md"
BLOCK_CYCLE = "EXECUTE → VERIFY → OSCAR → SCORE → INTEGRATE → CAPTURE → CHECK NETWORK → IDENTIFY NEXT BLOCK"


def fail(message: str) -> None:
    raise AssertionError(message)


def load(path: Path) -> str:
    if not path.is_file():
        fail(f"missing canonical artifact: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        fail(f"{label} missing required contract: {needle}")


def main() -> int:
    # A fresh Naya begins with no session memory. Only canonical repository state
    # is used to establish the modeled boot state.
    state = {
        "conversation_memory": "EMPTY",
        "activation_state": "DOCUMENTED",
        "context_state": "UNKNOWN",
        "operating_method_state": "UNKNOWN",
        "repository": None,
        "governance_branch": None,
        "policy": None,
        "evidence": [],
    }

    manifest = json.loads(load(MANIFEST))
    boot = load(BOOT)
    start = load(START)
    policy = load(POLICY)
    constitution = load(CONSTITUTION)
    master_note = load(MASTER_NOTE)

    state["repository"] = manifest.get("repository")
    state["governance_branch"] = manifest.get("governance_branch")
    state["policy"] = manifest.get("subjects", {}).get("human_capability_and_mastery", {}).get("canonical")

    if manifest.get("status") != "CANONICAL":
        fail("context manifest is not CANONICAL")
    if state["repository"] != "SoulSchoolAcademy/NayaPOWER":
        fail("canonical repository identity is incorrect")
    if state["governance_branch"] != "main":
        fail("governance branch is not main")
    if state["policy"] != EXPECTED_POLICY:
        fail("Human Capability & Mastery subject owner is not canonical")
    if EXPECTED_POLICY not in manifest.get("boot_order", []):
        fail("Human Capability & Mastery policy is absent from boot_order")
    if EXPECTED_CONSTITUTION not in manifest.get("boot_order", []):
        fail("governing constitution is absent from boot_order")

    for route_name, route in manifest.get("task_routes", {}).items():
        if "human_capability_and_mastery" not in route:
            fail(f"Human Capability & Mastery policy missing from task route: {route_name}")

    require(boot, EXPECTED_POLICY, "context boot")
    require(start, EXPECTED_POLICY, "START HERE")
    require(boot, "does not override platform/safety constraints", "authority preservation")
    require(start, "ACTIVATE BEFORE SUBSTANTIVE WORK", "policy activation")
    require(policy, "DO NOT BUILD FOR THE MACHINE. BUILD FOR THE HUMAN.", "human-outcome law")
    require(policy, "No Naya may claim that a human understands something", "understanding evidence law")
    require(policy, "MEASURE", "mastery loop")
    require(policy, "MASTER", "mastery loop")

    # The block method is validated as an integrated operating contract rather
    # than by filename existence. All canonical steps and handoff requirements
    # must be present in the activated policy and boot entry.
    require(policy, BLOCK_CYCLE, "continuous block cycle")
    for phrase in (
        "MISSION",
        "SOURCE OF TRUTH",
        "CURRENT STATE",
        "SCOPE",
        "SUCCESS CRITERIA",
        "EXECUTE",
        "VERIFY",
        "OSCAR",
        "SCORE",
        "INTEGRATE",
        "CAPTURE",
        "CHECK NETWORK",
        "NEXT BLOCK",
        "Block completion contract",
        "Continuous-flow rule",
        "Review cadence",
        "WHY IS THIS NOT A 10?",
        "ready-to-run **NEXT EXECUTION**",
    ):
        require(policy, phrase, "block operating contract")

    require(start, BLOCK_CYCLE, "START HERE block cycle")
    require(start, "One-Network law", "START HERE One-Network law")
    require(start, "Every Naya is a specialized node in one governed Naya network", "One-Network architecture")
    require(master_note, BLOCK_CYCLE, "Master Note block cycle")
    require(master_note, "Every Naya is a specialized node in one governed Naya network", "Master Note One-Network architecture")
    require(master_note, "After every 1–3 substantive blocks", "Master Scorecard cadence")
    require(master_note, "Every meaningful execution output must end with a ready-to-run Next Execution", "Next Execution law")

    if "does not override platform/safety constraints" not in boot:
        fail("boot protocol does not preserve higher-order authority")
    if not constitution.strip():
        fail("governing constitution could not be loaded")

    state["evidence"] = [
        "canonical_repository",
        "canonical_governance_branch",
        "canonical_boot_entry",
        "canonical_constitution",
        "human_capability_policy_loaded",
        "authority_relationship_verified",
        "task_routes_verified",
        "core_policy_requirements_verified",
        "continuous_block_contract_verified",
        "unfinished_block_handoff_verified",
        "master_scorecard_cadence_verified",
        "next_execution_requirement_verified",
        "one_network_contract_verified",
        "conversation_memory_empty",
    ]
    state["activation_state"] = "ACTIVATED"
    state["context_state"] = "CONTEXT ESTABLISHED"
    state["operating_method_state"] = "OPERATING-METHOD ESTABLISHED"

    receipt = {
        "schema": "naya/cold-start-activation-receipt/v2",
        "status": "VERIFIED",
        "scope": "repository-level cold-start modeled activation",
        "conversation_memory": state["conversation_memory"],
        "activation_state": state["activation_state"],
        "context_state": state["context_state"],
        "operating_method_state": state["operating_method_state"],
        "repository": state["repository"],
        "governance_branch": state["governance_branch"],
        "policy": state["policy"],
        "policy_sha256": hashlib.sha256(policy.encode("utf-8")).hexdigest(),
        "evidence": state["evidence"],
        "limitation": "This proves the canonical repository boot contract, not an external LLM/provider execution.",
    }

    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
