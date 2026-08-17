#!/usr/bin/env python3
from pathlib import Path
import re, urllib.request
ROOT=Path(__file__).resolve().parents[1]
RESULTS=ROOT/'20260817 912am RESULTS PAGE CODE'
REPORT=ROOT/'V21-SYSTEM-FLOW-QA.md'
URL='https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/CURRENT%20WORKING%20FILE'
fail=[]; warn=[]
rt=RESULTS.read_text(encoding='utf-8') if RESULTS.exists() else ''
if not RESULTS.exists(): fail.append('Results authoritative source file not found')
for t,l in [('window.MAXESS_RESULT','Results consumes window.MAXESS_RESULT'),('function result()','result resolver'),('Array.isArray(r.dimensions)','dimension normalization'),('list.slice(0,5)','five-dimension constraint'),("data-results-state','awaiting'",'safe missing-data state'),("data-results-state','ready'",'ready state')]:
    if t not in rt: fail.append('missing Results contract behavior: '+l)
for t,l in [('YOUR RESULT','result section'),('YOUR FIVE DIMENSIONS','dimensions section'),('YOUR PERSONALIZED REPORT','report section'),('YOUR PATTERN','pattern section'),('YOUR STRENGTH','strength section'),('YOUR LEVER','lever section'),('YOUR NEXT MOVE','next move section'),('18 NAYA MASTERS','masters section'),('PLAYGROUND','playground section'),('LISTEN TO NAYA','Naya CTA')]:
    if t not in rt: fail.append('missing Results experience element: '+l)
assessment=''
try:
    with urllib.request.urlopen(URL,timeout=20) as r: assessment=r.read().decode('utf-8','replace')
except Exception as e: warn.append('could not fetch Assessment source: '+type(e).__name__)
if assessment:
    qnums=set(int(x) for x in re.findall(r'question\s*([0-9]{1,2})',assessment,re.I))
    qnums |= set(int(x) for x in re.findall(r'Q(?:uestion)?[_ -]?([0-9]{1,2})',assessment,re.I))
    if len([n for n in qnums if 1<=n<=15])<15: warn.append('could not prove all 15 assessment questions statically')
    low=assessment.lower()
    if 'maxess_result' not in low and 'result contract' not in low: warn.append('Assessment source lacks explicit Result Contract/MAXESS_RESULT evidence')
    if not re.search(r'results(?:\.nayanet\.xyz)?',assessment,re.I): warn.append('Assessment source lacks visible Results destination evidence')
for a in ['overallScore','masterScore','score','overall']:
    if a in rt: break
else: fail.append('Results lacks accepted overall score field')
if 'dimensions' not in rt: fail.append('Results lacks dimensions contract field')
if 'This page does not invent a score when real result data is unavailable.' not in rt: fail.append('Results lacks no-fabrication safety message')
report=['# MAXESS V21 — SYSTEM FLOW QA','', '- Journey: `nayanet.xyz → maxess.nayanet.xyz → results.nayanet.xyz`','- Contract: `15 answers → Result Contract → window.MAXESS_RESULT → Results`','',f'- Results source lines: `{len(rt.splitlines())}`',f'- Assessment fetched: `{"YES" if assessment else "NO"}`',f'- Failures: `{len(fail)}`',f'- Warnings: `{len(warn)}`','', '## Failures']
report += [f'- {x}' for x in fail] if fail else ['- NONE']
report += ['', '## Warnings']+[f'- {x}' for x in warn] if warn else ['- NONE']
report += ['', '## Gate', 'PASS' if not fail else 'FAIL','']
REPORT.write_text('\n'.join(report),encoding='utf-8')
for x in fail: print('FAIL:',x)
for x in warn: print('WARN:',x)
print(f'Results source lines: {len(rt.splitlines())}')
print(f'Assessment source fetched: {"YES" if assessment else "NO"}')
print(f'FAILURES: {len(fail)}'); print(f'WARNINGS: {len(warn)}')
print('V21 SYSTEM FLOW QA PASS' if not fail else 'V21 SYSTEM FLOW QA FAIL')
raise SystemExit(0 if not fail else 5)
