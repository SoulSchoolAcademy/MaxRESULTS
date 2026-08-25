#!/usr/bin/env python3
"""Canonical Smart Notes v3 runtime.

Event-centric, chronological, semantic, provenance-aware memory plus CIS
report synthesis. Note Events are the system of record.
"""
from __future__ import annotations
import argparse, json, re
from datetime import datetime, timedelta, timezone
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
    return sorted(EVENTS.glob('*/*/*/*/SE-*.json'))


def load_events():
    return [(p, json.loads(p.read_text(encoding='utf-8'))) for p in event_files()]


def validate():
    errors=[]; ids=set()
    events=load_events()
    for p,e in events:
        eid=e.get('event_id')
        if not EVENT_RE.match(eid or ''): errors.append(f'{p}: invalid event_id')
        if eid in ids: errors.append(f'duplicate event_id: {eid}')
        ids.add(eid)
        try: created=parse_time(e['created_at'])
        except Exception as exc: errors.append(f'{p}: invalid created_at: {exc}'); created=None
        try: effective=parse_time(e.get('effective_at')) if e.get('effective_at') else None
        except Exception as exc: errors.append(f'{p}: invalid effective_at: {exc}'); effective=None
        if created:
            expected=f"{created.year:04d}/{created.month:02d}/{created.day:02d}/{created.hour:02d}/{eid}.json"
            actual=str(p.relative_to(EVENTS))
            if e.get('effective_at') is not None and effective:
                expected=f"{effective.year:04d}/{effective.month:02d}/{effective.day:02d}/{effective.hour:02d}/{eid}.json"
            if actual != expected and e.get('effective_at') is not None:
                errors.append(f'{p}: time bucket mismatch; expected {expected}')
        if not e.get('representations'): errors.append(f'{p}: missing representations')
        if not e.get('source'): errors.append(f'{p}: missing source')
        if e.get('verification',{}).get('status') == 'VERIFIED' and not e.get('verification',{}).get('canonical_url'):
            errors.append(f'{p}: verified event missing canonical_url')
    for _,e in events:
        for rel in e.get('relationships',{}).get('related',[]):
            if rel not in ids: errors.append(f"{e['event_id']}: unresolved relationship {rel}")
    idx=json.loads(INDEX.read_text(encoding='utf-8'))
    indexed={x['event_id'] for x in idx.get('events',[])}
    if indexed != ids: errors.append(f'INDEX mismatch: index={len(indexed)} events={len(ids)}')
    return errors


def retrieve(query, limit=10):
    q=set(re.findall(r'[a-z0-9]+',query.lower())); results=[]
    for _,e in load_events():
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


def fixed_offset(value):
    sign=1 if value.startswith('+') else -1
    hours,minutes=map(int,value[1:].split(':'))
    return timezone(sign*timedelta(hours=hours,minutes=minutes))


def daily(day, offset='-07:00'):
    tz=fixed_offset(offset)
    start=datetime.fromisoformat(day+'T00:00:00'+offset)
    end=start+timedelta(days=1)
    selected=[]
    for _,e in load_events():
        t=e.get('effective_at') or e.get('created_at')
        dt=parse_time(t).astimezone(tz)
        if start <= dt < end: selected.append(e)
    learning=[]; wins=[]; nexts=[]
    for e in selected:
        learning += e.get('representations',{}).get('naya',{}).get('lessons',[])
        if e.get('event_type') in {'milestone','success'}: wins.append(e['event_id'])
        nexts += e.get('representations',{}).get('naya',{}).get('next_best_actions',[])
    return {'report_type':'DAILY_INTELLIGENCE_REPORT','period':day,'timezone':offset,'event_count':len(selected),'source_event_ids':[e['event_id'] for e in selected],'learning':learning,'wins':wins,'next_best_actions':nexts,'verification_required':True,'feed_receipt_required_when_supported':True}


def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='cmd',required=True)
    sub.add_parser('validate')
    r=sub.add_parser('retrieve'); r.add_argument('query'); r.add_argument('--limit',type=int,default=10)
    d=sub.add_parser('daily-report'); d.add_argument('day'); d.add_argument('--offset',default='-07:00')
    args=ap.parse_args()
    if args.cmd=='validate':
        errors=validate(); print('PASS — Smart Notes v3 is structurally valid' if not errors else 'FAIL\n'+'\n'.join('- '+x for x in errors)); return 0 if not errors else 1
    if args.cmd=='retrieve':
        for score,e in retrieve(args.query,args.limit): print(f"{score:3} {e['event_id']} | {e['subject']} | {e['event_type']}")
        return 0
    print(json.dumps(daily(args.day,args.offset),indent=2,ensure_ascii=False)); return 0

if __name__=='__main__': raise SystemExit(main())
