#!/usr/bin/env python3
"""Machine acceptance test for Naya-owned human-facing successor-torch delivery.

This test exercises the canonical continuity_enforcement runtime at its
structured-handoff boundary. It proves that a meaningful execution requires
a complete successor torch and, when the next actor is human, a Naya-authored
human-facing continuation with explicit return payload requirements.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".naya" / "runtime"))
import continuity_enforcement as ce  # noqa: E402


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def fixture(next_actor: str = "human") -> dict:
    policy = ce.load_policy()
    handoff = {
        "mission": "Test Naya-owned torch delivery",
        "source_of_truth": "SoulSchoolAcademy/NayaPOWER",
        "current_state": "Testing the structured handoff boundary",
        "protected_baseline": "Continuity law and UNKNOWN semantics",
        "work_completed": "Created positive and negative torch fixtures",
        "evidence": "Runtime acceptance test",
        "decisions": "Human continuation remains Naya-authored",
        "lessons": "Torch has both successor and human delivery targets",
        "unknowns": "None for this fixture",
        "risks": "False completion if human continuation is omitted",
        "recommendation": "Require Naya-authored human continuation",
        "next_action": "Run the governance verification command now.",
        "next_actor": next_actor,
        "ready_to_run_execution": "WHERE: NayaPOWER. WHY: verify the continuity contract. CURRENT STATE: testing the structured handoff boundary. WHAT WAS VERIFIED: runtime fixture. WHAT IS UNKNOWN: none. WHAT IS PROTECTED: continuity law. WHAT IS BLOCKED: none. WHAT TO READ: canonical contract and tests. WHAT TO DO: run the governance verification command. WHAT NOT TO DO: bypass validators. WHAT TO PRESERVE: evidence and UNKNOWN semantics. WHAT TO VERIFY: exact command result. EXPECTED RESULT: the contract passes. FAILURE HANDLING: stop at the first real failure and preserve evidence. NEXT DECISION POINT: authoritative gate.",
        "expected_output": "Exact verification output and the first real failure, if any.",
        "success_criteria": "All positive torch requirements pass and every deliberate-negative omission is rejected.",
        "verification": "Run the continuity and project contract regression tests against the exact tested SHA.",
        "human_continuation": "Open the prepared execution command, run it, and return the exact output without interpreting it.",
        "human_continuation_naya_authored": True,
    }
    if next_actor == "human":
        handoff["human_action"] = "Run the prepared governance verification command and return its exact output."
        handoff["human_return_payload"] = "Paste the exact command output and any visible failure identifiers."
    return {
        "event_id": "SE-20260829-180000-torch-delivery-positive-test",
        "effective_at": policy["structured_handoff_effective_at"],
        "event_type": "execution-milestone",
        "representations": {
            "naya": {
                "id": "SN-20260829-180000-torch-naya",
                "lessons": ["Naya owns continuation; the human does not author the next prompt."],
                "next_best_actions": ["Run the next governance verification."],
            },
            "shawn": {
                "id": "SN-20260829-180000-torch-human",
                "lessons": ["The human receives and uses the Naya-authored continuation."],
                "next_best_actions": ["Use the provided Naya continuation."],
            },
        },
        "verification": {"status": "VERIFIED", "receipt": "RCPT-torch-delivery-test"},
        "receipt": {"receipt_id": "RCPT-torch-delivery-test"},
        "delivery": {"state": "VERIFIED"},
        "continuity": {
            "handoff_url": "https://example.invalid/torch-handoff",
            "learning_status": "LEARNED",
            "execution_state": "COMPLETED",
            "handoff": handoff,
        },
    }


def main() -> int:
    policy = ce.load_policy()
    required = {"human_continuation", "human_continuation_naya_authored"}
    configured = set(policy.get("structured_handoff_fields", []))
    if not required.issubset(configured):
        fail("policy does not require both human continuation fields")
    if policy.get("contract", {}).get("naya_owned_human_continuation") is not True:
        fail("policy does not enable Naya-owned human continuation")
    if policy.get("contract", {}).get("human_prompt_authoring_required") != "conditional":
        fail("policy does not use conditional human prompt authoring")

    good = fixture("human")
    good_errors = ce.check_event(good, Path("positive-torch-fixture.json"), policy)
    if good_errors:
        fail("positive Naya-owned torch fixture rejected: " + "; ".join(good_errors))
    print("GREEN PROOF: complete successor handoff + Naya-authored human continuation satisfies the structured continuity contract.")

    missing_continuation = json.loads(json.dumps(good))
    del missing_continuation["continuity"]["handoff"]["human_continuation"]
    del missing_continuation["continuity"]["handoff"]["human_continuation_naya_authored"]
    del missing_continuation["continuity"]["handoff"]["human_action"]
    del missing_continuation["continuity"]["handoff"]["human_return_payload"]
    missing_errors = ce.check_event(missing_continuation, Path("negative-torch-fixture.json"), policy)
    if not any("structured Future-Naya handoff missing required fields" in error and "human_continuation" in error for error in missing_errors):
        fail("negative fixture did not make missing human-facing continuation RED")
    print("RED PROOF: removing the Naya-authored human continuation fails the structured continuity contract.")

    wrong_author = json.loads(json.dumps(good))
    wrong_author["continuity"]["handoff"]["human_continuation_naya_authored"] = False
    wrong_errors = ce.check_event(wrong_author, Path("wrong-author-torch-fixture.json"), policy)
    if not any("structured Future-Naya handoff missing required fields" in error and "human_continuation_naya_authored" in error for error in wrong_errors):
        fail("wrong-author fixture did not reject non-Naya-authored continuation")
    print("RED PROOF: marking the human continuation as not Naya-authored fails the contract.")

    missing_delivery = json.loads(json.dumps(good))
    missing_delivery["continuity"]["handoff"]["verification"] = ""
    missing_delivery_errors = ce.check_event(missing_delivery, Path("missing-delivery-fixture.json"), policy)
    if not any("next action delivery missing verification" in error for error in missing_delivery_errors):
        fail("missing-delivery fixture did not reject missing verification")
    print("RED PROOF: removing verification fails the canonical successor-torch contract.")

    print("PASS: Naya-owned human-facing torch delivery is policy-configured and machine-enforced at the structured handoff boundary.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
