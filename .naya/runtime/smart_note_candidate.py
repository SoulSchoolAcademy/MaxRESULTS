#!/usr/bin/env python3
"""Narrow boundary from valuable completed execution evidence to a Smart Note candidate.

This module does not store notes, write Note Events, promote authority, or run CSI.
It only filters and packages durable learning candidates with provenance.
"""
from __future__ import annotations
from typing import Any

ALLOWED_TYPES = {"insight", "lesson", "mistake", "breakthrough", "decision", "correction", "opportunity", "procedure", "goal", "win"}
REQUIRED_SOURCE = {"execution_id", "evidence_id", "commit_sha"}
REQUIRED_LEARNING = {"what_mattered", "what_was_learned", "future_action"}


def _text(v: Any) -> bool:
    return isinstance(v, str) and bool(v.strip())


def build_candidate(execution_evidence: dict[str, Any], learning: dict[str, Any], *, note_type: str) -> dict[str, Any]:
    """Create a candidate only when observed evidence has durable learning value."""
    if not isinstance(execution_evidence, dict):
        raise ValueError("execution evidence must be an object")
    missing_source = REQUIRED_SOURCE - set(execution_evidence)
    if missing_source:
        raise ValueError(f"missing evidence provenance: {sorted(missing_source)}")
    if not _text(execution_evidence.get("execution_id")) or not _text(execution_evidence.get("evidence_id")) or not _text(execution_evidence.get("commit_sha")):
        raise ValueError("execution_id, evidence_id, and commit_sha are required")
    if execution_evidence.get("schema") != "naya-power-evidence/v1":
        raise ValueError("non-canonical evidence rejected")
    if not isinstance(learning, dict):
        raise ValueError("learning must be an object")
    missing_learning = REQUIRED_LEARNING - set(learning)
    if missing_learning:
        raise ValueError(f"missing durable learning: {sorted(missing_learning)}")
    if any(not _text(learning.get(k)) for k in REQUIRED_LEARNING):
        raise ValueError("durable learning fields must be non-empty")
    if note_type not in ALLOWED_TYPES:
        raise ValueError("invalid Smart Note type")
    return {
        "kind": "smart-note-candidate/v1",
        "note_type": note_type,
        "what_mattered": learning["what_mattered"].strip(),
        "what_was_learned": learning["what_was_learned"].strip(),
        "future_action": learning["future_action"].strip(),
        "source": {
            "execution_id": execution_evidence["execution_id"],
            "evidence_id": execution_evidence["evidence_id"],
            "commit_sha": execution_evidence["commit_sha"],
        },
        "promotion_state": "CANDIDATE",
    }
