from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".naya" / "runtime"))

from cct_durable import artifact_hash, canonical_bytes, read_block, reload_identity, write_block  # noqa: E402
from cct_protocol import block_hash, consume_block, create_block, validate_block, verify_link  # noqa: E402

FIXTURE = ROOT / "tests" / "fixtures" / "cctb" / "a.json"


def make_a():
    return create_block(
        agent_id="naya-a", subject="durable CCTB", claim="Verified learning survives serialization.",
        evidence=[{"type": "durable_acceptance", "id": "A"}],
        verification_method="repository-local durable acceptance test", audience=["naya-b"],
        created_at="2026-08-29T00:00:00Z",
    )


def test_canonical_fixture_reloads_with_stable_identity():
    a = read_block(FIXTURE)
    assert a["block_id"] == "sha256:0eb22f69d13d717682895e92441db20e44b9a2888fa69213e3fbaff04b27a5ac"
    assert block_hash(a) == a["block_id"]
    assert canonical_bytes(a) == FIXTURE.read_bytes()


def test_durable_a_to_b_successor_lineage(tmp_path: Path):
    a = make_a()
    a_path = tmp_path / "a.json"
    a_write = write_block(a_path, a)
    a_loaded = read_block(a_path)
    assert a_loaded["block_id"] == a["block_id"]
    assert block_hash(a_loaded) == a["block_id"]
    assert a_write["artifact_hash"] == artifact_hash(a_path.read_bytes())

    # B receives only the durable artifact and explicit consumer identity.
    consumed = consume_block(json.loads(a_path.read_text(encoding="utf-8")), "naya-b")
    b = create_block(
        agent_id="naya-b", subject=consumed["subject"],
        claim="Independent Naya B can consume durable A and create a successor.",
        evidence=[{"type": "independent_consumption", "parent_block_id": consumed["block_id"]}],
        verification_method="independent durable consumer test", audience=["naya-a"],
        parent={"block_id": consumed["block_id"], "block_hash": block_hash(a_loaded)},
        created_at="2026-08-29T00:01:00Z",
    )
    b_path = tmp_path / "b.json"
    write_block(b_path, b)
    a_reloaded = read_block(a_path)
    b_reloaded = read_block(b_path)
    assert b_reloaded["lineage"]["parent_block_id"] == a_reloaded["block_id"]
    assert b_reloaded["lineage"]["parent_block_hash"] == block_hash(a_reloaded)
    assert verify_link(b_reloaded, a_reloaded) == []
    assert reload_identity(a_path)["block_id"] == a["block_id"]


def test_tampered_serialized_artifact_is_rejected(tmp_path: Path):
    path = tmp_path / "a.json"
    write_block(path, make_a())
    data = json.loads(path.read_text(encoding="utf-8"))
    data["claim"] = "tampered"
    path.write_text(json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n", encoding="utf-8")
    with pytest.raises(ValueError, match="block_id"):
        read_block(path)


def test_unauthorized_consumer_remains_red_after_reload(tmp_path: Path):
    path = tmp_path / "a.json"
    write_block(path, make_a())
    loaded = read_block(path)
    assert any("not permitted" in error for error in validate_block(loaded, consumer_id="naya-c"))


def test_broken_lineage_is_rejected_after_reload(tmp_path: Path):
    a = make_a()
    b = create_block(
        agent_id="naya-b", subject="durable CCTB", claim="successor", evidence=[{"parent": a["block_id"]}],
        verification_method="test", audience=["naya-a"],
        parent={"block_id": a["block_id"], "block_hash": "sha256:wrong"}, created_at="2026-08-29T00:01:00Z",
    )
    path = tmp_path / "b.json"
    path.write_bytes(canonical_bytes(b))
    loaded = read_block(path)
    assert verify_link(loaded, a)


def test_malformed_artifact_is_rejected(tmp_path: Path):
    path = tmp_path / "bad.json"
    path.write_text('{"schema_version":"not-cctb"}\n', encoding="utf-8")
    with pytest.raises(ValueError, match="invalid durable CCTB block"):
        read_block(path)
