#!/usr/bin/env python3
"""Positive and deliberate-failure tests for zero-setup activation."""
from __future__ import annotations
import json
import tempfile
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "runtime"))
from activation_contract import validate_manifest
from activation_engine import activate, chunk_text, inspect_package, stable_document_identity


def doc(i: int, content: str | None = None) -> dict:
    return {
        "document_id": f"ACT-{i:02d}",
        "version": "1.0",
        "package_id": "NAYA-ACTIVATION-TEST",
        "order": i,
        "purpose": f"Activation document {i}",
        "content": content or (f"Document {i} canonical knowledge. " * 30),
    }


def manifest(n: int = 1) -> dict:
    return {
        "schema_version": 1,
        "package_id": "NAYA-ACTIVATION-TEST",
        "package_version": "1.0",
        "north_star": "activate verified memory",
        "documents": [doc(i) for i in range(1, n + 1)],
    }


def main() -> int:
    assert not validate_manifest(manifest(1))
    one = inspect_package(manifest(1))
    ten = inspect_package(manifest(10))
    twenty = inspect_package(manifest(20))
    assert one["status"] == "READY" and one["document_count"] == 1
    assert ten["status"] == "READY" and ten["document_count"] == 10
    assert twenty["status"] == "READY" and twenty["document_count"] == 20

    # Duplicate identity is deterministic and content-sensitive.
    a = stable_document_identity("P", "D", "1", "same")
    b = stable_document_identity("P", "D", "1", "same")
    c = stable_document_identity("P", "D", "1", "changed")
    assert a == b and a != c

    # Out-of-order / missing document is visible, never silently accepted.
    bad = manifest(3)
    bad["documents"] = [bad["documents"][0], bad["documents"][2]]
    bad["documents"][1]["order"] = 3
    assert inspect_package(bad)["status"] == "PARTIAL"

    # Empty content is a deliberate failure.
    empty = manifest(1)
    empty["documents"][0]["content"] = ""
    assert inspect_package(empty)["status"] == "FAILED"

    # Malformed package fails closed.
    malformed = manifest(1)
    malformed["documents"][0].pop("document_id")
    assert inspect_package(malformed)["status"] == "FAILED"

    # Activation is idempotent at the derived state/receipt layer.
    with tempfile.TemporaryDirectory() as td:
        import activation_engine as ae
        old_root, old_state, old_receipt = ae.ACTIVATION_ROOT, ae.STATE_FILE, ae.RECEIPT_FILE
        ae.ACTIVATION_ROOT = Path(td) / "activations"
        ae.STATE_FILE = ae.ACTIVATION_ROOT / "ACTIVATION-STATE.json"
        ae.RECEIPT_FILE = ae.ACTIVATION_ROOT / "ACTIVATION-RECEIPT.json"
        try:
            first = activate(manifest(10))
            state1 = ae.STATE_FILE.read_text(encoding="utf-8")
            second = activate(manifest(10))
            state2 = ae.STATE_FILE.read_text(encoding="utf-8")
            assert first == second and state1 == state2
            receipt = json.loads(ae.RECEIPT_FILE.read_text(encoding="utf-8"))
            assert receipt["verified"] is True and receipt["document_count"] == 10
        finally:
            ae.ACTIVATION_ROOT, ae.STATE_FILE, ae.RECEIPT_FILE = old_root, old_state, old_receipt

    print("PASS — activation positive, duplicate, idempotency, ordering, and deliberate-failure tests GREEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
