#!/usr/bin/env python3
"""Fail-closed release authorization gate for NayaPOWER.

This module decides whether a specific Vercel deployment may proceed. It does
not deploy anything itself. A deployment consumer must provide the exact
commit SHA and an explicit, complete authorization record.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
POLICY_PATH = ROOT / ".naya" / "control-plane" / "DEPLOYMENT-GOVERNANCE.json"
AUTH_PATH = ROOT / ".naya" / "control-plane" / "RELEASE-AUTHORIZATION.json"


@dataclass(frozen=True)
class Decision:
    allowed: bool
    reason: str


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def authorize(*, authorization: dict, commit_sha: str, target_environment: str) -> Decision:
    """Return ALLOW only when every release gate is explicitly satisfied."""
    if not isinstance(commit_sha, str) or not commit_sha:
        return Decision(False, "exact commit SHA is required")
    if not isinstance(target_environment, str) or target_environment not in {"preview", "production"}:
        return Decision(False, "target environment must be preview or production")
    if authorization.get("status") != "AUTHORIZED":
        return Decision(False, "release authorization is not AUTHORIZED")
    if authorization.get("repository") != "SoulSchoolAcademy/NayaPOWER":
        return Decision(False, "repository binding mismatch")
    if authorization.get("commit_sha") != commit_sha:
        return Decision(False, "exact commit SHA binding mismatch")
    if authorization.get("target_environment") != target_environment:
        return Decision(False, "target environment mismatch")
    if authorization.get("deployment_surface") != "vercel":
        return Decision(False, "deployment surface is not Vercel")
    if authorization.get("approval") != "EXPLICIT_APPROVAL_GRANTED":
        return Decision(False, "explicit approval is missing")
    verification = authorization.get("verification")
    if not isinstance(verification, dict) or verification.get("status") != "PASS":
        return Decision(False, "verification status is not PASS")
    evidence = verification.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        return Decision(False, "verification evidence is required")
    for field in ("release_id", "release_reason", "authorized_by", "authorized_at"):
        value = authorization.get(field)
        if not isinstance(value, str) or not value or value.startswith("REQUIRED") or value.startswith("REPLACE_WITH"):
            return Decision(False, f"required authorization field missing: {field}")
    return Decision(True, "release authorization accepted for exact commit and target")


def current_template_decision(commit_sha: str, target_environment: str) -> Decision:
    return authorize(
        authorization=_load(AUTH_PATH),
        commit_sha=commit_sha,
        target_environment=target_environment,
    )


def policy() -> dict:
    return _load(POLICY_PATH)
