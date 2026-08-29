#!/usr/bin/env python3
"""Validate and classify canonical Naya intelligence events.

This runner deliberately separates deterministic automation from AI judgment:
- it validates required event fields;
- it derives candidate durable homes from explicit event signals;
- it rejects ambiguous/high-authority changes instead of guessing;
- it emits a promotion receipt that records what automation decided.

It does not silently rewrite laws, constitutional documents, Mission State, or
production configuration. Those destinations require their normal authority
and verification boundaries.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / ".naya/intelligence/intelligence-event.schema.json"
EVENT_DIR = ROOT / "MASTER-NOTES/INTELLIGENCE-EVENTS"
RECEIPT_DIR = ROOT / "MASTER-NOTES/INTELLIGENCE-PROMOTIONS"

REQUIRED = {
    "event_id",
    "timestamp",
    "project",
    "lesson",
    "source",
    "evidence_state",
    "promotion_status",
}

HIGH_AUTHORITY = {"LAW", "GUARDRAIL", "MACHINE_CONTRACT", "TEST", "MISSION_STATE"}


def load_events() -> list[tuple[Path, dict]]:
    events = []
    if not EVENT_DIR.exists():
        return events
    for path in sorted(EVENT_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        events.append((path, data))
    return events


def classify(event: dict) -> tuple[list[str], str]:
    explicit = [x for x in event.get("candidate_homes", []) if isinstance(x, str)]
    if explicit:
        homes = list(dict.fromkeys(explicit))
    else:
        text = " ".join(
            str(event.get(k, ""))
            for k in ("lesson", "what_happened", "root_cause", "recommendation")
        ).lower()
        homes = []
        if any(x in text for x in ("every naya", "must always", "governance", "universal")):
            homes.append("LAW")
        if any(x in text for x in ("repeat", "regression", "prevent", "guardrail")):
            homes.append("GUARDRAIL")
        if any(x in text for x in ("test", "assert", "machine", "automate")):
            homes.append("TEST")
        if not homes:
            homes.append("NAYA_NOTE")

    if any(h in HIGH_AUTHORITY for h in homes):
        status = "PROMOTION_PROPOSAL_REQUIRES_AUTHORITY"
    else:
        status = "AUTO_CLASSIFIED"
    return homes, status


def main() -> int:
    errors = []
    receipts = []
    for path, event in load_events():
        missing = sorted(REQUIRED - set(event))
        if missing:
            errors.append(f"{path}: missing required fields: {', '.join(missing)}")
            continue
        homes, decision = classify(event)
        receipt = {
            "event_id": event["event_id"],
            "source_event": str(path.relative_to(ROOT)),
            "candidate_homes": homes,
            "decision": decision,
            "evidence_state": event["evidence_state"],
            "promotion_status": event["promotion_status"],
            "promoted_artifacts": event.get("promoted_artifacts", []),
            "rule": "HIGH_AUTHORITY_DESTINATIONS_REQUIRE_AUTHORITY_AND_VERIFICATION; OTHER_DESTINATIONS_MAY_BE_AUTO_CLASSIFIED",
        }
        receipts.append(receipt)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    RECEIPT_DIR.mkdir(parents=True, exist_ok=True)
    out = RECEIPT_DIR / "LATEST-PROMOTION-RECEIPT.json"
    out.write_text(json.dumps({"receipts": receipts}, indent=2) + "\n", encoding="utf-8")
    print(f"Validated {len(receipts)} intelligence event(s). Receipt: {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
