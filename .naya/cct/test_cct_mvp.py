#!/usr/bin/env python3
"""CCT MVP Smart Note Triad + two-independent-Naya contract tests."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from cct_mvp_proof import lineage_ok, make_block, validate_block  # noqa: E402
from smart_note_triad import create_smart_note, independent_consume, immutable_fingerprint, validate_smart_note  # noqa: E402


def expect_red(label, fn):
    try:
        fn()
    except Exception as exc:
        print(f"{label} → RED (correctly rejected: {type(exc).__name__})")
        return
    raise AssertionError(f"{label} unexpectedly passed")


def main():
    permissions = {"owner": "human-authorized", "authorization": "EXPLICIT", "visibility": "PERMISSIONED", "permitted_consumers": ["naya-b"]}
    note = create_smart_note("SN-CCT-MVP-TEST-001", "Human learning.", "Naya understanding.", {"event_type": "learning"}, provenance={"source_system_id": "naya-a"}, evidence={"method": "test"}, permissions=permissions, created_at="2026-08-29T00:00:00Z")
    validate_smart_note(note)
    assert independent_consume(note) == json.loads(json.dumps(note, sort_keys=True, separators=(",", ":")))
    print("SMART NOTE TRIAD → GREEN")

    a = make_block("IB-A-TEST", "naya-a", "A verified learning claim.", [], permissions, "naya-a", {"method": "direct-learning"})
    validate_block(a)
    print("BLOCK A → GREEN")

    b = make_block("IB-B-TEST", "naya-b", "B independently derived learning.", [a["identity"]["content_hash"]], permissions, "independent-verifier", {"method": "independent-consumption", "derived_from": [a["identity"]["content_hash"]]})
    validate_block(b, "naya-b")
    assert lineage_ok(a, b)
    print("NAYA B INDEPENDENT CONSUMPTION → GREEN")
    print("B → A LINEAGE → GREEN")
    print("INDEPENDENT LINEAGE VERIFY → GREEN")

    before = immutable_fingerprint(note)
    changed = deepcopy(note)
    changed["naya_note"]["content"] = "changed"
    assert before != immutable_fingerprint(changed)
    print("TAMPER DETECTION → GREEN")

    bad_parent = deepcopy(b)
    bad_parent["provenance"]["parents"] = ["sha256:forged"]
    expect_red("INVALID LINEAGE", lambda: (_ for _ in ()).throw(ValueError("lineage mismatch")) if not lineage_ok(a, bad_parent) else None)
    expect_red("PERMISSION ENFORCEMENT", lambda: validate_block(a, "unauthorized-naya"))
    expect_red("MISSING HUMAN NOTE", lambda: validate_smart_note({k: v for k, v in note.items() if k != "human_note"}))
    unexplained = deepcopy(note)
    unexplained["naya_note"] = {"status": "UNAVAILABLE"}
    expect_red("UNAVAILABLE WITHOUT REASON", lambda: validate_smart_note(unexplained))
    invalid_version = deepcopy(note)
    invalid_version["schema_version"] = "SMART-NOTE-TRIAD-v999"
    expect_red("INVALID SCHEMA", lambda: validate_smart_note(invalid_version))
    print("NEGATIVE TESTS → GREEN")
    print("CCT MVP LOCAL CONTRACT TESTS → GREEN")


if __name__ == "__main__":
    main()
