#!/usr/bin/env python3
"""Naya Power Smart Brain v3.

Canonical source: chronological Note Events under .naya/memory/events.
The runtime deliberately tolerates the v2 event envelope while enforcing the
v3 retrieval and CIS model, so migration can be incremental without losing history.
Indexes are derived; canonical event JSON remains the source of truth.
"""
from __future__ import annotations
import argparse, json, math, re
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[2]
MEMORY = ROOT / '.naya' / 'memory'
EVENTS = MEMORY / 'events'
INDEX = EVENTS / 'INDEX.json'
EVENT_RE = re.compile(r'^SE-[0-9]{8}-[0-9]{6}-[a-z0-9-]+$')
NOTE_RE = re.compile(r'^SN-[0-9]{8}-[0-9]{6}-.+$')
VALID_STATUS = {'ACTIVE','CANONICAL','HISTORICAL','SUPERSEDED','CONFLICTED','STALE'}


def parse_time(value):
    if value.endswith('Z'): value = value[:-1] + '+00:00'
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None: raise ValueError('timestamp must include timezone')
    return dt


def tokens(text): return re.findall(r'[a-z0-9]+', str(text).lower())


def event_files(): return sorted(EVENTS.rglob('SE-*.json')) if EVENTS.exists() else []


def load_events():
    out=[]
    for p in event_files():
        try: out.append((p,json.loads(p.read_text(encoding='utf-8'))))
        except Exception as exc: out.append((p,{'__parse_error__':str(exc)}))
    return out


def reps(e):
    r=e.get('representations',{})
    if isinstance(r,dict): return list(r.values())
    return r if isinstance(r,list) else []


def all_text(e):
    parts=[e.get('event_id',''),e.get('title',''),e.get('subject',''),e.get('project',''),e.get('event_type',''),e.get('type',''),e.get('summary','')]
    for k in ('tags','aliases','concepts'): parts += e.get(k,[]) or []
    for r in reps(e):
        parts += [r.get('title',''),r.get('summary',''),r.get('content','')]
        parts += r.get('lessons',[]) or r.get('what_we_learned',[]) or r.get('learning',[]) or []
        parts += r.get('next_best_actions',[]) or r.get('what_changed',[]) or []
        parts += r.get('aliases',[]) or []
    return ' '.join(map(str,parts))


def validate_event(e,p):
    errors=[]
    if not EVENT_RE.match(e.get('event_id','')): errors.append(f'{p}: invalid event_id')
    parsed={}
    for k in ('created_at','effective_at'):
        try: parsed[k]=parse_time(e[k])
        except Exception as exc: errors.append(f'{p}: invalid {k}: {exc}')
    if e.get('status') not in VALID_STATUS: errors.append(f'{p}: invalid status')
    if not reps(e): errors.append(f'{p}: missing representations')
    if not e.get('source'): errors.append(f'{p}: missing source')
    v=e.get('verification',{})
    if v.get('status')=='VERIFIED' and not v.get('canonical_url'): errors.append(f'{p}: verified event missing canonical_url')
    dt=parsed.get('effective_at')
    if dt:
        expected=f'{dt:%Y/%m/%d/%H}/{e["event_id"]}.json'
        try: relative=str(p.relative_to(EVENTS))
        except ValueError: relative=str(p)
        if relative != expected: errors.append(f'{p}: physical time bucket mismatch; expected {expected}')
    for r in reps(e):
        if r.get('id') and not NOTE_RE.match(r['id']): errors.append(f'{p}: invalid representation id {r["id"]}')
    return errors


def validate():
    errors=[]; ids={}
    loaded=load_events()
    for p,e in loaded:
        if e.get('__parse_error__'): errors.append(f'{p}: {e["__parse_error__"]}'); continue
        errors += validate_event(e,p); eid=e.get('event_id')
        if eid in ids: errors.append(f'duplicate event_id: {eid}')
        ids[eid]=str(p)
    for _,e in loaded:
        if e.get('__parse_error__'): continue
        rel=e.get('relationships',{}) or {}
        for key in ('related','depends_on','supersedes','superseded_by','source_events'):
            vals=rel.get(key,[])
            if vals is None: continue
            vals=[vals] if isinstance(vals,str) else vals
            if not isinstance(vals,list): errors.append(f'{e["event_id"]}: invalid relationship list: {key}'); continue
            for target in vals:
                if target and target not in ids and not str(target).startswith('EXT:'): errors.append(f'{e["event_id"]}: unresolved {key}: {target}')
    if not INDEX.exists(): errors.append('missing events/INDEX.json')
    else:
        try:
            idx=json.loads(INDEX.read_text(encoding='utf-8'))
            indexed={x.get('event_id') if isinstance(x,dict) else x for x in idx.get('events',[])}
            if indexed != set(ids): errors.append(f'INDEX mismatch: index={len(indexed)} canonical={len(ids)}')
        except Exception as exc: errors.append(f'INDEX invalid: {exc}')
    return errors


def build_index():
    rows=[]
    for p,e in load_events():
        if e.get('__parse_error__'): continue
        dt=parse_time(e['effective_at'])
        rows.append({'event_id':e['event_id'],'path':str(p.relative_to(EVENTS)),'subject':e.get('subject',''),'type':e.get('type') or e.get('event_type',''),'tags':e.get('tags',[]) or []})
    rows.sort(key=lambda x:(x['path'],x['event_id']))
    data={'version':'3.0.0','status':'CANONICAL','organization':'YEAR/MONTH/DAY/HOUR/EVENT','event_count':len(rows),'events':rows}
    INDEX.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8'); return data


def corpus(events):
    docs=[]; df=Counter()
    for e in events:
        c=Counter(tokens(all_text(e))); docs.append(c); df.update(c.keys())
    n=max(1,len(docs)); return docs,{t:math.log((n+1)/(d+1))+1 for t,d in df.items()}


def cosine(q,doc,idf):
    if not q or not doc:return 0.0
    qc=Counter(q); qv={t:(1+math.log(c))*idf.get(t,1) for t,c in qc.items()}; dv={t:(1+math.log(c))*idf.get(t,0) for t,c in doc.items()}
    dot=sum(qv.get(t,0)*dv.get(t,0) for t in qv); qn=math.sqrt(sum(x*x for x in qv.values())); dn=math.sqrt(sum(x*x for x in dv.values()))
    return dot/(qn*dn) if qn and dn else 0.0


def lexical(query,e):
    q=set(tokens(query)); title=set(tokens(e.get('title',''))); aliases=set(tokens(' '.join(e.get('aliases',[]) or []))); tags=set(tokens(' '.join(e.get('tags',[]) or []))); concepts=set(tokens(' '.join(e.get('concepts',[]) or []))); body=set(tokens(all_text(e)))
    return len(q&title)*120+len(q&aliases)*90+len(q&tags)*70+len(q&concepts)*65+len(q&body)*18


def retrieve(query,limit=10,since=None,until=None):
    loaded=[(p,e) for p,e in load_events() if not e.get('__parse_error__')]; es=[e for _,e in loaded]; docs,idf=corpus(es); q=tokens(query); ranked=[]
    for i,e in enumerate(es):
        dt=parse_time(e['effective_at'])
        if since and dt<since or until and dt>until: continue
        score=lexical(query,e)+cosine(q,docs[i],idf)*180; ql=query.lower()
        score += 80 if e.get('subject') and e['subject'].lower() in ql else 0
        score += 60 if e.get('project') and e['project'].lower() in ql else 0
        score += 25 if e.get('verification',{}).get('status')=='VERIFIED' else 0
        score += {'ACTIVE':30,'CANONICAL':25,'HISTORICAL':0,'CONFLICTED':-20,'STALE':-40,'SUPERSEDED':-70}.get(e.get('status'),0)
        ranked.append([score,e])
    ranked.sort(key=lambda x:x[0],reverse=True); seed={e['event_id'] for _,e in ranked[:3]}
    for row in ranked:
        rel=row[1].get('relationships',{}) or {}; targets=set()
        for k in ('related','depends_on','supersedes','superseded_by','source_events'):
            v=rel.get(k,[]); targets.update([v] if isinstance(v,str) else (v or []))
        if targets&seed: row[0]+=35
    ranked.sort(key=lambda x:(-x[0],x[1]['effective_at'],x[1]['event_id'])); return ranked[:limit]


def daily_report(day=None,tz_name='America/Vancouver'):
    zone=ZoneInfo(tz_name); local_day=datetime.now(zone).date()-timedelta(days=1) if day is None else datetime.fromisoformat(day).date(); start=datetime.combine(local_day,datetime.min.time(),zone); end=start+timedelta(days=1); selected=[]
    for _,e in load_events():
        if e.get('__parse_error__'):continue
        dt=parse_time(e['effective_at']).astimezone(zone)
        if start<=dt<end:selected.append(e)
    selected.sort(key=lambda x:x['effective_at']); lessons=[]; changes=[]; nexts=[]
    for e in selected:
        for r in reps(e):
            lessons += r.get('lessons',[]) or r.get('what_we_learned',[]) or r.get('learning',[]) or []; changes += r.get('what_changed',[]) or []; nexts += r.get('next_best_actions',[]) or []
    uniq=lambda xs:list(dict.fromkeys(xs))
    return {'report_type':'DAILY_INTELLIGENCE_REPORT','period':local_day.isoformat(),'timezone':tz_name,'event_count':len(selected),'source_event_ids':[e['event_id'] for e in selected],'what_happened':[e.get('title') or e.get('subject') for e in selected],'what_we_learned':uniq(lessons),'what_changed':uniq(changes),'wins':[e['event_id'] for e in selected if e.get('event_type') in {'milestone','success'} or e.get('type')=='milestone'],'next_best_actions':uniq(nexts),'open_loops':[e['event_id'] for e in selected if e.get('status') in {'CONFLICTED','STALE'}],'verification_required':True,'feed_status':'PENDING_INTEGRATION'}


def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='cmd',required=True); sub.add_parser('validate'); sub.add_parser('index')
    r=sub.add_parser('retrieve'); r.add_argument('query'); r.add_argument('--limit',type=int,default=10)
    d=sub.add_parser('daily-report'); d.add_argument('--day'); d.add_argument('--timezone',default='America/Vancouver')
    a=ap.parse_args()
    if a.cmd=='validate':
        err=validate(); print('PASS — Smart Brain v3 validation is GREEN' if not err else 'FAIL\n'+'\n'.join('- '+x for x in err)); return 0 if not err else 1
    if a.cmd=='index': print(json.dumps(build_index(),indent=2,ensure_ascii=False)); return 0
    if a.cmd=='retrieve':
        for s,e in retrieve(a.query,a.limit): print(f'{s:7.2f} {e["event_id"]} | {e.get("title") or e.get("subject")} | {e.get("status")}')
        return 0
    print(json.dumps(daily_report(a.day,a.timezone),indent=2,ensure_ascii=False)); return 0

if __name__=='__main__': raise SystemExit(main())
