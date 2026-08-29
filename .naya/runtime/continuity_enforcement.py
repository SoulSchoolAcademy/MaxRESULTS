#!/usr/bin/env python3
"""Machine-enforceable execution continuity for Naya Power."""
from __future__ import annotations
import argparse, json, os, re, sys
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
MEMORY=ROOT/".naya"/"memory"; EVENTS=MEMORY/"events"; POLICY=MEMORY/"CONTINUITY-ENFORCEMENT-POLICY.json"; REPORT=MEMORY/"CONTINUITY-VALIDATION-REPORT.json"; RECEIPT=MEMORY/"CONTINUITY-GATE-RECEIPT.json"
EVENT_RE=re.compile(r"^SE-[0-9]{8}-[0-9]{6}-[a-z0-9-]+$")
def parse_time(value:str)->datetime:
    if value.endswith("Z"): value=value[:-1]+"+00:00"
    dt=datetime.fromisoformat(value)
    if dt.tzinfo is None: raise ValueError("timestamp must include timezone")
    return dt.astimezone(timezone.utc)
def load_policy()->dict:return json.loads(POLICY.read_text(encoding="utf-8"))
def event_files():return sorted(EVENTS.rglob("SE-*.json")) if EVENTS.exists() else []
def load_event(path:Path):
    try:return json.loads(path.read_text(encoding="utf-8")),None
    except Exception as exc:return None,str(exc)
def is_meaningful_execution(event:dict,policy:dict)->bool:
    boundary=parse_time(policy["effective_at"]); effective=parse_time(event.get("effective_at",event.get("created_at","")))
    if effective<boundary:return False
    if event.get("continuity_required") is True:return True
    event_type=str(event.get("event_type",event.get("type",""))).lower()
    if event_type in set(policy.get("meaningful_event_types",[])):return True
    event_id=str(event.get("event_id","")).lower()
    if any(token in event_id for token in policy.get("event_id_markers",[])):return True
    tags={str(x).lower() for x in (event.get("tags") or [])}
    return bool(tags.intersection({str(x).lower() for x in policy.get("meaningful_tags",[])}))
def has_handoff(event:dict,policy:dict)->bool:
    continuity=event.get("continuity",{}) or {}
    if any(continuity.get(k) for k in ("handoff_url","handoff_path","ai_to_ai_handoff")):return True
    verification=event.get("verification",{}) or {}
    if verification.get("handoff_url") or verification.get("handoff_path"):return True
    event_id=event.get("event_id","")
    for root in policy.get("handoff_roots",[".naya/handoffs"]):
        base=ROOT/root
        if base.exists() and any(event_id in p.name for p in base.rglob("*")):return True
    return False
def has_structured_handoff(event:dict,policy:dict)->tuple[bool,list[str]]:
    continuity=event.get("continuity",{}) or {};handoff=continuity.get("handoff") or event.get("handoff") or {}
    if not isinstance(handoff,dict):return False,["structured handoff must be an object"]
    missing=[field for field in policy.get("structured_handoff_fields",[]) if not handoff.get(field)]
    return not missing,missing
def check_event(event:dict,path:Path,policy:dict)->list[str]:
    errors=[];eid=event.get("event_id","<missing>");continuity=event.get("continuity",{}) or {};execution_state=str(continuity.get("execution_state","COMPLETED")).upper()
    if execution_state not in {"IN_PROGRESS","COMPLETED"}:errors.append(f"{eid}: invalid continuity.execution_state={execution_state}")
    reps=event.get("representations") or {};naya=reps.get("naya") if isinstance(reps,dict) else None;human=(reps.get("shawn") or reps.get("human")) if isinstance(reps,dict) else None
    if not naya or not human:errors.append(f"{eid}: missing paired Naya + Shawn/Human representations")
    verification=event.get("verification") or {}
    if execution_state=="COMPLETED" and verification.get("status")!="VERIFIED":errors.append(f"{eid}: completed continuity requires verification.status=VERIFIED")
    if execution_state=="IN_PROGRESS" and verification.get("status") not in {None,"PENDING"}:errors.append(f"{eid}: in-progress continuity must remain PENDING until verified")
    receipt=event.get("receipt") or {}
    if not (receipt.get("receipt_id") or verification.get("receipt") or verification.get("receipt_url")):errors.append(f"{eid}: continuity requires a durable receipt reference")
    delivery=event.get("delivery") or {}
    if not delivery.get("state") and not verification.get("feed_status"):errors.append(f"{eid}: continuity requires explicit delivery state")
    if not has_handoff(event,policy):errors.append(f"{eid}: continuity requires an AI-to-AI handoff reference/artifact")
    effective=parse_time(event.get("effective_at",event.get("created_at","")));structured_boundary=parse_time(policy.get("structured_handoff_effective_at",policy["effective_at"]))
    if effective>=structured_boundary:
        structured_ok,missing=has_structured_handoff(event,policy)
        if not structured_ok:errors.append(f"{eid}: structured Future-Naya handoff missing required fields: {', '.join(missing)}")
    lessons,next_actions=[],[]
    for rep in (naya,human):
        if isinstance(rep,dict):
            lessons+=rep.get("lessons",[]) or rep.get("learning",[]) or rep.get("what_we_learned",[]) or []
            next_actions+=rep.get("next_best_actions",[]) or []
    if not lessons and not continuity.get("learning_status"):errors.append(f"{eid}: continuity requires learning or explicit learning_status")
    if not next_actions and not continuity.get("next_action_status"):errors.append(f"{eid}: continuity requires a next-action record")
    if not EVENT_RE.match(str(eid)):errors.append(f"{path}: invalid event_id")
    return errors
def validate()->tuple[int,dict]:
    policy=load_policy();checked=0;errors=[]
    for path in event_files():
        event,parse_error=load_event(path)
        if parse_error:errors.append(f"{path}: JSON parse error: {parse_error}");continue
        if not is_meaningful_execution(event,policy):continue
        checked+=1;errors.extend(check_event(event,path,policy))
    report={"schema_version":2,"status":"GREEN" if not errors else "RED","policy_effective_at":policy["effective_at"],"structured_handoff_effective_at":policy.get("structured_handoff_effective_at"),"meaningful_execution_events_checked":checked,"error_count":len(errors),"errors":errors,"checks":["paired_naya_human_representation","verification_state_by_execution_state","durable_receipt","delivery_state","ai_to_ai_handoff","structured_future_naya_handoff","naya_owned_human_continuation","learning_or_explicit_non_applicability","next_action"]}
    REPORT.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8");return (0 if not errors else 1),report
def emit_receipt()->int:
    code,report=validate();receipt={"schema_version":1,"receipt_type":"superbrain-continuity-gate","status":"VERIFIED" if code==0 else "FAILED","created_at":datetime.now(timezone.utc).isoformat(),"commit_sha":os.environ.get("GITHUB_SHA"),"workflow_run_id":os.environ.get("GITHUB_RUN_ID"),"workflow_job":os.environ.get("GITHUB_JOB"),"repository":os.environ.get("GITHUB_REPOSITORY"),"report":report,"evidence":{"validation_report":str(REPORT.relative_to(ROOT))}};RECEIPT.write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+"\n",encoding="utf-8");print(json.dumps(receipt,indent=2,ensure_ascii=False));return code
def self_test()->int:
    policy=load_policy()
    good={"event_id":"SE-20260825-999999-continuity-positive-test","effective_at":policy["structured_handoff_effective_at"],"event_type":"execution-milestone","representations":{"naya":{"id":"SN-20260825-999999-test-naya","lessons":["test lesson"],"next_best_actions":["test next"]},"shawn":{"id":"SN-20260825-999999-test-shawn","lessons":["human lesson"],"next_best_actions":["human next"]}},"verification":{"status":"VERIFIED","receipt":"RCPT-test"},"receipt":{"receipt_id":"RCPT-test"},"delivery":{"state":"VERIFIED"},"continuity":{"handoff_url":"https://example.invalid/handoff","learning_status":"LEARNED","execution_state":"COMPLETED","handoff":{"mission":"test mission","source_of_truth":"test source","current_state":"test state","protected_baseline":"test baseline","work_completed":"test work","evidence":"test evidence","decisions":"test decisions","lessons":"test lessons","unknowns":"none","risks":"none","recommendation":"test recommendation","next_action":"test next action","ready_to_run_execution":"test execution","human_continuation":"test Naya-authored human continuation","human_continuation_naya_authored":True}}}
    if check_event(good,Path("positive-fixture.json"),policy):print("FAIL — positive continuity fixture rejected");return 1
    bad=json.loads(json.dumps(good));del bad["receipt"];bad["verification"].pop("receipt",None);bad["continuity"].pop("handoff_url",None);bad["continuity"].pop("learning_status",None);bad["representations"]["naya"].pop("lessons",None);bad["representations"]["shawn"].pop("lessons",None);bad["continuity"]["handoff"].pop("ready_to_run_execution",None);bad["continuity"]["handoff"].pop("human_continuation",None);bad["continuity"]["handoff"].pop("human_continuation_naya_authored",None)
    errors=check_event(bad,Path("negative-fixture.json"),policy);required_fragments=["durable receipt","AI-to-AI handoff","learning","structured Future-Naya handoff"]
    if not all(any(fragment in error for error in errors) for fragment in required_fragments):print("FAIL — negative continuity fixture did not expose all deliberate failures");return 1
    print("PASS — continuity positive and deliberate-failure tests GREEN");return 0
def main()->int:
    parser=argparse.ArgumentParser();sub=parser.add_subparsers(dest="command",required=True);sub.add_parser("validate");sub.add_parser("self-test");sub.add_parser("receipt");args=parser.parse_args()
    if args.command=="self-test":return self_test()
    if args.command=="receipt":return emit_receipt()
    code,report=validate();print("PASS — execution continuity validation is GREEN" if code==0 else "FAIL — execution continuity validation is RED");print(json.dumps(report,indent=2,ensure_ascii=False));return code
if __name__=="__main__":sys.exit(main())
