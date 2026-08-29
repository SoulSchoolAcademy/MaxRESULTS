#!/usr/bin/env python3
"""Fail-closed regression tests for NayaPOWER deployment governance.

These tests prove repository-side authorization policy. They do not claim that
an external Vercel webhook was observed; that requires provider evidence.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
POLICY = ROOT / ".naya" / "control-plane" / "DEPLOYMENT-GOVERNANCE.json"
AUTH = ROOT / ".naya" / "control-plane" / "RELEASE-AUTHORIZATION.json"
VERCEL = ROOT / "vercel.json"
WORKFLOWS = ROOT / ".github" / "workflows"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def deployment_allowed(*, authorization: dict, commit_sha: str, target: str) -> bool:
    """Pure policy decision used by the regression cases."""
    return (
        authorization.get("status") == "AUTHORIZED"
        and authorization.get("commit_sha") == commit_sha
        and authorization.get("target_environment") == target
        and authorization.get("deployment_surface") == "vercel"
        and authorization.get("approval") == "EXPLICIT_APPROVAL_GRANTED"
        and authorization.get("verification", {}).get("status") == "PASS"
    )


def test_vercel_git_deployments_disabled():
    config = load(VERCEL)
    assert config["git"]["deploymentEnabled"] is False


def test_release_contract_is_fail_closed_template():
    auth = load(AUTH)
    assert auth["status"] == "TEMPLATE"
    assert not deployment_allowed(authorization=auth, commit_sha="abc", target="production")


def test_documentation_change_does_not_authorize_deployment():
    assert not deployment_allowed(authorization=load(AUTH), commit_sha="docs", target="preview")


def test_smart_note_change_does_not_authorize_deployment():
    assert not deployment_allowed(authorization=load(AUTH), commit_sha="smart-note", target="preview")


def test_naya_governance_change_does_not_authorize_deployment():
    assert not deployment_allowed(authorization=load(AUTH), commit_sha="governance", target="production")


def test_normal_commit_does_not_authorize_deployment():
    assert not deployment_allowed(authorization=load(AUTH), commit_sha="ordinary", target="production")


def test_authorized_release_is_permitted():
    auth = {
        "status": "AUTHORIZED",
        "commit_sha": "abc123",
        "target_environment": "production",
        "deployment_surface": "vercel",
        "approval": "EXPLICIT_APPROVAL_GRANTED",
        "verification": {"status": "PASS"},
    }
    assert deployment_allowed(authorization=auth, commit_sha="abc123", target="production")


def test_no_workflow_contains_unconditional_vercel_deploy_command():
    forbidden = ("vercel deploy", "npx vercel", "npm exec vercel", "deploy_to_vercel")
    offenders = []
    for path in WORKFLOWS.glob("*.yml"):
        text = path.read_text(encoding="utf-8").lower()
        if any(token in text for token in forbidden):
            offenders.append(str(path.relative_to(ROOT)))
    assert not offenders, f"Vercel bypass candidates found: {offenders}"


def test_policy_preserves_connection_but_denies_default_deployment():
    policy = load(POLICY)
    assert policy["default"]["deployment"] == "DENY"
    assert policy["default"]["preview_deployment"] == "DENY"
    assert policy["default"]["production_deployment"] == "DENY"


if __name__ == "__main__":
    tests = [value for name, value in globals().items() if name.startswith("test_")]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
    print(f"PASS {len(tests)} deployment-governance tests")
