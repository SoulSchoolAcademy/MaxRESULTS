#!/usr/bin/env python3
"""Executable contract and adversarial tests for the Intelligent Hub kernel."""
from __future__ import annotations

from intelligent_hub_kernel import (
    AuthenticatedContext,
    ConnectionStatus,
    GateStatus,
    IntelligentHubKernel,
    ReferenceAuthenticator,
    validate_collective_event,
)


def fixture():
    auth = ReferenceAuthenticator(b"test-secret")
    hub = IntelligentHubKernel(auth)
    connection = hub.connect(
        owner_subject="subject:anonymous-test-01",
        provider="github",
        installation_id="gh-install-01",
        resource_id="repo-superbrain-01",
        capabilities={
            "read_superbrain_metadata",
            "submit_wisdom_candidate",
            "receive_collective_updates",
            "event_acknowledgement",
        },
    )
    context = AuthenticatedContext(
        subject="subject:anonymous-test-01",
        provider="github",
        installation_id="gh-install-01",
        resource_id="repo-superbrain-01",
    )
    token = auth.issue(context.subject, context.installation_id, context.resource_id)
    return hub, connection, context, token


def valid_wisdom():
    return {
        "subject": "Smallest safe integration boundary",
        "wisdom": "When integrating a mature system, preserve working behavior and establish the smallest verified boundary before expanding scope.",
        "why_it_matters": "This reduces architectural drift and makes failures easier to localize.",
        "applicability": ["software architecture", "NayaPOWER kernel work"],
        "evidence": [{"kind": "test", "state": "observed"}],
        "confidence": 0.92,
    }


def test_connection_and_capability_boundary():
    hub, connection, context, token = fixture()
    assert connection.status == ConnectionStatus.CONNECTED
    assert hub.authorize(connection.connection_id, context, token)


def test_connection_without_contribution_consent_cannot_contribute():
    hub, connection, context, token = fixture()
    result = hub.submit_wisdom(
        connection_id=connection.connection_id,
        context=context,
        token=token,
        contribution=valid_wisdom(),
        human_approved=True,
    )
    assert result.status == GateStatus.REJECTED
    assert "contribution_consent_not_granted" in result.reasons


def test_consent_then_valid_contribution_publishes_cie_without_identity():
    hub, connection, context, token = fixture()
    hub.grant_consent(connection.connection_id, {"wisdom_contribution"})
    result = hub.submit_wisdom(
        connection_id=connection.connection_id,
        context=context,
        token=token,
        contribution=valid_wisdom(),
        human_approved=True,
    )
    assert result.status == GateStatus.ACCEPTED
    assert result.event is not None
    event = result.event
    assert event["status"] == "published"
    assert event["privacy"] == {"identity_included": False, "raw_source_included": False, "privacy_review": "passed"}
    assert "owner_subject" not in event
    assert "connection_id" not in event
    assert "repository_url" not in event
    assert validate_collective_event(event) == []
    assert hub.retrieve_event(event["event_id"])["event_id"] == event["event_id"]


def test_human_review_is_required():
    hub, connection, context, token = fixture()
    hub.grant_consent(connection.connection_id, {"wisdom_contribution"})
    result = hub.submit_wisdom(
        connection_id=connection.connection_id,
        context=context,
        token=token,
        contribution=valid_wisdom(),
        human_approved=False,
    )
    assert result.status == GateStatus.REJECTED
    assert "human_review_required_before_publication" in result.reasons


def test_bad_authentication_is_rejected():
    hub, connection, context, token = fixture()
    hub.grant_consent(connection.connection_id, {"wisdom_contribution"})
    result = hub.submit_wisdom(
        connection_id=connection.connection_id,
        context=context,
        token=token + "tampered",
        contribution=valid_wisdom(),
        human_approved=True,
    )
    assert result.status == GateStatus.REJECTED
    assert "authentication_or_binding_failed" in result.reasons


def test_identity_and_repository_data_are_quarantined():
    hub, connection, context, token = fixture()
    hub.grant_consent(connection.connection_id, {"wisdom_contribution"})
    candidate = valid_wisdom()
    candidate["wisdom"] += " Contact jane@example.com or https://github.com/example/private-superbrain"
    result = hub.submit_wisdom(
        connection_id=connection.connection_id,
        context=context,
        token=token,
        contribution=candidate,
        human_approved=True,
    )
    assert result.status == GateStatus.QUARANTINED
    assert "direct_identifier_detected" in result.reasons
    assert "repository_identity_detected" in result.reasons


def test_raw_private_source_is_quarantined_not_published():
    hub, connection, context, token = fixture()
    hub.grant_consent(connection.connection_id, {"wisdom_contribution"})
    candidate = valid_wisdom()
    candidate["raw_source"] = "private conversation transcript"
    result = hub.submit_wisdom(
        connection_id=connection.connection_id,
        context=context,
        token=token,
        contribution=candidate,
        human_approved=True,
    )
    assert result.status == GateStatus.QUARANTINED
    assert "raw/private source fields are not accepted" in result.reasons[0]
    assert hub.intelligence_feed() == []


def test_duplicate_is_detected():
    hub, connection, context, token = fixture()
    hub.grant_consent(connection.connection_id, {"wisdom_contribution"})
    first = hub.submit_wisdom(connection_id=connection.connection_id, context=context, token=token, contribution=valid_wisdom(), human_approved=True)
    second = hub.submit_wisdom(connection_id=connection.connection_id, context=context, token=token, contribution=valid_wisdom(), human_approved=True)
    assert first.status == GateStatus.ACCEPTED
    assert second.status == GateStatus.DUPLICATE


def test_revoked_connection_cannot_contribute_or_ack():
    hub, connection, context, token = fixture()
    hub.grant_consent(connection.connection_id, {"wisdom_contribution"})
    hub.revoke(connection.connection_id)
    result = hub.submit_wisdom(connection_id=connection.connection_id, context=context, token=token, contribution=valid_wisdom(), human_approved=True)
    assert result.status == GateStatus.REJECTED
    assert "authentication_or_binding_failed" in result.reasons
    assert not hub.acknowledge(connection.connection_id, "cie_missing")


def test_feed_and_acknowledgement():
    hub, connection, context, token = fixture()
    hub.grant_consent(connection.connection_id, {"wisdom_contribution"})
    result = hub.submit_wisdom(connection_id=connection.connection_id, context=context, token=token, contribution=valid_wisdom(), human_approved=True)
    event = result.event
    assert event is not None
    feed = hub.intelligence_feed()
    assert [x["event_id"] for x in feed] == [event["event_id"]]
    assert hub.acknowledge(connection.connection_id, event["event_id"])
    assert (connection.connection_id, event["event_id"]) in hub.acknowledgements


if __name__ == "__main__":
    tests = [value for name, value in globals().items() if name.startswith("test_") and callable(value)]
    for test in tests:
        test()
    print(f"PASS: {len(tests)} Intelligent Hub contract/adversarial tests")
