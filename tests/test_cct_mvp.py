from __future__ import annotations

import copy
import json

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".naya" / "runtime"))
from cct_protocol import block_hash, consume_block, create_block, validate_block, verify_link  # noqa: E402
from cct_mvp_proof import build_proof  # noqa: E402
from cct_mvp_second_pass import verify  # noqa: E402


def block_a():
    return create_block(
        agent_id="naya-a", subject="test", claim="verified claim",
        evidence=[{"type": "test", "id": "A"}], verification_method="test",
        audience=["naya-b"], created_at="2026-08-29T00:00:00Z"
    )


def test_two_naya_lineage_and_independent_consumption():
    a = block_a()
    consumed = consume_block(json.loads(json.dumps(a)), "naya-b")
    b = create_block(
        agent_id="naya-b", subject=consumed["subject"], claim="successor",
        evidence=[{"parent": consumed["block_id"]}], verification_method="test",
        audience=["naya-a"], parent={"block_id": a["block_id"], "block_hash": block_hash(a)},
        created_at="2026-08-29T00:01:00Z"
    )
    assert not validate_block(a, consumer_id="naya-b")
    assert not verify_link(b, a)


def test_tamper_is_rejected():
    tampered = copy.deepcopy(block_a())
    tampered["claim"] = "changed"
    assert any("block_id" in e for e in validate_block(tampered))


def test_permission_is_enforced():
    assert any("not permitted" in e for e in validate_block(block_a(), consumer_id="naya-c"))


def test_conversation_dependency_is_rejected():
    dependent = copy.deepcopy(block_a())
    dependent["source_context"] = "conversation_history"
    assert any("source_context" in e for e in validate_block(dependent))


def test_orphan_lineage_is_rejected_by_link_verifier():
    orphan = copy.deepcopy(block_a())
    orphan["lineage"] = {"parent_block_id": "missing-parent", "parent_block_hash": "sha256:missing"}
    orphan["block_id"] = block_hash(orphan)
    assert verify_link(orphan, block_a())


def test_canonical_proof_is_byte_reproducible():
    proof = build_proof()
    proof["second_pass"] = verify(proof)
    proof["final_status"] = "CCT MVP GREEN"
    expected = json.dumps(proof, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    artifact = ROOT / "proofs" / "cctb-v0.1-mvp-proof.json"
    assert artifact.read_text(encoding="utf-8") == expected
