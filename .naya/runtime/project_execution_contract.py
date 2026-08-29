#!/usr/bin/env python3
"""Machine-enforce project, Next Execution, successor-torch, learning, and prompt contracts."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
MEMORY=ROOT/'.naya'/'memory'; EVENTS=MEMORY/'events'; PROJECT=MEMORY/'projects'/'CURRENT-DAILY-PROJECT.json'; POLICY=MEMORY/'CONTINUITY-ENFORCEMENT-POLICY.json'; TORCH_CONTRACT=ROOT/'.naya'/'contracts'/'NEXT-ACTION-DELIVERY-CONTRACT-v1.json'; REPORT=MEMORY/'PROJECT-EXECUTION-CONTRACT-REPORT.json'
EVENT_RE=re.compile(r'^SE-[0-9]{8}-[0-9]{6}-[a-z0-9-]+$'); NEXT_RE=re.compile(r'^NEXT-EXECUTION-[0-9]{8}-.+\.(?:md|json)$')

def load(path:Path)->dict[str,Any]: return json.loads(path.read_text(encoding='utf-8'))
def _nonempty(value:Any)->bool: return bool(_text(value))
def _text(value:Any)->str:
    if isinstance(value,str): return value.strip()
    if isinstance(value,(list,tuple)): return ' '.join(str(x).strip() for x in value if str(x).strip()).strip()
    if isinstance(value,dict): return ' '.join(str(x).strip() for x in value.values() if str(x).strip()).strip()
    return '' if value is None else str(value).strip()

def load_next_execution(path:Path)->dict[str,Any]:
    """Load the canonical Next Execution contract from JSON or human-readable Markdown."""
    if path.suffix.lower()=='.json': return load(path)
    text=path.read_text(encoding='utf-8'); result:dict[str,Any]={}; lines=text.splitlines()
    for raw in lines:
        line=raw.strip()
        if not line or line.startswith('#') or line.startswith('- '): continue
        if ':' in line:
            key,value=line.split(':',1); key=key.strip().lower().replace(' ','_'); value=value.strip()
            if key in {'schema_version','status'} and value: result[key]=int(value) if key=='schema_version' and value.isdigit() else value
    headings={'project':'Project','north_star':'North Star','current_state':'Current state','completed_work':'Completed work','verified_evidence':'Verified evidence','unresolved_issues':'Unresolved issues','constraints':'Constraints','current_objective':'Current objective','next_action':'Next action','next_actor':'Next actor','ready_to_run_execution':'Ready to run execution','expected_output':'Expected output','success_criteria':'Success criteria','verification':'Verification','verification_requirements':'Verification requirements','mission':'Mission','desired_outcome':'Desired outcome','verified':'Verified','unknown':'Unknown','protected':'Protected','blocked':'Blocked','decision_recommendation':'Decision / Recommendation','human_action':'Human action','human_return_payload':'Human return payload','why_this_action':'Why this action'}
    for key,title in headings.items():
        marker=f'## {title}'.lower(); start=None
        for i,line in enumerate(lines):
            if line.strip().lower()==marker: start=i+1; break
        if start is None: continue
        values=[]
        for line in lines[start:]:
            stripped=line.strip()
            if stripped.startswith('## '): break
            if stripped and not stripped.startswith('#') and not stripped.startswith('```'):
                values.append(stripped[2:].strip() if stripped.startswith('- ') else stripped)
        if values: result[key]=values if key in {'completed_work','verified_evidence','unresolved_issues','constraints','verification_requirements'} else ' '.join(values)
    for raw in lines:
        line=raw.strip()
        if line.lower().startswith('human_prompt_authoring_required:'):
            result['human_prompt_authoring_required']=line.split(':',1)[1].strip().lower()=='true'; break
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
def _is_human_actor(value:Any,policy:dict[str,Any])->bool:
    return _text(value).lower() in {str(x).lower() for x in policy.get('next_action_delivery_schema',{}).get('human_continuation_actors',['human','shawn','user'])}
def _torch_required_fields(policy,contract=None):
    return tuple(contract.get('required_fields',())) if contract and contract.get('required_fields') else tuple(policy.get('next_action_delivery_schema',{}).get('required_fields',('next_action','next_actor','ready_to_run_execution','expected_output','success_criteria','verification')))
def validate_next_action_delivery(n,policy=None,*,human_continuation_required=None):
    policy=policy or {}; contract=load(TORCH_CONTRACT) if TORCH_CONTRACT.exists() else None; errors=[]
    errors += [f'next action delivery missing {field}' for field in _torch_required_fields(policy,contract) if not _nonempty(n.get(field))]
    actor=n.get('next_actor'); human_required=_is_human_actor(actor,policy) if human_continuation_required is None else human_continuation_required
    if human_required:
        if n.get('human_prompt_authoring_required') is not True: errors.append('human_prompt_authoring_required must be true whenever human continuation is required')
        for field in (contract or {}).get('human_continuation',{}).get('required_additional_fields',['human_action','human_return_payload']):
            if not _nonempty(n.get(field)): errors.append(f'human continuation missing {field}')
    elif n.get('human_prompt_authoring_required') is not None and not isinstance(n.get('human_prompt_authoring_required'),bool): errors.append('human_prompt_authoring_required must be boolean when present')
    quality=(contract or {}).get('quality_rules',{}); minimum=int(quality.get('next_action_min_chars',24)); rejected={str(x).strip().lower() for x in quality.get('rejected_next_actions',[])}; action=_text(n.get('next_action'))
    if action and (len(action)<minimum or action.lower() in rejected): errors.append('next_action is vague/non-executable')
    execution=_text(n.get('ready_to_run_execution')).lower()
    required_sections=quality.get('ready_to_run_execution_must_include',[])
    labels={'where':'where:','why':'why:','current_state':'current state:','what_was_verified':'what was verified:','what_is_unknown':'what is unknown:','what_is_protected':'what is protected:','what_is_blocked':'what is blocked:','what_to_read':'what to read:','what_to_do':'what to do:','what_not_to_do':'what not to do:','what_to_preserve':'what to preserve:','what_to_verify':'what to verify:','expected_result':'expected result:','failure_handling':'failure handling:','next_decision_point':'next decision point:'}
    if execution:
        missing_sections=[name for name in required_sections if labels.get(name,name+':') not in execution]
        errors += [f'ready_to_run_execution missing section {name}' for name in missing_sections]
    context_fields=tuple((contract or {}).get('successor_context_fields',()) or policy.get('next_action_delivery_schema',{}).get('successor_context_fields',('mission','current_state','constraints','why_this_action')))
    context_values={'mission':n.get('mission') or n.get('project') or n.get('current_objective'),'current_state':n.get('current_state'),'constraints':n.get('constraints'),'why_this_action':n.get('why_this_action') or n.get('current_objective')}
    if execution and any(not _nonempty(context_values.get(field)) for field in context_fields): errors.append('successor cannot act without reconstructing context: ready_to_run_execution lacks required mission/state/constraints/why-this-action context')
    return errors

def validate_next_execution(n):
    req=('schema_version','status','project','north_star','current_state','completed_work','verified_evidence','unresolved_issues','constraints','current_objective','next_action','execution_instructions','success_criteria','verification_requirements','next_actor','ready_to_run_execution','expected_output','verification')
    errors=[f'next execution missing {k}' for k in req if k not in n or n.get(k) is None or n.get(k)=='']
    if not errors: errors.extend(validate_next_action_delivery(n,load(POLICY)))
    return errors

def validate_event(event,project,policy):
    errors=[]; eid=str(event.get('event_id','<missing>'))
    if not EVENT_RE.match(eid): errors.append(f'{eid}: invalid event_id')
    ctx=event.get('project_context') or {}
    if ctx.get('project_id')!=project.get('project_id') or (ctx.get('current_daily_project') or ctx.get('project_name'))!=project.get('project_name'): errors.append(f'{eid}: meaningful execution must bind to CURRENT-DAILY-PROJECT ({project.get("project_name")})')
    if not ctx.get('current_objective'): errors.append(f'{eid}: missing project_context.current_objective')
    reps=event.get('representations') or {}; naya=reps.get('naya') if isinstance(reps,dict) else None; shawn=(reps.get('shawn') or reps.get('human')) if isinstance(reps,dict) else None
    if not naya or not shawn: errors.append(f'{eid}: paired representations are required')
    else:
        if naya.get('canonical_event_id')!=eid: errors.append(f'{eid}: Naya representation is not bound to canonical event')
        if shawn.get('canonical_event_id')!=eid: errors.append(f'{eid}: Shawn/Human representation is not bound to canonical event')
        if naya.get('id')==shawn.get('id'): errors.append(f'{eid}: Naya and Shawn/Human representation IDs must remain distinct')
    nex=event.get('next_execution') or {}; path=nex.get('path') or (event.get('continuity') or {}).get('next_execution_path')
    if not path or not NEXT_RE.match(Path(path).name): errors.append(f'{eid}: invalid or missing Next Execution contract path')
    else:
        doc=ROOT/path
        if not doc.exists(): errors.append(f'{eid}: Next Execution artifact missing: {path}')
        else:
            try: errors.extend([f'{eid}: {x}' for x in validate_next_execution(load_next_execution(doc))])
            except Exception as exc: errors.append(f'{eid}: Next Execution parse failure: {exc}')
    learning=event.get('learning') or {}; continuity=event.get('continuity') or {}; lessons=[]
    for rep in (naya,shawn):
        if isinstance(rep,dict): lessons += rep.get('lessons',[]) or rep.get('learning',[]) or rep.get('what_we_learned',[]) or []
    if not lessons and not learning.get('status') and not continuity.get('learning_status'): errors.append(f'{eid}: meaningful execution requires learning capture or explicit learning status')
    return errors

def validate():
    errors=validate_project(load(PROJECT)) if PROJECT.exists() else ['missing CURRENT-DAILY-PROJECT.json']; project=load(PROJECT) if PROJECT.exists() else {}; policy=load(POLICY); checked=0
    for path in event_files():
        event=load(path)
        if not is_meaningful(event,policy): continue
        if str(event.get('effective_at',''))<str(policy.get('effective_at','')): continue
        checked+=1; errors.extend([f'{path}: {x}' for x in validate_event(event,project,policy)])
    report={'schema_version':4,'status':'GREEN' if not errors else 'RED','meaningful_events_checked':checked,'error_count':len(errors),'errors':errors,'checks':['current_daily_project','project_event_binding','paired_representation_identity','next_execution_contract','next_action_delivery','human_continuation_authoring','successor_torch_execution_sections','successor_survival','learning_capture']}
    REPORT.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8'); return (0 if not errors else 1),report

def self_test():
    policy=load(POLICY)
    complete={'mission':'test mission','desired_outcome':'test outcome','current_state':'test state','verified':'test evidence','unknown':'none','protected':'test baseline','blocked':'none','decision_recommendation':'test recommendation','next_action':'Inspect the authoritative continuity contract and run the narrow regression suite now.','next_actor':'successor_naya','ready_to_run_execution':'WHERE: NayaPOWER. WHY: verify the contract. CURRENT STATE: test state. WHAT WAS VERIFIED: test evidence. WHAT IS UNKNOWN: none. WHAT IS PROTECTED: test baseline. WHAT IS BLOCKED: none. WHAT TO READ: contract and tests. WHAT TO DO: run narrow tests. WHAT NOT TO DO: bypass validators. WHAT TO PRESERVE: evidence. WHAT TO VERIFY: exact results. EXPECTED RESULT: tests pass. FAILURE HANDLING: stop at first failure. NEXT DECISION POINT: authoritative gate.','expected_output':'Observed test results and exact first failure if any.','success_criteria':'All positive fixtures pass and all deliberate-negative fixtures fail.','verification':'Run the authoritative project/prompt contract regression suite.','constraints':'test constraints','current_objective':'test objective'}
    assert validate_next_action_delivery(complete,policy)==[]
    for field in ('next_action','next_actor','ready_to_run_execution','expected_output','success_criteria','verification'):
        bad=json.loads(json.dumps(complete)); bad.pop(field,None); assert any(field in e for e in validate_next_action_delivery(bad,policy)), field
    vague=json.loads(json.dumps(complete)); vague['next_action']='inspect it'; assert any('vague/non-executable' in e for e in validate_next_action_delivery(vague,policy))
    missing_section=json.loads(json.dumps(complete)); missing_section['ready_to_run_execution']='WHERE: NayaPOWER. WHY: verify the contract.'; assert any('missing section current_state' in e for e in validate_next_action_delivery(missing_section,policy))
    human=json.loads(json.dumps(complete)); human['next_actor']='human'; assert any('human_prompt_authoring_required' in e for e in validate_next_action_delivery(human,policy))
    human['human_prompt_authoring_required']=True; assert any('human continuation missing human_action' in e for e in validate_next_action_delivery(human,policy))
    human['human_action']='Paste the requested evidence back to Naya.'; human['human_return_payload']='Paste the exact GitHub screen text.'; assert validate_next_action_delivery(human,policy)==[]
    context=json.loads(json.dumps(complete)); context['current_state']=''; assert any('reconstructing context' in e for e in validate_next_action_delivery(context,policy))
    assert TORCH_CONTRACT.exists(), 'canonical torch contract missing'
    print('PASS — successor torch positive and deliberate-failure tests GREEN'); return 0

def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='command',required=True); sub.add_parser('validate'); sub.add_parser('self-test'); args=ap.parse_args()
    if args.command=='self-test': return self_test()
    code,report=validate(); print('PASS — project/execution contracts are GREEN' if code==0 else 'FAIL — project/execution contracts are RED'); print(json.dumps(report,indent=2,ensure_ascii=False)); return code
if __name__=='__main__':raise SystemExit(main())
