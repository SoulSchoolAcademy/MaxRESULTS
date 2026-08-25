#!/usr/bin/env python3
"""Build the deterministic external-delivery outbox from canonical events.

The outbox is derived, so a failed external integration can never destroy or
hide the canonical Smart Note. Each pending receipt is idempotent by event_id.
"""
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[2]
MEMORY=ROOT/'.naya/memory'; EVENTS=MEMORY/'events'; OUTBOX=MEMORY/'OUTBOX.jsonl'

lines=[]
for p in sorted(EVENTS.rglob('SE-*.json')):
    e=json.loads(p.read_text(encoding='utf-8')); v=e.get('verification',{})
    if v.get('status')=='VERIFIED' and v.get('feed_status')=='PENDING_INTEGRATION':
        lines.append({'event_id':e['event_id'],'operation':'PUBLISH_VERIFICATION_RECEIPT','status':'PENDING','canonical_url':v.get('canonical_url'),'created_at':datetime.now(timezone.utc).isoformat()})
OUTBOX.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in lines),encoding='utf-8')
print(f'OUTBOX {len(lines)} pending delivery records')
