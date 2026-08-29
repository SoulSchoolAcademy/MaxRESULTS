#!/usr/bin/env python3
"""Deterministic reference implementation of the CCTB v0.1 proof protocol."""
from __future__ import annotations
import argparse, hashlib, json
from datetime import datetime, timezone
from typing import Any

SCHEMA = "cctb-0.1"
REQUIRED = ("schema_version", "block_type", "producer", "created_at", "subject", "claim", "evidence", "verification", "permissions", "lineage")


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def block_hash(block: dict[str, Any]) -> str:
    body = {k: v for k, v in block.items() if k != "block_id"}
    return "sha256:" + hashlib.sha256(canonical_json(body).encode("utf-8")).hexdigest()


def create_block(*, agent_id: str, subject: str, claim: str, evidence: list[dict[str, Any]], verification_method: str, audience: list[str], parent: dict[str, str] | None = None, created_at: str | None = None) -> dict[str, Any]:
    if not all(isinstance(x, dict) and x for x in evidence):
        raise ValueError("evidence must contain non-empty objects")
    block: dict[str, Any] = {
        "schema_version": SCHEMA,
        "block_type": "learning",
        "producer": {"agent_id": agent_id},
        "created_at": created_at or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "subject": subject,
        "claim": claim,
        "evidence": evidence,
        "verification": {"status": "VERIFIED", "method": verification_method},
        "permissions": {"scope": "network:approved", "audience": sorted(set(audience))},
        "lineage": {
            "parent_block_id": parent["block_id"] if parent else None,
            "parent_block_hash": parent["block_hash"] if parent else None,
        },
    }
    block["block_id"] = block_hash(block)
    return block


def validate_block(block: dict[str, Any], *, consumer_id: str | None = None) -> list[str]:
    errors: list[str] = []
    if not isinstance(block, dict):
        return ["block must be an object"]
    for key in REQUIRED:
        if key not in block or block[key] in (None, "", [], {}):
            errors.append(f"missing {key}")
    if block.get("schema_version") != SCHEMA:
        errors.append("unsupported schema_version")
    if not isinstance(block.get("producer"), dict) or not block.get("producer", {}).get("agent_id"):
        errors.append("producer.agent_id required")
    if block.get("verification", {}).get("status") != "VERIFIED":
        errors.append("verification.status must be VERIFIED")
    if not isinstance(block.get("evidence"), list) or not block.get("evidence"):
        errors.append("evidence is required")
    permissions = block.get("permissions", {})
    audience = permissions.get("audience", []) if isinstance(permissions, dict) else []
    if consumer_id is not None and consumer_id not in audience and "*" not in audience:
        errors.append(f"consumer {consumer_id} is not permitted")
    expected = block_hash(block) if isinstance(block, dict) else None
    if block.get("block_id") != expected:
        errors.append("block_id does not match canonical content")
    lineage = block.get("lineage", {})
    if lineage.get("parent_block_id") is None and lineage.get("parent_block_hash") is not None:
        errors.append("parent_block_hash cannot exist without parent_block_id")
    if lineage.get("parent_block_id") is not None and not lineage.get("parent_block_hash"):
        errors.append("parent_block_hash required for linked successor")
    return errors


def consume_block(block: dict[str, Any], consumer_id: str) -> dict[str, Any]:
    errors = validate_block(block, consumer_id=consumer_id)
    if errors:
        raise ValueError("; ".join(errors))
    return {
        "block_id": block["block_id"],
        "subject": block["subject"],
        "claim": block["claim"],
        "evidence": block["evidence"],
        "verification": block["verification"],
        "producer": block["producer"],
        "lineage": block["lineage"],
    }


def verify_link(child: dict[str, Any], parent: dict[str, Any]) -> list[str]:
    errors = validate_block(child)
    if errors:
        return errors
    if child["lineage"].get("parent_block_id") != parent.get("block_id"):
        errors.append("parent_block_id does not match parent")
    if child["lineage"].get("parent_block_hash") != parent.get("block_id"):
        errors.append("parent_block_hash does not match parent block hash")
    return errors


def self_test() -> int:
    a = create_block(
        agent_id="naya-a", subject="verified execution efficiency", claim="Local proof should precede scarce remote CI.",
        evidence=[{"type": "repository_issue", "ref": "#80"}], verification_method="independent protocol test", audience=["naya-b"], created_at="2026-08-29T00:00:00Z")
    consumed = consume_block(a, "naya-b")
    assert consumed["block_id"] == a["block_id"]
    assert consumed["claim"] == a["claim"]
    b = create_block(
        agent_id="naya-b", subject="verified execution efficiency", claim="A consumer can preserve and extend verified learning without originating chat context.",
        evidence=[{"type": "cctb_consumer_test", "ref": a["block_id"]}], verification_method="independent consumer test", audience=["naya-a"], parent={"block_id": a["block_id"], "block_hash": a["block_id"]}, created_at="2026-08-29T00:01:00Z")
    assert verify_link(b, a) == []
    tampered = dict(a); tampered["claim"] = "tampered"
    assert any("block_id" in e for e in validate_block(tampered, consumer_id="naya-b"))
    denied = validate_block(a, consumer_id="naya-c")
    assert any("not permitted" in e for e in denied)
    print("NAYA A CREATES VERIFIED BLOCK → GREEN")
    print("NAYA B INDEPENDENTLY CONSUMES A → GREEN")
    print("NAYA B CREATES LINKED SUCCESSOR → GREEN")
    print("LINEAGE A → B VERIFIED → GREEN")
    print("TAMPER DETECTION → GREEN")
    print("PERMISSION ENFORCEMENT → GREEN")
    print("CCTB v0.1 TWO-NAYA PROOF → GREEN")
    print(json.dumps({"root_block_id": a["block_id"], "successor_block_id": b["block_id"], "parent_block_id": b["lineage"]["parent_block_id"]}, indent=2))
    return 0


def main() -> int:
    p = argparse.ArgumentParser(); p.add_argument("command", choices=["self-test"]); args = p.parse_args(); return self_test()

if __name__ == "__main__":
    raise SystemExit(main())
