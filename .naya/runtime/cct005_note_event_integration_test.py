#!/usr/bin/env python3
from __future__ import annotations

import copy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from cct005_note_event_integration import IntegrationRejected, integrate_verified_note_event


def note_event(status="VERIFIED"):
    return {
        "event_id": "SN-20260829-120000-cct005-integration",
        "type": "learning",
        "subject": "verified reusable intelligence",
        "provenance": {"source": "NAYA-A", "kind": "runtime"},
        "evidence": [{"type": "VERIFIED", "ref": "proof-1"}],
        "verification": {"status": status, "receipt": "receipt-1"},
        "representations": {
            "naya": {
                "id": "SN-20260829-120000-cct005-integration-naya",
                "canonical_event_id": "SN-20260829-120000-cct005-integration",
                "title": "Reusable intelligence",
                "summary": "A verified reusable lesson.",
                "content": "Use the verified lesson.",
            }
        },
    }


def run(name, fn):
    fn()
    print("PASS", name)


def test_complete_chain():
    event = note_event()
    result = integrate_verified_note_event(
        event,
        producer="NAYA-A",
        actor="NAYA-B",
        intended_use="solve-task",
        action="used-block",
        result="task completed",
        classification="SUCCESS",
        evidence=[{"type": "VERIFIED", "ref": "outcome-proof"}],
        confidence=1.0,
        context={"domain": "test"},
        privacy="SCOPED",
    )
    assert result["event_id"] == event["event_id"]
    assert result["block"]["content"]["event_id"] == event["event_id"]
    assert result["outcome"]["provenance"]["source_block"] == result["block"]["block_id"]
    assert result["outcome"]["provenance"]["source_event"] == event["event_id"]
    assert result["value"] > 50.0
    assert "domain" not in result["block"]["content"]


def test_unverified_event_fails_closed():
    try:
        integrate_verified_note_event(
            note_event("SUPPORTED"), producer="NAYA-A", actor="NAYA-B",
            intended_use="solve-task", action="used-block", result="done",
            classification="SUCCESS", evidence=[{"type": "VERIFIED"}],
            confidence=1.0, context={}, privacy="SCOPED",
        )
    except IntegrationRejected:
        return
    raise AssertionError("unverified event was accepted")


def test_missing_smart_note_identity_fails_closed():
    event = note_event(); event["event_id"] = "SE-20260829-120000-not-a-note"
    try:
        integrate_verified_note_event(
            event, producer="NAYA-A", actor="NAYA-B", intended_use="solve-task",
            action="used-block", result="done", classification="SUCCESS",
            evidence=[{"type": "VERIFIED"}], confidence=1.0, context={}, privacy="SCOPED",
        )
    except IntegrationRejected:
        return
    raise AssertionError("non-Smart-Note event was accepted")


def test_actor_must_be_explicit_consumer():
    try:
        integrate_verified_note_event(
            note_event(), producer="NAYA-A", actor="NAYA-C", consumers=["NAYA-B"],
            intended_use="solve-task", action="used-block", result="done",
            classification="SUCCESS", evidence=[{"type": "VERIFIED"}],
            confidence=1.0, context={}, privacy="SCOPED",
        )
    except IntegrationRejected:
        return
    raise AssertionError("unauthorized actor was accepted")


def test_private_context_stays_in_outcome():
    event = note_event()
    result = integrate_verified_note_event(
        event, producer="NAYA-A", actor="NAYA-B", intended_use="solve-task",
        action="used-block", result="done", classification="SUCCESS",
        evidence=[{"type": "VERIFIED"}], confidence=1.0,
        context={"secret": "do-not-export"}, privacy="PRIVATE",
    )
    assert result["outcome"]["privacy"] == "PRIVATE"
    assert result["outcome"]["context"]["secret"] == "do-not-export"
    assert "secret" not in result["block"]["content"]


def test_source_event_is_not_mutated():
    event = note_event(); before = copy.deepcopy(event)
    integrate_verified_note_event(
        event, producer="NAYA-A", actor="NAYA-B", intended_use="solve-task",
        action="used-block", result="done", classification="SUCCESS",
        evidence=[{"type": "VERIFIED"}], confidence=1.0, context={}, privacy="SCOPED",
    )
    assert event == before


def test_duplicate_outcome_cannot_inflate_value():
    event = note_event()
    result = integrate_verified_note_event(
        event, producer="NAYA-A", actor="NAYA-B", intended_use="solve-task",
        action="used-block", result="done", classification="SUCCESS",
        evidence=[{"type": "VERIFIED"}], confidence=1.0, context={}, privacy="SCOPED",
    )
    from cct005_value_feedback import value_signal
    assert value_signal([result["outcome"], result["outcome"]]) == result["value"]


if __name__ == "__main__":
    tests = [
        test_complete_chain,
        test_unverified_event_fails_closed,
        test_missing_smart_note_identity_fails_closed,
        test_actor_must_be_explicit_consumer,
        test_private_context_stays_in_outcome,
        test_source_event_is_not_mutated,
        test_duplicate_outcome_cannot_inflate_value,
    ]
    for fn in tests:
        run(fn.__name__, fn)
    print(f"PASS {len(tests)} CCT-005 integration tests")
