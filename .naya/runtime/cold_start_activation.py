#!/usr/bin/env python3
"""Deterministic cold-start acceptance test for the canonical Naya boot contract.

This models a fresh Naya entering NayaPOWER with no conversation memory. It proves
repository-level activation state: authority, boot order, task routing, policy
content, and explicit state transitions. It does not claim to execute an external
LLM or provider; provider/model execution remains outside this repository contract.
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


def fail(message: str) -> None:
    raise AssertionError(message)


def load(path: Path) -> str:
    if not path.is_file():
        fail(f"missing canonical artifact: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def main() -> int:
    # A fresh Naya begins with no session memory. Only canonical repository state
    # is used to establish the modeled boot state.
    state = {
        "conversation_memory": "EMPTY",
        "activation_state": "DOCUMENTED",
        "context_state": "UNKNOWN",
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

    state["repository"] = manifest.get("repository")
    state["governance_branch"] = manifest.get("governance_branch")
    state["policy"] = manifest.get("subjects", {}).get("human_capability_and_mastery", {}).get("canonical")

    expected_policy = ".naya/codex/HUMAN-CAPABILITY-AND-MASTERY-OPERATING-PROTOCOL.md"
    expected_constitution = ".naya/codex/11-RUNTIME-CONSTITUTION.md"

    if manifest.get("status") != "CANONICAL":
        fail("context manifest is not CANONICAL")
    if state["repository"] != "SoulSchoolAcademy/NayaPOWER":
        fail("canonical repository identity is incorrect")
    if state["governance_branch"] != "main":
        fail("governance branch is not main")
    if state["policy"] != expected_policy:
        fail("Human Capability & Mastery subject owner is not canonical")
    if expected_policy not in manifest.get("boot_order", []):
        fail("Human Capability & Mastery policy is absent from boot_order")

    for route_name, route in manifest.get("task_routes", {}).items():
        if "human_capability_and_mastery" not in route:
            fail(f"Human Capability & Mastery policy missing from task route: {route_name}")

    if expected_constitution not in manifest.get("boot_order", []):
        fail("governing constitution is absent from boot_order")
    if expected_policy not in boot or expected_policy not in start:
        fail("canonical boot entry does not explicitly activate the policy")
    if "does not override platform/safety constraints" not in boot:
        fail("boot protocol does not preserve higher-order authority")
    if "ACTIVATE BEFORE SUBSTANTIVE WORK" not in start:
        fail("START HERE does not require policy activation before substantive work")
    if "DO NOT BUILD FOR THE MACHINE. BUILD FOR THE HUMAN." not in policy:
        fail("core human-outcome law is missing")
    if "No Naya may claim that a human understands something" not in policy:
        fail("evidence threshold for understanding is missing")
    if "MEASURE" not in policy or "MASTER" not in policy:
        fail("mastery operating loop is incomplete")
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
        "conversation_memory_empty",
    ]
    state["activation_state"] = "ACTIVATED"
    state["context_state"] = "CONTEXT ESTABLISHED"

    receipt = {
        "schema": "naya/cold-start-activation-receipt/v1",
        "status": "VERIFIED",
        "scope": "repository-level cold-start modeled activation",
        "conversation_memory": state["conversation_memory"],
        "activation_state": state["activation_state"],
        "context_state": state["context_state"],
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
