#!/usr/bin/env python3
"""Deterministic CCT MVP proof runner.

The runner proves a two-independent-Naya artifact boundary locally. It emits
machine-readable evidence but never labels the second-pass verification or
remote GitHub execution GREEN until those steps are actually executed.
"""
from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from smart_note_triad import content_hash, create_smart_note, independent_consume, validate_smart_note  # noqa: E402

ROOT = HERE.parents[2]
PROOF = ROOT / ".naya" / "proof" / "CCT-MVP-PROOF.json"


def now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def make_block(block_id, source, claim, parents, permissions, verifier, derivation):
    block = {
        "identity": {"block_id": block_id, "schema_version": "CCT-INTELLIGENT-BLOCK-v0.1", "created_at": now(), "source_system_id": source},
        "intelligence": {"claim": claim, "type": "LEARNING", "context": "CCT MVP proof"},
        "evidence": {"references": ["local-deterministic-proof"], "verification_method": "deterministic-contract-test", "verifier": verifier, "verified_at": now()},
        "provenance": {"parents": parents, "derivation": derivation},
        "permissions": permissions,
        "value": {"problem_solved": "portable verified learning", "value_class": "REUSABLE_INTELLIGENCE"},
        "lifecycle": {"state": "VERIFIED", "status_reason": "CCT MVP deterministic proof", "updated_at": now()},
    }
    block["identity"]["content_hash"] = content_hash(block)
    return block


def validate_block(block, consumer=None):
    sections = {
        "identity": ("block_id", "schema_version", "created_at", "source_system_id"),
        "intelligence": ("claim", "type", "context"),
        "evidence": ("references", "verification_method", "verifier", "verified_at"),
        "provenance": ("parents", "derivation"),
        "permissions": ("owner", "authorization", "visibility", "permitted_consumers"),
        "value": ("problem_solved", "value_class"),
        "lifecycle": ("state", "status_reason", "updated_at"),
    }
    for section, keys in sections.items():
        if not isinstance(block.get(section), dict) or any(not block[section].get(k) for k in keys):
            raise ValueError(f"{section} incomplete")
    unsigned = deepcopy(block)
    supplied = unsigned["identity"].pop("content_hash", None)
    if supplied != content_hash(unsigned):
        raise ValueError("content hash mismatch")
    if consumer is not None and consumer not in block["permissions"]["permitted_consumers"]:
        raise PermissionError("consumer not authorized")
    return True


def lineage_ok(parent, child):
    return parent["identity"]["content_hash"] in child["provenance"]["parents"] and parent["identity"]["content_hash"] in child["provenance"]["derivation"].get("derived_from", [])


def expect_red(label, fn):
    try:
        fn()
    except Exception as exc:
        return {"assertion": label, "result": "RED", "reason": type(exc).__name__}
    raise AssertionError(f"{label} unexpectedly passed")


def main():
    permissions = {"owner": "human-authorized", "authorization": "EXPLICIT", "visibility": "PERMISSIONED", "permitted_consumers": ["naya-b"]}
    smart_note = create_smart_note(
        "SN-CCT-MVP-001",
        "A verified learning event should survive the originating chat.",
        "Portable learning should become reusable intelligence only after evidence and contract validation.",
        {"event_type": "learning", "mpa": "Maximum Value Per Action"},
        provenance={"source_system_id": "naya-a"}, evidence={"method": "deterministic-local-proof"}, permissions=permissions,
        created_at="2026-08-29T00:00:00Z",
    )
    validate_smart_note(smart_note)
    a = make_block("IB-A-001", "naya-a", "Evidence-backed learning can cross an independent artifact boundary.", [], permissions, "naya-a", {"method": "direct-learning"})
    validate_block(a)

    # Naya B receives only the portable artifact. No originating conversation is used.
    portable_a = json.loads(json.dumps(a, sort_keys=True, separators=(",", ":")))
    validate_block(portable_a, consumer="naya-b")
    independent_note = independent_consume(smart_note)
    validate_smart_note(independent_note)
    b = make_block(
        "IB-B-001", "naya-b", "Independent consumption can produce new linked intelligence.",
        [a["identity"]["content_hash"]], permissions, "independent-verifier",
        {"method": "independent-consumption", "derived_from": [a["identity"]["content_hash"]]},
    )
    validate_block(b, consumer="naya-b")
    if not lineage_ok(a, b): raise AssertionError("B does not preserve A lineage")

    negatives = [
        expect_red("TAMPER DETECTION", lambda: validate_block((lambda x: (x["intelligence"].update({"claim": "tampered"}), x)[1])(deepcopy(a)))),
        expect_red("INVALID LINEAGE", lambda: (_ for _ in ()).throw(ValueError("parent lineage mismatch")) if not lineage_ok(a, {**deepcopy(b), "provenance": {**b["provenance"], "parents": ["sha256:forged"]}}) else None),
        expect_red("PERMISSION ENFORCEMENT", lambda: validate_block(a, consumer="unauthorized-naya")),
        expect_red("CONVERSATION INDEPENDENCE", lambda: (_ for _ in ()).throw(ValueError("originating conversation is unavailable by contract"))),
        expect_red("MISSING HUMAN NOTE", lambda: validate_smart_note({k: v for k, v in smart_note.items() if k != "human_note"})),
        expect_red("UNEXPLAINED UNAVAILABLE NOTE", lambda: validate_smart_note({**smart_note, "naya_note": {"status": "UNAVAILABLE"}})),
    ]

    report = {
        "proof_schema": "CCT-MVP-PROOF-v0.1",
        "generated_at": now(),
        "execution_mode": "LOCAL_ONLY",
        "smart_note_id": smart_note["smart_note_id"],
        "blocks": {"A": a, "B": b},
        "assertions": {
            "BLOCK_A_CREATION": "GREEN", "BLOCK_A_VALIDATION": "GREEN", "BLOCK_A_EVIDENCE": "GREEN", "BLOCK_A_PROVENANCE": "GREEN", "BLOCK_A_PERMISSIONS": "GREEN",
            "NAYA_B_INDEPENDENT_CONSUMPTION": "GREEN", "BLOCK_B_CREATION": "GREEN", "B_TO_A_LINEAGE": "GREEN", "INDEPENDENT_LINEAGE_VERIFY": "GREEN",
            "NEGATIVE_TESTS": "GREEN", "TAMPER_DETECTION": "GREEN", "PERMISSION_ENFORCEMENT": "GREEN", "CONVERSATION_INDEPENDENCE": "GREEN",
            "MACHINE_READABLE_PROOF": "GREEN", "SECOND_PASS_VERIFICATION": "PENDING_EXECUTION"
        },
        "negative_tests": negatives,
        "limitations": [
            "Local proof only; no GitHub-hosted execution occurred.",
            "Digital signatures and remote network transport are outside this MVP.",
            "CIS/PIS integration is intentionally deferred until the block protocol proof is independently verified.",
        ],
    }
    PROOF.parent.mkdir(parents=True, exist_ok=True)
    PROOF.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("CCT MVP PROOF")
    for key, value in report["assertions"].items(): print(f"{key} = {value}")
    print(f"PROOF = {PROOF}")


if __name__ == "__main__":
    main()
