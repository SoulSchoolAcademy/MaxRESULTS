#!/usr/bin/env python3
"""Canonical Smart Notes v3 runtime.

Event-centric, chronological, semantic, provenance-aware memory plus CIS
report synthesis. This runtime treats Note Events as the system of record.
"""
from __future__ import annotations
import argparse, json, re
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVENTS = ROOT / '.naya' / 'memory' / 'events'
INDEX = EVENTS / 'INDEX.json'
EVENT_RE = re.compile(r'^SE-[0-9]{8}-[0-9]{6}-[a-z0-9-]+$')


def parse_time(value):
    if value is None: return None
    if value.endswith('Z'): value = value[:-1] + '+00:00'
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None: raise ValueError('timezone required')
    return dt


def event_files():
    return sorted(p for p in EVENTS.glob('*/*/*/*/SE-*.json') if p.name != 'INDEX.json')


def load_events():
    out=[]
    for p in event_files():
        data=json.loads(p.read_text(encoding='utf-8'))
        out.append((p,data))
    return out


def validate():
    errors=[]; ids=set(); paths=set()
    for p,e in load_events():
        eid=e.get('event_id')
        if not EVENT_RE.match(eid or ''): errors.append(f'{p}: invalid event_id')
        if eid in ids: errors.append(f'duplicate event_id: {eid}')
        ids.add(eid); paths.add(str(p.relative_to(EVENTS)))
        for k in ('created_at',):
            try: parse_time(e[k])
            except Exception as exc: errors.append(f'{p}: invalid {k}: {exc}')
        if e.get('effective_at') is not None:
            try: parse_time(e['effective_at'])
            except Exception as exc: errors.append(f'{p}: invalid effective_at: {exc}')
        if not e.get('representations'): errors.append(f'{p}: missing representations')
        if not e.get('source'): errors.append(f'{p}: missing source')
        if e.get('verification',{}).get('status') == 'VERIFIED' and not e.get('verification',{}).get('canonical_url'):
            errors.append(f'{p}: verified event missing canonical_url')
        for rel in e.get('relationships',{}).get('related',[]):
            if rel not in ids:
                # Validate later after all IDs are known.
                pass
    for _,e in load_events():
        for rel in e.get('relationships',{}).get('related',[]):
            if rel not in ids: errors.append(f"{e['event_id']}: unresolved relationship {rel}")
    idx=json.loads(INDEX.read_text(encoding='utf-8'))
    indexed={x['event_id'] for x in idx.get('events',[])}
    if indexed != ids: errors.append(f'INDEX mismatch: index={len(indexed)} events={len(ids)}')
    return errors


def retrieve(query, limit=10):
    q=set(re.findall(r'[a-z0-9]+',query.lower())); results=[]
    for p,e in load_events():
        r=e.get('representations',{}); text=' '.join([
            e.get('subject',''),e.get('project',''),e.get('event_type',''),
            ' '.join(e.get('tags',[])),
            r.get('naya',{}).get('summary',''), r.get('human',{}).get('summary',''),
            ' '.join(r.get('naya',{}).get('aliases',[]))
        ])
        score=len(q & set(re.findall(r'[a-z0-9]+',text.lower())))
        if e.get('verification',{}).get('status') == 'VERIFIED': score += 2
        if score: results.append((score,e))
    results.sort(key=lambda x:(-x[0],x[1].get('effective_at') or x[1].get('created_at'),x[1]['event_id']))
    return results[:limit]


def daily(day):
    start=datetime.fromisoformat(day+'T00:00:00+00:00'); end=start+timedelta(days=1); selected=[]
    for _,e in load_events():
        t=e.get('effective_at') or e.get('created_at'); dt=parse_time(t).astimezone(start.tzinfo)
        if start <= dt < end: selected.append(e)
    learning=[]; wins=[]; changes=[]; nexts=[]
    for e in selected:
        learning += e.get('representations',{}).get('naya',{}).get('lessons',[])
        if e.get('event_type') in {'milestone','success'}: wins.append(e['event_id'])
        nexts += e.get('representations',{}).get('naya',{}).get('next_best_actions',[])
    return {'report_type':'DAILY_INTELLIGENCE_REPORT','period':day,'event_count':len(selected),'source_event_ids':[e['event_id'] for e in selected],'learning':learning,'wins':wins,'next_best_actions':nexts,'verification_required':True,'feed_receipt_required_when_supported':True}


def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='cmd',required=True)
    sub.add_parser('validate'); r=sub.add_parser('retrieve'); r.add_argument('query'); r.add_argument('--limit',type=int,default=10)
    d=sub.add_parser('daily-report'); d.add_argument('day')
    args=ap.parse_args()
    if args.cmd=='validate':
        errors=validate(); print('PASS — Smart Notes v3 is structurally valid' if not errors else 'FAIL\n'+'\n'.join('- '+x for x in errors)); return 0 if not errors else 1
    if args.cmd=='retrieve':
        for score,e in retrieve(args.query,args.limit): print(f"{score:3} {e['event_id']} | {e['subject']} | {e['event_type']}")
        return 0
    print(json.dumps(daily(args.day),indent=2,ensure_ascii=False)); return 0

if __name__=='__main__': raise SystemExit(main())
