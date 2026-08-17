#!/usr/bin/env python3
from pathlib import Path
import re, hashlib, subprocess, tempfile

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'20260817 912am RESULTS PAGE CODE'
REPORT=ROOT/'docs/RECOGNITION-FLOW-10-4-FIX.md'


def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def extract(text, sid):
    m=re.search(r'<script[^>]*id=["\']'+re.escape(sid)+r'["\'][^>]*>(.*?)</script>', text, re.I|re.S)
    return m

def main():
    if not SRC.exists(): print('ERROR: source missing'); return 2
    text=SRC.read_text(encoding='utf-8')
    sid='maxess-recognition-flow-10-4-js'
    m=extract(text,sid)
    if not m: print('ERROR: target script not found'); return 3
    old=m.group(1)
    marker='function addStyle(){'
    a=old.find(marker); b=old.find('\n  function resultData()',a)
    if a<0 or b<0: print('ERROR: addStyle boundaries not found'); return 4
    replacement="function addStyle(){\n    // CSS is already present in the adjacent canonical <style id=\"maxess-recognition-flow-10-4\"> block.\n    // Do not inject raw CSS as JavaScript; doing so creates a syntax error and duplicates the stylesheet.\n  }"
    new=old[:a]+replacement+old[b:]
    candidate=text[:m.start(1)]+new+text[m.end(1):]
    cm=extract(candidate,sid)
    script=cm.group(1)
    with tempfile.NamedTemporaryFile('w',suffix='.js',delete=False,encoding='utf-8') as f:
        f.write(script); p=f.name
    proc=subprocess.run(['node','--check',p],capture_output=True,text=True)
    Path(p).unlink(missing_ok=True)
    if proc.returncode!=0:
        print('ERROR: target script still fails syntax validation')
        print(proc.stderr); return 5
    SRC.write_text(candidate,encoding='utf-8')
    REPORT.write_text('# Recognition Flow 10.4 Fix\n\nRemoved the invalid runtime CSS injection from `maxess-recognition-flow-10-4-js`. The canonical stylesheet remains intact; the target script now passes Node syntax validation.\n\nSource SHA-256: `'+sha(SRC)+'`\n',encoding='utf-8')
    print('RECOGNITION FLOW 10.4 FIX APPLIED')
    print('TARGET SCRIPT SYNTAX: PASS')
    print('Source SHA-256:',sha(SRC))
    return 0

if __name__=='__main__': raise SystemExit(main())
