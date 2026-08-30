#!/usr/bin/env python3
"""Adversarial tests for the universal Naya Power agent boundary."""
from __future__ import annotations
from naya_agent_interface import AgentInterfaceError, normalize_agent_input, validate_agent_result

def expect_error(fn, *args, **kwargs):
    try:
        fn(*args, **kwargs)
    except AgentInterfaceError:
        return
    raise AssertionError("expected AgentInterfaceError")

def test_normalizes_minimum_valid_agent():
    envelope = normalize_agent_input({"agent_id":"agent-1","host":"example-host","session_id":"session-1","input":"Help me finish this task."})
    payload = envelope.to_kernel_input()
    assert payload["schema"] == "naya-power-agent-interface/v1"
    assert payload["agent"]["id"] == "agent-1"
    assert payload["request"] == "Help me finish this task."
    assert payload["persistence"] == "NONE"

def test_rejects_missing_identity_or_input():
    expect_error(normalize_agent_input, {"host":"x","session_id":"s","input":"x"})
    expect_error(normalize_agent_input, {"agent_id":"a","host":"x","session_id":"s"})

def test_rejects_wrong_protocol():
    expect_error(normalize_agent_input, {"protocol":"other/v1","agent_id":"a","host":"x","session_id":"s","input":"x"})

def test_rejects_empty_strings_and_malformed_lists():
    base = {"agent_id":"a","host":"x","session_id":"s","input":"x"}
    expect_error(normalize_agent_input, {**base,"agent_id":" "})
    expect_error(normalize_agent_input, {**base,"source_refs":["ok",""]})
    expect_error(normalize_agent_input, {**base,"capabilities":"not-a-list"})

def test_preserves_opaque_mission_reference_without_qualifying_it():
    envelope = normalize_agent_input({"agent_id":"a","host":"x","session_id":"s","input":"x","mission_ref":"mission-7"})
    assert envelope.mission_ref == "mission-7"
    assert "mission_ref" in envelope.to_kernel_input()

def test_preserves_provenance_and_constraints():
    envelope = normalize_agent_input({"agent_id":"a","host":"x","session_id":"s","input":"x","source_refs":["drive:doc-1","github:commit-2"],"constraints":["do not deploy"]})
    payload = envelope.to_kernel_input()
    assert payload["source_refs"] == ["drive:doc-1","github:commit-2"]
    assert payload["constraints"] == ["do not deploy"]

def test_result_validation_does_not_promote_completion_to_verification():
    result = validate_agent_result({"status":"COMPLETED","output":"done","evidence_refs":[]})
    assert result["status"] == "COMPLETED"
    assert result["authority"] != "verification"

def test_unknown_is_valid_result_state():
    result = validate_agent_result({"status":"UNKNOWN","output":None})
    assert result["status"] == "UNKNOWN"

def test_rejects_unsupported_result_status():
    expect_error(validate_agent_result, {"status":"VERIFIED","output":"done"})

if __name__ == "__main__":
    tests = [value for name, value in globals().items() if name.startswith("test_")]
    for test in tests:
        test()
    print(f"PASS: {len(tests)} adversarial tests")
