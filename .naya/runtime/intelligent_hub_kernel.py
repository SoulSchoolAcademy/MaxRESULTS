#!/usr/bin/env python3
"""Contract-first Intelligent Hub connection kernel.

This module is provider-neutral. It proves the stable boundary between a
sovereign Superbrain and the Collective without treating GitHub repositories as
the synchronization primitive.

It deliberately keeps collective objects free of contributor identity and raw
source material. Provider authentication is an adapter concern; the kernel
accepts only an authenticated provider context and verifies that context
against the connection's least-privilege binding.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
import hashlib
import hmac
import json
import re
import secrets
from typing import Any, Callable, Iterable

PROTOCOL_VERSION = "1.0"
CIE_SCHEMA_VERSION = "1.0"

EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
GITHUB_REPO_RE = re.compile(r"https?://(?:www\.)?github\.com/[^\s/]+/[^\s/?#]+", re.I)
SECRET_RE = re.compile(
    r"(?:sk-[A-Za-z0-9_-]{16,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|Bearer\s+[A-Za-z0-9._-]{20,})"
)


class ConnectionStatus(str, Enum):
    PENDING = "PENDING"
    CONNECTED = "CONNECTED"
    DEGRADED = "DEGRADED"
    REVOKED = "REVOKED"
    UNKNOWN = "UNKNOWN"


class GateStatus(str, Enum):
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    NEEDS_REVIEW = "needs_review"
    QUARANTINED = "quarantined"
    DUPLICATE = "duplicate"


@dataclass(frozen=True)
class AuthenticatedContext:
    subject: str
    provider: str
    installation_id: str
    resource_id: str
    authenticated: bool = True


@dataclass
class Connection:
    connection_id: str
    owner_subject: str
    provider: str
    installation_id: str
    resource_id: str
    capabilities: set[str] = field(default_factory=set)
    consent_scope: set[str] = field(default_factory=set)
    status: ConnectionStatus = ConnectionStatus.PENDING
    created_at: str = ""
    updated_at: str = ""
    revoked_at: str | None = None


@dataclass(frozen=True)
class ContributionResult:
    status: GateStatus
    contribution_id: str
    event: dict[str, Any] | None
    reasons: tuple[str, ...]


class ReferenceAuthenticator:
    """Small HMAC authenticator used only by the reference fixture/tests.

    A production GitHub-backed adapter should validate a GitHub App installation
    and provider credentials instead of exposing this reference secret model.
    """

    def __init__(self, secret: bytes | None = None) -> None:
        self._secret = secret or secrets.token_bytes(32)

    def issue(self, subject: str, installation_id: str, resource_id: str) -> str:
        payload = f"{subject}|{installation_id}|{resource_id}".encode()
        sig = hmac.new(self._secret, payload, hashlib.sha256).hexdigest()
        return f"{subject}|{installation_id}|{resource_id}|{sig}"

    def verify(self, token: str, expected: AuthenticatedContext) -> bool:
        parts = token.split("|")
        if len(parts) != 4 or not expected.authenticated:
            return False
        subject, installation_id, resource_id, signature = parts
        payload = f"{subject}|{installation_id}|{resource_id}".encode()
        expected_sig = hmac.new(self._secret, payload, hashlib.sha256).hexdigest()
        return (
            hmac.compare_digest(signature, expected_sig)
            and subject == expected.subject
            and installation_id == expected.installation_id
            and resource_id == expected.resource_id
        )


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _stable_id(prefix: str, value: Any) -> str:
    canonical = json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return f"{prefix}_{hashlib.sha256(canonical.encode()).hexdigest()[:24]}"


def _contains_forbidden_text(value: Any) -> list[str]:
    text = json.dumps(value, ensure_ascii=False, sort_keys=True)
    reasons: list[str] = []
    if SECRET_RE.search(text):
        reasons.append("secret_or_credential_detected")
    if EMAIL_RE.search(text):
        reasons.append("direct_identifier_detected")
    if GITHUB_REPO_RE.search(text):
        reasons.append("repository_identity_detected")
    return reasons


def validate_collective_event(event: dict[str, Any]) -> list[str]:
    required = {
        "event_id", "schema_version", "event_type", "created_at", "effective_at",
        "subject", "wisdom", "why_it_matters", "applicability", "evidence",
        "confidence", "provenance", "privacy", "relationships", "supersedes",
        "status", "verification_receipt",
    }
    errors = sorted(required - event.keys())
    if event.get("schema_version") != CIE_SCHEMA_VERSION:
        errors.append("schema_version_mismatch")
    try:
        datetime.fromisoformat(str(event["created_at"]).replace("Z", "+00:00"))
        datetime.fromisoformat(str(event["effective_at"]).replace("Z", "+00:00"))
    except (KeyError, ValueError):
        errors.append("timestamps_must_be_timezone_aware_iso8601")
    if not isinstance(event.get("confidence"), (int, float)) or not 0 <= float(event.get("confidence", -1)) <= 1:
        errors.append("confidence_must_be_0_to_1")
    privacy = event.get("privacy") or {}
    if privacy.get("identity_included") is not False:
        errors.append("collective_identity_must_be_excluded")
    if privacy.get("raw_source_included") is not False:
        errors.append("collective_raw_source_must_be_excluded")
    if not isinstance(event.get("wisdom"), str) or not event["wisdom"].strip():
        errors.append("wisdom_required")
    errors.extend(_contains_forbidden_text({"subject": event.get("subject"), "wisdom": event.get("wisdom"), "why_it_matters": event.get("why_it_matters"), "applicability": event.get("applicability")}))
    return sorted(set(errors))


class IntelligentHubKernel:
    """Minimal, executable implementation of the three Intelligent Hub contracts."""

    def __init__(self, authenticator: ReferenceAuthenticator | None = None) -> None:
        self.authenticator = authenticator or ReferenceAuthenticator()
        self.connections: dict[str, Connection] = {}
        self.contributions: dict[str, dict[str, Any]] = {}
        self.events: dict[str, dict[str, Any]] = {}
        self.acknowledgements: set[tuple[str, str]] = set()

    def connect(
        self,
        *,
        owner_subject: str,
        provider: str,
        installation_id: str,
        resource_id: str,
        capabilities: Iterable[str],
    ) -> Connection:
        if not owner_subject or not provider or not installation_id or not resource_id:
            raise ValueError("connection identity/resource fields are required")
        allowed = {
            "read_superbrain_metadata",
            "read_authorized_wisdom_scope",
            "submit_wisdom_candidate",
            "receive_collective_updates",
            "event_acknowledgement",
        }
        granted = set(capabilities)
        unknown = granted - allowed
        if unknown:
            raise ValueError(f"unsupported capabilities: {sorted(unknown)}")
        connection_id = _stable_id("conn", [provider, installation_id, resource_id, owner_subject])
        now = _now()
        connection = Connection(
            connection_id=connection_id,
            owner_subject=owner_subject,
            provider=provider,
            installation_id=installation_id,
            resource_id=resource_id,
            capabilities=granted,
            status=ConnectionStatus.CONNECTED,
            created_at=now,
            updated_at=now,
        )
        self.connections[connection_id] = connection
        return connection

    def authorize(
        self,
        connection_id: str,
        context: AuthenticatedContext,
        token: str,
    ) -> bool:
        connection = self.connections.get(connection_id)
        if not connection or connection.status == ConnectionStatus.REVOKED:
            return False
        if not self.authenticator.verify(token, context):
            return False
        return (
            context.subject == connection.owner_subject
            and context.provider == connection.provider
            and context.installation_id == connection.installation_id
            and context.resource_id == connection.resource_id
        )

    def grant_consent(self, connection_id: str, scope: Iterable[str]) -> Connection:
        connection = self._connection(connection_id)
        requested = set(scope)
        if "wisdom_contribution" in requested:
            connection.consent_scope.add("wisdom_contribution")
        connection.updated_at = _now()
        return connection

    def revoke(self, connection_id: str, *, contribution_only: bool = False) -> Connection:
        connection = self._connection(connection_id)
        if contribution_only:
            connection.consent_scope.discard("wisdom_contribution")
        else:
            connection.status = ConnectionStatus.REVOKED
            connection.revoked_at = _now()
        connection.updated_at = _now()
        return connection

    def submit_wisdom(
        self,
        *,
        connection_id: str,
        context: AuthenticatedContext,
        token: str,
        contribution: dict[str, Any],
        human_approved: bool,
    ) -> ContributionResult:
        connection = self._connection(connection_id)
        if "submit_wisdom_candidate" not in connection.capabilities:
            return self._reject(contribution, "capability_not_granted")
        if "wisdom_contribution" not in connection.consent_scope:
            return self._reject(contribution, "contribution_consent_not_granted")
        if not self.authorize(connection_id, context, token):
            return self._reject(contribution, "authentication_or_binding_failed")
        if not human_approved:
            return self._reject(contribution, "human_review_required_before_publication")

        candidate = self._extract_value(contribution)
        privacy_reasons = _contains_forbidden_text(candidate)
        if privacy_reasons:
            return self._quarantine(candidate, *privacy_reasons)
        if float(candidate.get("confidence", -1)) < 0 or float(candidate.get("confidence", 0)) > 1:
            return self._reject(candidate, "confidence_out_of_range")
        if not candidate.get("wisdom") or not candidate.get("subject"):
            return self._reject(candidate, "subject_and_wisdom_required")

        fingerprint = _stable_id("fp", [candidate.get("subject"), candidate.get("wisdom"), candidate.get("why_it_matters")])
        for stored in self.contributions.values():
            if stored.get("fingerprint") == fingerprint:
                cid = str(stored["contribution_id"])
                return ContributionResult(GateStatus.DUPLICATE, cid, None, ("duplicate_wisdom",))

        contribution_id = _stable_id("contrib", [connection_id, fingerprint])
        event = self._build_event(candidate, contribution_id)
        errors = validate_collective_event(event)
        if errors:
            return self._quarantine(candidate, *errors)

        self.contributions[contribution_id] = {
            "contribution_id": contribution_id,
            "connection_id": connection_id,
            "owner_subject": connection.owner_subject,
            "fingerprint": fingerprint,
            "status": GateStatus.ACCEPTED.value,
        }
        self.events[event["event_id"]] = event
        return ContributionResult(GateStatus.ACCEPTED, contribution_id, event, ())

    def intelligence_feed(self, *, limit: int = 50, event_type: str | None = None) -> list[dict[str, Any]]:
        rows = [e for e in self.events.values() if e["status"] in {"published", "validated"}]
        if event_type:
            rows = [e for e in rows if e["event_type"] == event_type]
        return sorted(rows, key=lambda e: e["effective_at"], reverse=True)[:limit]

    def retrieve_event(self, event_id: str) -> dict[str, Any] | None:
        event = self.events.get(event_id)
        if event is None or event["status"] not in {"published", "validated"}:
            return None
        return json.loads(json.dumps(event))

    def acknowledge(self, connection_id: str, event_id: str) -> bool:
        connection = self._connection(connection_id)
        if "event_acknowledgement" not in connection.capabilities:
            return False
        if connection.status == ConnectionStatus.REVOKED or event_id not in self.events:
            return False
        self.acknowledgements.add((connection_id, event_id))
        return True

    def _connection(self, connection_id: str) -> Connection:
        if connection_id not in self.connections:
            raise KeyError(f"unknown connection: {connection_id}")
        return self.connections[connection_id]

    @staticmethod
    def _extract_value(contribution: dict[str, Any]) -> dict[str, Any]:
        """Normalize only the explicit wisdom fields; raw source is forbidden."""
        forbidden = {"raw_source", "conversation", "transcript", "private_memory", "repository_contents", "notes"}
        leaked = forbidden.intersection(contribution)
        if leaked:
            raise ValueError(f"raw/private source fields are not accepted: {sorted(leaked)}")
        return {
            "subject": str(contribution.get("subject", "")).strip(),
            "wisdom": str(contribution.get("wisdom", "")).strip(),
            "why_it_matters": str(contribution.get("why_it_matters", "")).strip(),
            "applicability": list(contribution.get("applicability", [])),
            "evidence": list(contribution.get("evidence", [])),
            "confidence": float(contribution.get("confidence", 0)),
        }

    @staticmethod
    def _build_event(candidate: dict[str, Any], contribution_id: str) -> dict[str, Any]:
        now = _now()
        event_id = _stable_id("cie", [candidate["subject"], candidate["wisdom"], candidate["why_it_matters"]])
        return {
            "event_id": event_id,
            "schema_version": CIE_SCHEMA_VERSION,
            "event_type": "insight",
            "created_at": now,
            "effective_at": now,
            "subject": candidate["subject"],
            "wisdom": candidate["wisdom"],
            "why_it_matters": candidate["why_it_matters"],
            "applicability": candidate["applicability"],
            "evidence": candidate["evidence"],
            "confidence": candidate["confidence"],
            "provenance": {
                "source_kind": "authorized_wisdom_contribution",
                "source_event_count": 0,
                "validation_state": "validated",
                "contribution_reference": contribution_id,
            },
            "privacy": {
                "identity_included": False,
                "raw_source_included": False,
                "privacy_review": "passed",
            },
            "relationships": [],
            "supersedes": [],
            "status": "published",
            "verification_receipt": {
                "verified": True,
                "verified_at": now,
                "checks": [
                    "authenticated_connection",
                    "explicit_contribution_consent",
                    "human_review",
                    "privacy_gate",
                    "quality_gate",
                    "schema_validation",
                    "identity_excluded_from_collective_object",
                    "raw_source_excluded_from_collective_object",
                ],
            },
        }

    @staticmethod
    def _reject(contribution: dict[str, Any], reason: str) -> ContributionResult:
        cid = _stable_id("contrib", contribution)
        return ContributionResult(GateStatus.REJECTED, cid, None, (reason,))

    @staticmethod
    def _quarantine(contribution: dict[str, Any], *reasons: str) -> ContributionResult:
        cid = _stable_id("contrib", contribution)
        return ContributionResult(GateStatus.QUARANTINED, cid, None, tuple(sorted(set(reasons))))


__all__ = [
    "AuthenticatedContext",
    "Connection",
    "ConnectionStatus",
    "ContributionResult",
    "GateStatus",
    "IntelligentHubKernel",
    "ReferenceAuthenticator",
    "validate_collective_event",
]
