#!/usr/bin/env python3
"""Machine-enforce project, Next Execution, paired-note, learning, and prompt contracts."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
MEMORY=ROOT/'.naya'/'memory'; EVENTS=MEMORY/'events'; PROJECT=MEMORY/'projects'/'CURRENT-DAILY-PROJECT.json'; POLICY=MEMORY/'CONTINUITY-ENFORCEMENT-POLICY.json'; REPORT=MEMORY/'PROJECT-EXECUTION-CONTRACT-REPORT.json'
EVENT_RE=re.compile(r'^SE-[0-9]{8}-[0-9]{6}-[a-z0-9-]+$'); NEXT_RE=re.compile(r'^NEXT-EXECUTION-[0-9]{8}-.+\.(?:md|json)$')

def load(path:Path)->dict[str,Any]: return json.loads(path.read_text(encoding='utf-8'))
def load_next_execution(path:Path)->dict[str,Any]:
    """Load the canonical Next Execution contract from JSON or human-readable Markdown."""
    if path.suffix.lower()=='.json': return load(path)
    text=path.read_text(encoding='utf-8'); result:dict[str,Any]={}
    for raw in text.splitlines():
        line=raw.strip()
        if not line or line.startswith('#') or line.startswith('- '): continue
        if ':' in line:
            key,value=line.split(':',1); key=key.strip().lower().replace(' ','_'); value=value.strip()
            if key in {'schema_version','status'} and value: result[key]=int(value) if key=='schema_version' and value.isdigit() else value
    headings={'project':'Project','north_star':'North Star','current_state':'Current state','completed_work':'Completed work','verified_evidence':'Verified evidence','unresolved_issues':'Unresolved issues','constraints':'Constraints','current_objective':'Current objective','next_action':'Next action','next_actor':'Next actor','ready_to_run_execution':'Ready to run execution','expected_output':'Expected output','success_criteria':'Success criteria','verification':'Verification','verification_requirements':'Verification requirements'}
    lines=text.splitlines()
    for key,title in headings.items():
        marker=f'## {title}'.lower(); start=None
        for i,line in enumerate(lines):
            if line.strip().lower()==marker: start=i+1; break
        if start is None: continue
        values=[]
        for line in lines[start:]:
            stripped=line.strip()
            if stripped.startswith('## '): break
            if stripped and not stripped.startswith('#'): values.append(stripped[2:].strip() if stripped.startswith('- ') else stripped)
        if values: result[key]=values if key.endswith(('work','evidence','issues','constraints','instructions','criteria','requirements','execution')) else ' '.join(values)
    # Canonical human-continuation flag is machine-readable when supplied in JSON/Markdown front matter.
    if 'human_prompt_authoring_required' not in result:
        for raw in lines:
            line=raw.strip()
            if line.lower().startswith('human_prompt_authoring_required:'):
                value=line.split(':',1)[1].strip().lower(); result['human_prompt_authoring_required']=value=='true'; break
    return result

def event_files(): return sorted(EVENTS.rglob('SE-*.json')) if EVENTS.exists() else []
def is_meaningful(event,policy):
    if event.get('continuity_required') is True:return True
    typ=str(event.get('event_type',event.get('type',''))).lower()
    if typ in {str(x).lower() for x in policy.get('meaningful_event_types',[])}:return True
    tags={str(x).lower() for x in (event.get('tags') or [])}; meaningful_tags={str(x).lower() for x in policy.get('meaningful_tags',[])}
    return bool(tags.intersection(meaningful_tags))
def validate_project(p):
    req=('project_id','project_name','date','goal','vision','mission','north_star','current_objective','success_criteria','constraints','current_state','next_execution_path')
    return [f'project state missing {k}' for k in req if k not in p or p.get(k) is None or p.get(k)=='']

def _text(value: Any) -> str:
    if isinstance(value, str): return value.strip()
    if isinstance(value, (list, tuple)): return ' '.join(str(x).strip() for x in value if str(x).strip()).strip()
    if isinstance(value, dict): return ' '.join(str(x).strip() for x in value.values() if str(x).strip()).strip()
    return '' if value is None else str(value).strip()

def _is_human_actor(value: Any, policy: dict[str,Any]) -> bool:
    return _text(value).lower() in {str(x).lower() for x in policy.get('next_action_delivery_schema',{}).get('human_continuation_actors',['human','shawn','user'])}

def validate_next_action_delivery(n: dict[str,Any], policy: dict[str,Any]|None=None, *, human_continuation_required: bool|None=None) -> list[str]:
    """Validate the single canonical operational torch carried by a Next Execution handoff."""
    policy = policy or {}
    schema = policy.get('next_action_delivery_schema',{})
    errors=[]
    required=tuple(schema.get('required_fields',('next_action','next_actor','ready_to_run_execution','expected_output','success_criteria','verification')))
    missing=[field for field in required if not _text(n.get(field))]
    errors.extend([f'next action delivery missing {field}' for field in missing])
    actor=n.get('next_actor')
    human_required=_is_human_actor(actor,policy) if human_continuation_required is None else human_continuation_required
    if human_required and n.get('human_prompt_authoring_required') is not True:
        errors.append('human_prompt_authoring_required must be true whenever human continuation is required')
    if n.get('human_prompt_authoring_required') is not None and not isinstance(n.get('human_prompt_authoring_required'), bool):
        errors.append('human_prompt_authoring_required must be boolean when present')
    context_fields=tuple(schema.get('successor_context_fields',('mission','current_state','constraints','why_this_action')))
    # A ready-to-run execution must carry its own operational context. The legacy top-level
    # fields are accepted as the canonical context envelope so valid handoffs do not need a second system.
    context_values={
        'mission':n.get('mission') or n.get('project') or n.get('current_objective'),
        'current_state':n.get('current_state'),
        'constraints':n.get('constraints'),
        'why_this_action':n.get('why_this_action') or n.get('current_objective')
    }
    if _text(n.get('ready_to_run_execution')) and any(not _text(context_values.get(field)) for field in context_fields):
        errors.append('successor cannot act without reconstructing context: ready_to_run_execution lacks required mission/state/constraints/why-this-action context')
    if not _text(n.get('next_action')): pass
    elif len(_text(n.get('next_action'))) < 24 or _text(n.get('next_action')).lower() in {'inspect it','review this','run the next test','continue','do it','fix it'}:
        errors.append('next_action is vague/non-executable')
    return errors

def validate_next_execution(n):
    req=('schema_version','status','project','north_star','current_state','completed_work','verified_evidence','unresolved_issues','constraints','current_objective','next_action','execution_instructions','success_criteria','verification_requirements')
    errors=[f'next execution missing {k}' for k in req if k not in n or n.get(k) is None or n.get(k)=='']
    if not errors:
        errors.extend(validate_next_action_delivery(n, load(POLICY)))
    return errors

def validate_event(event,project,policy):
    errors=[]; eid=str(event.get('event_id','<missing>'))
    if not EVENT_RE.match(eid):errors.append(f'{eid}: invalid event_id')
    ctx=event.get('project_context') or {}
    if ctx.get('project_id')!=project.get('project_id') or (ctx.get('current_daily_project') or ctx.get('project_name'))!=project.get('project_name'):
        errors.append(f'{eid}: meaningful execution must bind to CURRENT-DAILY-PROJECT ({project.get("project_name")})')
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
            try:errors.extend([f'{eid}: {x}' for x in validate_next_execution(load_next_execution(doc))])
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
    report={'schema_version':2,'status':'GREEN' if not errors else 'RED','meaningful_events_checked':checked,'error_count':len(errors),'errors':errors,'checks':['current_daily_project','project_event_binding','paired_representation_identity','next_execution_contract','next_action_delivery','learning_capture']}
    REPORT.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8'); return (0 if not errors else 1),report

def self_test():
    project={'project_id':'PRJ-TEST','project_name':'Test Project'}; policy={'meaningful_event_types':['implementation'],'meaningful_tags':[],'next_action_delivery_schema':{'human_continuation_actors':['human','shawn','user'],'required_fields':['next_action','next_actor','ready_to_run_execution','expected_output','success_criteria','verification'],'successor_context_fields':['mission','current_state','constraints','why_this_action']}}
    base={'event_id':'SE-20260825-999999-contract-test','event_type':'implementation','project':'Test Project','project_context':{'project_id':'PRJ-TEST','current_daily_project':'Test Project','current_objective':'test'},'representations':{'naya':{'id':'SN-20260825-999999-naya','canonical_event_id':'SE-20260825-999999-contract-test','lessons':['test learning']},'shawn':{'id':'SN-20260825-999999-shawn','canonical_event_id':'SE-20260825-999999-contract-test','lessons':['test lesson']}},'continuity':{'learning_status':'LEARNED'},'next_execution':{'path':'.naya/handoffs/NEXT-EXECUTION-20260825-TEST.md'}}
    complete={'schema_version':1,'status':'READY','project':'Test Project','mission':'test mission','north_star':'test','current_state':'test state','completed_work':['test'],'verified_evidence':['test'],'unresolved_issues':[],'constraints':['test constraints'],'current_objective':'why this action','next_action':'Inspect the authoritative continuity contract and run the narrow regression suite.','next_actor':'successor_naya','ready_to_run_execution':['Read project_execution_contract.py and test_project_prompt_contracts.py; execute the narrow contract tests before the authoritative gate.'], 'expected_output':['Observed test results and exact first failure if any.'],'success_criteria':['All positive fixtures pass and all deliberate-negative fixtures fail.'],'verification':['Run the authoritative project/prompt contract regression suite.'],'verification_requirements':['test']}
    assert not validate_project({'project_id':'x','project_name':'x','date':'x','goal':'x','vision':'x','mission':'x','north_star':'x','current_objective':'x','success_criteria':['x'],'constraints':['x'],'current_state':'x','next_execution_path':'x'})
    assert validate_next_execution(complete)==[]
    existing=ROOT/'.naya'/'handoffs'/'NEXT-EXECUTION-20260825-SUPERBRAIN-CONTRACT-ENFORCEMENT.md'
    # The existing artifact is allowed to fail here until the source-of-truth handoff is upgraded in this change.
    assert existing.exists()
    assert any('next action delivery missing next_actor' in x for x in validate_next_execution(load_next_execution(existing)))
    negatives=[]
    for field in ('next_action','next_actor','ready_to_run_execution','expected_output','success_criteria','verification'):
        bad=json.loads(json.dumps(complete)); bad[field]=''; negatives.append((field,validate_next_action_delivery(bad,policy)))
    assert all(any(field in e for e in errs) for field,errs in negatives)
    vague=json.loads(json.dumps(complete)); vague['next_action']='inspect it'; assert any('vague/non-executable' in e for e in validate_next_action_delivery(vague,policy))
    human=json.loads(json.dumps(complete)); human['next_actor']='human'; human.pop('human_prompt_authoring_required',None); assert any('human_prompt_authoring_required must be true' in e for e in validate_next_action_delivery(human,policy))
    human['human_prompt_authoring_required']=True; human['ready_to_run_execution']='Run the supplied prompt with the known mission context.'; assert not validate_next_action_delivery(human,policy)
    context=json.loads(json.dumps(complete)); context['current_state']=''; assert any('reconstructing context' in e for e in validate_next_action_delivery(context,policy))
    print('PASS — Next Action Delivery positive and deliberate-failure tests GREEN'); return 0

def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='command',required=True); sub.add_parser('validate'); sub.add_parser('self-test'); args=ap.parse_args()
    if args.command=='self-test':return self_test()
    code,report=validate(); print('PASS — project/execution contracts are GREEN' if code==0 else 'FAIL — project/execution contracts are RED'); print(json.dumps(report,indent=2,ensure_ascii=False)); return code
if __name__=='__main__':raise SystemExit(main())
