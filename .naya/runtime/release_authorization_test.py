#!/usr/bin/env python3
"""Dependency-free regression tests for the release authorization gate."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / ".naya" / "runtime" / "release_authorization.py"
spec = importlib.util.spec_from_file_location("release_authorization_test_module", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class ReleaseAuthorizationTests(unittest.TestCase):
    def test_checked_in_template_fails_closed(self):
        for environment in ("preview", "production"):
            decision = module.current_template_decision(
                "eec72c93bca6c4c9a625aa60327c452da2c63b4a", environment
            )
            self.assertFalse(decision.allowed, decision.reason)

    def test_wrong_commit_denied(self):
        authorization = {
            "status": "AUTHORIZED",
            "repository": "SoulSchoolAcademy/NayaPOWER",
            "commit_sha": "a" * 40,
            "target_environment": "preview",
            "deployment_surface": "vercel",
            "vercel_project_id": "prj_cHa9gwrtscCW8JuMDjcvw6DafaOK",
            "approval": "EXPLICIT_APPROVAL_GRANTED",
            "verification": {"status": "PASS", "evidence": ["test"]},
            "release_id": "TEST-001",
            "release_reason": "controlled regression test",
            "authorized_by": "test",
            "authorized_at": "2026-08-29T00:00:00Z",
        }
        decision = module.authorize(
            authorization=authorization,
            commit_sha="b" * 40,
            target_environment="preview",
        )
        self.assertFalse(decision.allowed)
        self.assertIn("SHA", decision.reason)

    def test_wrong_project_denied(self):
        authorization = {
            "status": "AUTHORIZED",
            "repository": "SoulSchoolAcademy/NayaPOWER",
            "commit_sha": "a" * 40,
            "target_environment": "preview",
            "deployment_surface": "vercel",
            "vercel_project_id": "wrong-project",
            "approval": "EXPLICIT_APPROVAL_GRANTED",
            "verification": {"status": "PASS", "evidence": ["test"]},
            "release_id": "TEST-002",
            "release_reason": "controlled regression test",
            "authorized_by": "test",
            "authorized_at": "2026-08-29T00:00:00Z",
        }
        decision = module.authorize(
            authorization=authorization,
            commit_sha="a" * 40,
            target_environment="preview",
        )
        self.assertFalse(decision.allowed)
        self.assertIn("project", decision.reason.lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
