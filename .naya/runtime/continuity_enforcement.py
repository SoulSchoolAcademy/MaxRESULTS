#!/usr/bin/env python3
"""Machine-enforceable execution continuity for Naya Power.

The canonical source remains Note Events. This runtime adds a narrow enforcement
layer around meaningful executions without changing the existing event schema.
It is deliberately conservative: only events at/after the policy effective
boundary are required to satisfy the continuity contract.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MEMORY = ROOT / ".naya" / "memory"
EVENTS = MEMORY / "events"
POLICY = MEMORY / "CONTINUITY-ENFORCEMENT-POLICY.json"
REPORT = MEMORY / "CONTINUITY-VALIDATION-REPORT.json"
EVENT_RE = re.compile(r"^SE-[0-9]{8}-[0-9]{6}-[a-z0-9-]+$")


def parse_time(value: str) -> datetime:
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        raise ValueError("timestamp must include timezone")
    return dt.astimezone(timezone.utc)


def load_policy() -> dict:
    return json.loads(POLICY.read_text(encoding="utf-8"))


def event_files():
    return sorted(EVENTS.rglob("SE-*.json")) if EVENTS.exists() else []


def load_event(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except Exception as exc:
        return None, str(exc)


def is_meaningful_execution(event: dict, policy: dict) -> bool:
    """Classify only explicit execution-like events; ordinary notes are untouched."""
    boundary = parse_time(policy["effective_at"])
    effective = parse_time(event.get("effective_at", event.get("created_at", "")))
    if effective < boundary:
        return False
    if event.get("continuity_required") is True:
        return True
    event_type = str(event.get("event_type", event.get("type", ""))).lower()
    if event_type in set(policy.get("meaningful_event_types", [])):
        return True
    event_id = str(event.get("event_id", "")).lower()
    if any(token in event_id for token in policy.get("event_id_markers", [])):
        return True
    tags = {str(x).lower() for x in (event.get("tags") or [])}
    return bool(tags.intersection({str(x).lower() for x in policy.get("meaningful_tags", [])}))


def has_handoff(event: dict, policy: dict) -> bool:
    continuity = event.get("continuity", {}) or {}
    for key in ("handoff_url", "handoff_path", "ai_to_ai_handoff"):
        if continuity.get(key):
            return True
    verification = event.get("verification", {}) or {}
    if verification.get("handoff_url") or verification.get("handoff_path"):
        return True
    event_id = event.get("event_id", "")
    for root in policy.get("handoff_roots", [".naya/handoffs"]):
        base = ROOT / root
        if base.exists() and any(event_id in p.name for p in base.rglob("*")):
            return True
    return False


def check_event(event: dict, path: Path, policy: dict) -> list[str]:
    errors = []
    eid = event.get("event_id", "<missing>")
    reps = event.get("representations") or {}
    naya = reps.get("naya") if isinstance(reps, dict) else None
    human = (reps.get("shawn") or reps.get("human")) if isinstance(reps, dict) else None
    if not naya or not human:
        errors.append(f"{eid}: missing paired Naya + Shawn/Human representations")
    verification = event.get("verification") or {}
    if verification.get("status") != "VERIFIED":
        errors.append(f"{eid}: continuity requires verification.status=VERIFIED")
    receipt = event.get("receipt") or {}
    receipt_id = receipt.get("receipt_id") or verification.get("receipt") or verification.get("receipt_url")
    if not receipt_id:
        errors.append(f"{eid}: continuity requires a durable receipt reference")
    delivery = event.get("delivery") or {}
    if not delivery.get("state") and not verification.get("feed_status"):
        errors.append(f"{eid}: continuity requires explicit delivery state")
    if not has_handoff(event, policy):
        errors.append(f"{eid}: continuity requires an AI-to-AI handoff reference/artifact")
    lessons = []
    next_actions = []
    for rep in (naya, human):
        if isinstance(rep, dict):
            lessons += rep.get("lessons", []) or rep.get("learning", []) or rep.get("what_we_learned", []) or []
            next_actions += rep.get("next_best_actions", []) or []
    if not lessons and not (event.get("continuity") or {}).get("learning_status"):
        errors.append(f"{eid}: continuity requires learning or explicit learning_status")
    if not next_actions and not (event.get("continuity") or {}).get("next_action_status"):
        errors.append(f"{eid}: continuity requires a next-action record")
    if not EVENT_RE.match(str(eid)):
        errors.append(f"{path}: invalid event_id")
    return errors


def validate() -> tuple[int, dict]:
    policy = load_policy()
    checked = 0
    meaningful = 0
    errors = []
    for path in event_files():
        event, parse_error = load_event(path)
        if parse_error:
            errors.append(f"{path}: JSON parse error: {parse_error}")
            continue
        if not is_meaningful_execution(event, policy):
            continue
        checked += 1
        meaningful += 1
        errors.extend(check_event(event, path, policy))
    report = {
        "schema_version": 1,
        "status": "GREEN" if not errors else "RED",
        "policy_effective_at": policy["effective_at"],
        "meaningful_execution_events_checked": checked,
        "error_count": len(errors),
        "errors": errors,
        "checks": [
            "paired_naya_human_representation",
            "verification",
            "durable_receipt",
            "delivery_state",
            "ai_to_ai_handoff",
            "learning_or_explicit_non_applicability",
            "next_action",
        ],
    }
    REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return (0 if not errors else 1), report


def self_test() -> int:
    policy = load_policy()
    good = {
        "event_id": "SE-20260825-999999-continuity-positive-test",
        "effective_at": policy["effective_at"],
        "event_type": "execution-milestone",
        "representations": {
            "naya": {"id": "SN-20260825-999999-test-naya", "lessons": ["test lesson"], "next_best_actions": ["test next"]},
            "shawn": {"id": "SN-20260825-999999-test-shawn", "lessons": ["human lesson"], "next_best_actions": ["human next"]},
        },
        "verification": {"status": "VERIFIED", "receipt": "RCPT-test"},
        "receipt": {"receipt_id": "RCPT-test"},
        "delivery": {"state": "VERIFIED"},
        "continuity": {"handoff_url": "https://example.invalid/handoff", "learning_status": "LEARNED"},
    }
    if check_event(good, Path("positive-fixture.json"), policy):
        print("FAIL — positive continuity fixture rejected")
        return 1
    bad = json.loads(json.dumps(good))
    del bad["receipt"]
    bad["verification"].pop("receipt", None)
    bad["continuity"].pop("handoff_url", None)
    bad["continuity"].pop("learning_status", None)
    errors = check_event(bad, Path("negative-fixture.json"), policy)
    required_fragments = ["durable receipt", "AI-to-AI handoff", "learning"]
    if not all(any(fragment in error for error in errors) for fragment in required_fragments):
        print("FAIL — negative continuity fixture did not expose all deliberate failures")
        return 1
    print("PASS — continuity positive and deliberate-failure tests GREEN")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    sub.add_parser("self-test")
    args = parser.parse_args()
    if args.command == "self-test":
        return self_test()
    code, report = validate()
    print("PASS — execution continuity validation is GREEN" if code == 0 else "FAIL — execution continuity validation is RED")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return code


if __name__ == "__main__":
    sys.exit(main())
