#!/usr/bin/env python3
"""Machine-enforce project, Next Execution, paired-note, learning, and prompt contracts."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
MEMORY=ROOT/'.naya'/'memory'; EVENTS=MEMORY/'events'; PROJECT=MEMORY/'projects'/'CURRENT-DAILY-PROJECT.json'; POLICY=MEMORY/'CONTINUITY-ENFORCEMENT-POLICY.json'; REPORT=MEMORY/'PROJECT-EXECUTION-CONTRACT-REPORT.json'
EVENT_RE=re.compile(r'^SE-[0-9]{8}-[0-9]{6}-[a-z0-9-]+$'); NEXT_RE=re.compile(r'^NEXT-EXECUTION-[0-9]{8}-.+\.md$')

def load(path:Path)->dict[str,Any]: return json.loads(path.read_text(encoding='utf-8'))
def event_files(): return sorted(EVENTS.rglob('SE-*.json')) if EVENTS.exists() else []
def is_meaningful(event,policy):
    if event.get('continuity_required') is True:return True
    typ=str(event.get('event_type',event.get('type',''))).lower()
    if typ in {str(x).lower() for x in policy.get('meaningful_event_types',[])}:return True
    tags={str(x).lower() for x in (event.get('tags') or [])}
    meaningful_tags={str(x).lower() for x in policy.get('meaningful_tags',[])}
    return bool(tags.intersection(meaningful_tags))
def validate_project(p):
    req=('project_id','project_name','date','goal','vision','mission','north_star','current_objective','success_criteria','constraints','current_state','next_execution_path')
    return [f'project state missing {k}' for k in req if k not in p or p.get(k) is None or p.get(k)=='']
def validate_next_execution(n):
    req=('schema_version','status','project','north_star','current_state','completed_work','verified_evidence','unresolved_issues','constraints','current_objective','next_action','execution_instructions','success_criteria','verification_requirements')
    return [f'next execution missing {k}' for k in req if k not in n or n.get(k) is None or n.get(k)=='']
def validate_event(event,project,policy):
    errors=[]; eid=str(event.get('event_id','<missing>'))
    if not EVENT_RE.match(eid):errors.append(f'{eid}: invalid event_id')
    if event.get('project')!=project.get('project_name'):errors.append(f'{eid}: meaningful execution must bind to CURRENT-DAILY-PROJECT ({project.get("project_name")})')
    ctx=event.get('project_context') or {}
    if ctx.get('project_id')!=project.get('project_id'):errors.append(f'{eid}: missing project_context.project_id binding')
    if not ctx.get('current_objective'):errors.append(f'{eid}: missing project_context.current_objective')
    reps=event.get('representations') or {}; naya=reps.get('naya') if isinstance(reps,dict) else None; shawn=(reps.get('shawn') or reps.get('human')) if isinstance(reps,dict) else None
    if not naya or not shawn:errors.append(f'{eid}: paired representations are required')
    else:
        if naya.get('canonical_event_id')!=eid:errors.append(f'{eid}: Naya representation is not bound to canonical event')
        if shawn.get('canonical_event_id')!=eid:errors.append(f'{eid}: Shawn/Human representation is not bound to canonical event')
        if naya.get('id')==shawn.get('id'):errors.append(f'{eid}: Naya and Shawn/Human representation IDs must remain distinct')
    nex=event.get('next_execution') or {}; path=nex.get('path') or (event.get('continuity') or {}).get('next_execution_path')
    if not path or not NEXT_RE.match(Path(path).name):errors.append(f'{eid}: invalid or missing Next Execution contract path')
    else:
        doc=ROOT/path
        if not doc.exists():errors.append(f'{eid}: Next Execution artifact missing: {path}')
        else:
            try:errors.extend([f'{eid}: {x}' for x in validate_next_execution(load(doc))])
            except Exception as exc:errors.append(f'{eid}: Next Execution parse failure: {exc}')
    learning=event.get('learning') or {}; continuity=event.get('continuity') or {}; lessons=[]
    for rep in (naya,shawn):
        if isinstance(rep,dict):lessons += rep.get('lessons',[]) or rep.get('learning',[]) or rep.get('what_we_learned',[]) or []
    if not lessons and not learning.get('status') and not continuity.get('learning_status'):errors.append(f'{eid}: meaningful execution requires learning capture or explicit learning status')
    return errors
def validate():
    errors=validate_project(load(PROJECT)) if PROJECT.exists() else ['missing CURRENT-DAILY-PROJECT.json']; project=load(PROJECT) if PROJECT.exists() else {}; policy=load(POLICY); checked=0
    for path in event_files():
        event=load(path)
        if not is_meaningful(event,policy):continue
        if str(event.get('effective_at',''))<str(policy.get('effective_at','')):continue
        checked+=1; errors.extend([f'{path}: {x}' for x in validate_event(event,project,policy)])
    report={'schema_version':1,'status':'GREEN' if not errors else 'RED','meaningful_events_checked':checked,'error_count':len(errors),'errors':errors,'checks':['current_daily_project','project_event_binding','paired_representation_identity','next_execution_contract','learning_capture']}
    REPORT.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8'); return (0 if not errors else 1),report
def self_test():
    project={'project_id':'PRJ-TEST','project_name':'Test Project'}; policy={'meaningful_event_types':['implementation'],'meaningful_tags':[]}
    base={'event_id':'SE-20260825-999999-contract-test','event_type':'implementation','project':'Test Project','project_context':{'project_id':'PRJ-TEST','current_objective':'test'},'representations':{'naya':{'id':'SN-20260825-999999-naya','canonical_event_id':'SE-20260825-999999-contract-test','lessons':['test learning']},'shawn':{'id':'SN-20260825-999999-shawn','canonical_event_id':'SE-20260825-999999-contract-test','lessons':['test lesson']}},'continuity':{'learning_status':'LEARNED'},'next_execution':{'path':'.naya/handoffs/NEXT-EXECUTION-20260825-TEST.md'}}
    complete={'schema_version':1,'status':'READY','project':'Test Project','north_star':'test','current_state':'test','completed_work':['test'],'verified_evidence':['test'],'unresolved_issues':[],'constraints':['test'],'current_objective':'test','next_action':'test','execution_instructions':['test'],'success_criteria':['test'],'verification_requirements':['test']}
    assert not validate_project({'project_id':'x','project_name':'x','date':'x','goal':'x','vision':'x','mission':'x','north_star':'x','current_objective':'x','success_criteria':['x'],'constraints':['x'],'current_state':'x','next_execution_path':'x'})
    assert validate_next_execution(complete)==[]
    errors=validate_event(base,project,policy); assert any('artifact missing' in x for x in errors)
    bad=json.loads(json.dumps(base)); bad['project']='Wrong Project'; bad['representations']['naya']['canonical_event_id']='WRONG'; bad_errors=validate_event(bad,project,policy); assert any('bind' in x for x in bad_errors) and any('Naya representation' in x for x in bad_errors)
    print('PASS — project/Next Execution/paired-representation deliberate-failure tests GREEN'); return 0
def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='command',required=True); sub.add_parser('validate'); sub.add_parser('self-test'); args=ap.parse_args()
    if args.command=='self-test':return self_test()
    code,report=validate(); print('PASS — project/execution contracts are GREEN' if code==0 else 'FAIL — project/execution contracts are RED'); print(json.dumps(report,indent=2,ensure_ascii=False)); return code
if __name__=='__main__':raise SystemExit(main())
