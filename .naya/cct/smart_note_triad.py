#!/usr/bin/env python3
"""Canonical Smart Note Triad primitives for CCT/NayaNet MVP.

A Smart Note is one learning event with three synchronized projections:
Human, Naya, and Machine. The three projections share one identity and are
never silently overwritten. This module intentionally uses only the Python
standard library so the deterministic contract can be proven locally.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
from typing import Any

SCHEMA_VERSION = "SMART-NOTE-TRIAD-v0.1"
REQUIRED_LAYERS = ("human_note", "naya_note", "machine_note")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def content_hash(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def _layer(status: str, content: Any = None, unavailable_reason: str | None = None) -> dict[str, Any]:
    if status == "PRESENT":
        if content is None:
            raise ValueError("PRESENT layer requires content")
        if unavailable_reason is not None:
            raise ValueError("PRESENT layer cannot contain unavailable_reason")
        return {"status": status, "content": content}
    if status == "UNAVAILABLE":
        if not unavailable_reason or not unavailable_reason.strip():
            raise ValueError("UNAVAILABLE layer requires a machine-readable reason")
        if content is not None:
            raise ValueError("UNAVAILABLE layer cannot contain content")
        return {"status": status, "unavailable_reason": unavailable_reason.strip()}
    raise ValueError("layer status must be PRESENT or UNAVAILABLE")


def create_smart_note(
    smart_note_id: str,
    human_content: Any,
    naya_content: Any,
    machine_content: dict[str, Any],
    *,
    provenance: dict[str, Any],
    evidence: dict[str, Any],
    permissions: dict[str, Any],
    created_at: str | None = None,
) -> dict[str, Any]:
    if not smart_note_id.strip():
        raise ValueError("smart_note_id is required")
    event = {
        "smart_note_id": smart_note_id,
        "schema_version": SCHEMA_VERSION,
        "created_at": created_at or utc_now(),
        "human_note": _layer("PRESENT", human_content),
        "naya_note": _layer("PRESENT", naya_content),
        "machine_note": {
            "status": "PRESENT",
            "content": machine_content,
            "provenance": provenance,
            "evidence": evidence,
            "permissions": permissions,
        },
    }
    validate_smart_note(event)
    return event


def validate_smart_note(note: dict[str, Any]) -> None:
    if not isinstance(note, dict):
        raise ValueError("smart note must be an object")
    for key in ("smart_note_id", "schema_version", "created_at", *REQUIRED_LAYERS):
        if key not in note:
            raise ValueError(f"missing required field: {key}")
    if note["schema_version"] != SCHEMA_VERSION:
        raise ValueError("unsupported Smart Note schema version")
    for name in REQUIRED_LAYERS:
        layer = note[name]
        if not isinstance(layer, dict):
            raise ValueError(f"{name} must be an object")
        status = layer.get("status")
        if status == "PRESENT":
            if "content" not in layer:
                raise ValueError(f"{name}: PRESENT requires content")
            if "unavailable_reason" in layer:
                raise ValueError(f"{name}: PRESENT cannot have unavailable_reason")
        elif status == "UNAVAILABLE":
            reason = layer.get("unavailable_reason")
            if not isinstance(reason, str) or not reason.strip():
                raise ValueError(f"{name}: UNAVAILABLE requires unavailable_reason")
            if "content" in layer:
                raise ValueError(f"{name}: UNAVAILABLE cannot have content")
        else:
            raise ValueError(f"{name}: invalid status")
    machine = note["machine_note"]
    if machine["status"] == "PRESENT":
        for key in ("content", "provenance", "evidence", "permissions"):
            if key not in machine:
                raise ValueError(f"machine_note missing {key}")


def immutable_fingerprint(note: dict[str, Any]) -> str:
    validate_smart_note(note)
    return content_hash(note)


def assert_same_identity(*notes: dict[str, Any]) -> None:
    ids = {n.get("smart_note_id") for n in notes}
    if len(ids) != 1:
        raise ValueError("Smart Note projections must share one smart_note_id")


def independent_consume(note: dict[str, Any]) -> dict[str, Any]:
    """Return the portable triad only; no conversation/runtime context is consulted."""
    validate_smart_note(note)
    portable = json.loads(canonical_json(note))
    validate_smart_note(portable)
    return portable


if __name__ == "__main__":
    demo = create_smart_note(
        "SN-DEMO-001",
        "The local proof should precede expensive remote CI.",
        "Capture the resource-efficiency lesson as reusable intelligence.",
        {"event_type": "learning", "mpa": "maximize verified value per action"},
        provenance={"source": "NayaPOWER-local-proof"},
        evidence={"method": "deterministic-contract-test"},
        permissions={"visibility": "PRIVATE"},
    )
    print(json.dumps({"valid": True, "fingerprint": immutable_fingerprint(demo), "note": demo}, indent=2))
