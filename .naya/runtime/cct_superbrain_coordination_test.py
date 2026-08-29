#!/usr/bin/env python3
"""Adversarial acceptance tests for the CCT -> Superbrain boundary."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest

from cct_intelligent_block import make_block
from cct_superbrain_coordination import CoordinationRejected, coordinate_next_action
from naya_claim import Claim


NOW = "2026-08-29T20:00:00Z"
BASE = "abc123"


def claim(*, work_id: str = "W-1", owner: str = "naya-a", base: str = BASE, status: str = "IN_PROGRESS") -> Claim:
    return Claim(
        work_id=work_id,
        owner_naya=owner,
        task_id="T-1",
        scope="superbrain",
        affected_files=(".naya/runtime/example.py",),
        base_commit=base,
        acceptance="tests pass",
        status=status,
        started_at="2026-08-29T19:00:00Z",
        expires_at="2026-08-29T21:00:00Z",
    )


def block(*, consumer: str = "naya-a", verification: str = "VERIFIED") -> dict:
    return make_block(
        block_id="IB-1",
        producer="naya-source",
        content={"next_best_action": "execute"},
        evidence=[{"type": "VERIFIED", "ref": "E-1"}],
        permissions={"consumers": [consumer], "purposes": ["execute"]},
        verification=verification,
    )


def action(*, work_id: str = "W-1", block_id: str = "IB-1") -> dict:
    return {
        "action_id": "A-1",
        "objective": "advance mission",
        "instruction": "run the next verified action",
        "acceptance": "record evidence",
        "claim_work_id": work_id,
        "block_id": block_id,
    }


def test_accepts_verified_bound_action():
    result = coordinate_next_action(
        block(), consumer="naya-a", claim=claim(), current_commit=BASE,
        existing_claims=[], next_action=action(), now=NOW,
    )
    assert result["schema"] == "naya/cct/superbrain-coordination/v1"
    assert result["claim_work_id"] == "W-1"
    assert result["block_id"] == "IB-1"
    assert result["base_commit"] == BASE


def test_rejects_unverified_cct_block():
    with pytest.raises(CoordinationRejected, match="CCT block rejected"):
        coordinate_next_action(
            block(verification="UNVERIFIED"), consumer="naya-a", claim=claim(),
            current_commit=BASE, existing_claims=[], next_action=action(), now=NOW,
        )


def test_rejects_unauthorized_consumer():
    with pytest.raises(CoordinationRejected, match="consumer is not authorized"):
        coordinate_next_action(
            block(consumer="naya-b"), consumer="naya-a", claim=claim(),
            current_commit=BASE, existing_claims=[], next_action=action(), now=NOW,
        )


def test_rejects_stale_claim():
    with pytest.raises(CoordinationRejected, match="stale base commit"):
        coordinate_next_action(
            block(), consumer="naya-a", claim=claim(base="old"),
            current_commit=BASE, existing_claims=[], next_action=action(), now=NOW,
        )


def test_rejects_conflicting_active_claim():
    with pytest.raises(CoordinationRejected, match="conflicting active claims"):
        coordinate_next_action(
            block(), consumer="naya-a", claim=claim(), current_commit=BASE,
            existing_claims=[claim(work_id="W-2", owner="naya-b")], next_action=action(), now=NOW,
        )


def test_rejects_action_bound_to_different_claim():
    with pytest.raises(CoordinationRejected, match="not bound to the active claim"):
        coordinate_next_action(
            block(), consumer="naya-a", claim=claim(), current_commit=BASE,
            existing_claims=[], next_action=action(work_id="W-9"), now=NOW,
        )


def test_rejects_action_bound_to_different_cct_block():
    with pytest.raises(CoordinationRejected, match="not bound to the verified CCT block"):
        coordinate_next_action(
            block(), consumer="naya-a", claim=claim(), current_commit=BASE,
            existing_claims=[], next_action=action(block_id="IB-9"), now=NOW,
        )


def test_rejects_incomplete_action():
    bad = action()
    del bad["instruction"]
    with pytest.raises(CoordinationRejected, match="missing required fields"):
        coordinate_next_action(
            block(), consumer="naya-a", claim=claim(), current_commit=BASE,
            existing_claims=[], next_action=bad, now=NOW,
        )


def test_rejects_expired_claim_even_with_current_commit():
    expired = Claim(
        work_id="W-1", owner_naya="naya-a", task_id="T-1", scope="superbrain",
        affected_files=(".naya/runtime/example.py",), base_commit=BASE,
        acceptance="tests pass", status="IN_PROGRESS",
        started_at="2026-08-29T18:00:00Z", expires_at="2026-08-29T19:00:00Z",
    )
    with pytest.raises(CoordinationRejected, match="claim rejected: active claim is expired"):
        coordinate_next_action(
            block(), consumer="naya-a", claim=expired, current_commit=BASE,
            existing_claims=[], next_action=action(), now=NOW,
        )
