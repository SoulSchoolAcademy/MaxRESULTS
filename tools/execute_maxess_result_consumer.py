from pathlib import Path

TARGET = Path('E01-SECTION-01-WORKING.html')
MARKER = 'MAXESS_RESULT_CONSUMER_V1'

BOOTSTRAP = r'''
<script id="MAXESS_RESULT_CONSUMER_V1">
(function(){
  'use strict';
  const KEY = 'MAXESS_RESULT_V1';
  function decode(value){
    try{
      const normalized = value.replace(/-/g,'+').replace(/_/g,'/');
      const padded = normalized + '='.repeat((4-normalized.length%4)%4);
      const binary = atob(padded);
      const bytes = Uint8Array.from(binary, c=>c.charCodeAt(0));
      return JSON.parse(new TextDecoder().decode(bytes));
    }catch(e){ return null; }
  }
  function readHash(){
    const match = location.hash.match(/(?:^|#)maxess-result=([^&]+)/);
    return match ? decode(match[1]) : null;
  }
  function readStorage(){
    try{
      const raw = sessionStorage.getItem(KEY) || localStorage.getItem(KEY);
      return raw ? JSON.parse(raw) : null;
    }catch(e){ return null; }
  }
  function valid(result){
    return !!(
      result &&
      result.contractVersion === 'MAXESS_RESULT_V1' &&
      Number.isFinite(Number(result.overallScore)) &&
      Array.isArray(result.dimensions) && result.dimensions.length === 5 &&
      Array.isArray(result.responses) && result.responses.length === 15
    );
  }
  const result = readHash() || readStorage();
  if(valid(result)){
    window.MAXESS_RESULT = result;
    try{ sessionStorage.setItem(KEY, JSON.stringify(result)); }catch(e){}
    try{ localStorage.setItem(KEY, JSON.stringify(result)); }catch(e){}
    window.dispatchEvent(new CustomEvent('MAXESS_RESULT_READY',{detail:result}));
    window.dispatchEvent(new CustomEvent('maxess:result-updated',{detail:result}));
  }
})();
</script>
'''

s = TARGET.read_text(encoding='utf-8')
if MARKER not in s:
    head = s.lower().find('</head>')
    if head < 0:
        raise SystemExit('E01 consumer: closing head tag missing')
    s = s[:head] + BOOTSTRAP + '\n' + s[head:]

# Remove the visual-review demo fallback. A missing contract must remain a safe missing-result state.
s = s.replace("var DEMO_SCORE=82; /* VISUAL REVIEW ONLY: real MAXESS_RESULT.overallScore replaces this automatically when connected. */", "var DEMO_SCORE=null; /* Production safety: no invented result. */")
s = s.replace("if(s===null){scoreNode.textContent=formatScore(DEMO_SCORE);scoreNode.dataset.hydrated='true';scoreNode.dataset.demo='true';applyPalette(DEMO_SCORE);scoreDescription.textContent='Preview score '+formatScore(DEMO_SCORE)+' of 100. A live MAXESS result will replace this demo value automatically.';liveNode.textContent='Preview score '+formatScore(DEMO_SCORE)+' of 100. A live MAXESS result will replace this demo value automatically.';unavailableNode.dataset.visible='false';return}", "if(s===null){scoreNode.textContent='';scoreNode.dataset.hydrated='false';scoreNode.dataset.demo='false';unavailableNode.dataset.visible='true';scoreDescription.textContent='MAXESS has not received a valid result yet.';liveNode.textContent='MAXESS has not received a valid result yet.';return}")

TARGET.write_text(s, encoding='utf-8')
print('patched Results consumer:', len(s.encode('utf-8')), 'bytes')
