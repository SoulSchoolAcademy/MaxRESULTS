#!/usr/bin/env python3
"""Canonical, idempotent Note Event creation primitives.

The chronological event store remains authoritative. This module adds a safe
write boundary without changing historical events. Replays resolve to the
existing event; conflicting payloads are rejected for explicit review.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path
from typing import Any

EVENT_RE = re.compile(r"^SE-[0-9]{8}-[0-9]{6}-[a-z0-9-]+$")


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def content_fingerprint(event: dict[str, Any]) -> str:
    """Stable content identity excluding mutable receipt/delivery fields."""
    excluded = {"event_id", "created_at", "receipt", "delivery", "verification"}
    payload = {k: v for k, v in event.items() if k not in excluded}
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


def idempotency_key(event: dict[str, Any]) -> str:
    """Prefer explicit source identity; otherwise use stable content identity."""
    source = event.get("source") or {}
    if isinstance(source, dict):
        source_id = source.get("event_id") or source.get("id")
    else:
        source_id = None
    if source_id:
        return f"source:{source_id}"
    if event.get("idempotency_key"):
        return str(event["idempotency_key"])
    return f"content:{content_fingerprint(event)}"


def _candidate_path(events_root: Path, event_id: str, effective_at: str) -> Path:
    if not EVENT_RE.match(event_id):
        raise ValueError(f"invalid event_id: {event_id}")
    value = effective_at.replace("Z", "+00:00")
    from datetime import datetime
    dt = datetime.fromisoformat(value)
    return events_root / f"{dt:%Y/%m/%d/%H}/{event_id}.json"


def create_or_replay(event: dict[str, Any], events_root: Path, index_path: Path) -> dict[str, Any]:
    """Atomically create an event or return its existing canonical identity.

    This function is intentionally filesystem-rooted so tests can use a clean
    temporary store. It never overwrites an existing event.
    """
    event = json.loads(canonical_json(event))
    event_id = str(event.get("event_id", ""))
    path = _candidate_path(events_root, event_id, str(event["effective_at"]))
    key = idempotency_key(event)
    fingerprint = content_fingerprint(event)
    path.parent.mkdir(parents=True, exist_ok=True)
    index_path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists():
        existing = json.loads(path.read_text(encoding="utf-8"))
        if content_fingerprint(existing) == fingerprint:
            return {"status": "REPLAY", "event_id": existing["event_id"], "path": str(path), "idempotency_key": key, "fingerprint": fingerprint}
        return {"status": "CONFLICT", "event_id": existing.get("event_id"), "path": str(path), "idempotency_key": key, "fingerprint": fingerprint}

    # O_EXCL prevents two writers from silently overwriting one another.
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(event, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
    except Exception:
        try: path.unlink()
        except OSError: pass
        raise

    rows = []
    if index_path.exists():
        try: rows = json.loads(index_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError: rows = []
    if not any(isinstance(row, dict) and row.get("event_id") == event_id for row in rows):
        rows.append({"event_id": event_id, "path": str(path), "idempotency_key": key, "fingerprint": fingerprint})
    rows.sort(key=lambda row: (row.get("event_id", ""), row.get("path", "")))
    index_path.write_text(json.dumps({"version": 1, "events": rows}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {"status": "CREATED", "event_id": event_id, "path": str(path), "idempotency_key": key, "fingerprint": fingerprint}
