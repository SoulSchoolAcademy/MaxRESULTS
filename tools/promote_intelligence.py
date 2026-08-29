#!/usr/bin/env python3
"""Validate, classify, and promote canonical Naya intelligence events.

Deterministic destinations are automated. Governance-sensitive destinations
remain proposals requiring their normal authority and verification boundary.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
EVENT_DIR = ROOT / "MASTER-NOTES/INTELLIGENCE-EVENTS"
RECEIPT_DIR = ROOT / "MASTER-NOTES/INTELLIGENCE-PROMOTIONS"
NAYA_DIR = ROOT / "MASTER-NOTES/NAYA-NOTES"
SHAWN_DIR = ROOT / "MASTER-NOTES/SHAWN-NOTES"
REQUIRED = {"event_id", "timestamp", "project", "lesson", "source", "evidence_state", "promotion_status"}
HIGH_AUTHORITY = {"LAW", "GUARDRAIL", "MACHINE_CONTRACT", "TEST", "MISSION_STATE"}

def load_events():
    return [(p, json.loads(p.read_text(encoding="utf-8"))) for p in sorted(EVENT_DIR.glob("*.json"))]

def classify(event):
    explicit = [x for x in event.get("candidate_homes", []) if isinstance(x, str)]
    if explicit:
        homes = list(dict.fromkeys(explicit))
    else:
        text = " ".join(str(event.get(k, "")) for k in ("lesson", "what_happened", "root_cause", "recommendation")).lower()
        homes = []
        if any(x in text for x in ("every naya", "must always", "governance", "universal")): homes.append("LAW")
        if any(x in text for x in ("repeat", "regression", "prevent", "guardrail")): homes.append("GUARDRAIL")
        if any(x in text for x in ("test", "assert", "machine", "automate")): homes.append("TEST")
        if not homes: homes.append("NAYA_NOTE")
    return homes, ("PROMOTION_PROPOSAL_REQUIRES_AUTHORITY" if any(h in HIGH_AUTHORITY for h in homes) else "AUTO_CLASSIFIED")

def write_note(event, human=False):
    target = SHAWN_DIR if human else NAYA_DIR
    target.mkdir(parents=True, exist_ok=True)
    kind = "SHAWN NOTE / HUMAN RECEIPT" if human else "NAYA NOTE / AI INTELLIGENCE"
    filename = f"{event['event_id']}.md"
    content = f"# 🔱 {kind}\n\n**Event:** {event['event_id']}\n**Timestamp:** {event['timestamp']}\n**Project:** {event['project']}\n\n## WHAT HAPPENED\n{event.get('what_happened','')}\n\n## WHAT WE LEARNED\n{event['lesson']}\n\n## VALUE\n{event.get('value','')}\n\n## WHAT CHANGED\n{event.get('actual_outcome','')}\n\n## EVIDENCE\n" + "\n".join(f"- `{x}`" for x in event.get('evidence', [])) + f"\n\n## NEXT ACTION\n{event.get('next_action','')}\n\n## SUCCESSOR / HUMAN GUIDANCE\n{event.get('successor_instruction','')}\n\n## PROVENANCE\nSource event: `{event['event_id']}`\n"
    path = target / filename
    if not path.exists(): path.write_text(content, encoding="utf-8")
    return str(path.relative_to(ROOT))

def main():
    errors, receipts = [], []
    for path, event in load_events():
        missing = sorted(REQUIRED - set(event))
        if missing:
            errors.append(f"{path}: missing required fields: {', '.join(missing)}")
            continue
        homes, decision = classify(event)
        promoted = list(event.get("promoted_artifacts", []))
        if "NAYA_NOTE" in homes:
            promoted.append(write_note(event, human=False))
        if "HUMAN_SMART_NOTE" in homes:
            promoted.append(write_note(event, human=True))
        receipts.append({"event_id": event["event_id"], "source_event": str(path.relative_to(ROOT)), "candidate_homes": homes, "decision": decision, "evidence_state": event["evidence_state"], "promotion_status": event["promotion_status"], "promoted_artifacts": list(dict.fromkeys(promoted)), "rule": "HIGH_AUTHORITY_DESTINATIONS_REQUIRE_AUTHORITY_AND_VERIFICATION; DETERMINISTIC_NOTE_DESTINATIONS_MAY_BE_AUTO-PROMOTED"})
    if errors:
        for error in errors: print(error, file=sys.stderr)
        return 1
    RECEIPT_DIR.mkdir(parents=True, exist_ok=True)
    (RECEIPT_DIR / "LATEST-PROMOTION-RECEIPT.json").write_text(json.dumps({"receipts": receipts}, indent=2) + "\n", encoding="utf-8")
    print(f"Validated and promoted {len(receipts)} intelligence event(s).")
    return 0
if __name__ == "__main__": raise SystemExit(main())
