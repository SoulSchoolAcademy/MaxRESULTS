from pathlib import Path
import re

E01 = Path('E01-SECTION-01-WORKING.html')
E02 = Path('E02-SECTION-02-WORKING.html')
E03 = Path('E03-SECTION-03-WORKING.html')
E04 = Path('E04-SECTION-04-WORKING.html')
CONSUMER = Path('MAXESS-RESULT-CONSUMER-V1.html')
MARKER = 'MAXESS_RESULT_CONSUMER_V1'

# NAYA TRANSPORT REPAIR TRIGGER: execute the canonical cleanup against the current branch source.
# NORTH STAR GUARDRAIL V4: one authoritative result transport across the host page and
# Groove iframe embeds. Sections never score or invent results; they only consume the
# authoritative MAXESS_RESULT contract/events/message relay.

EMBED_MESSAGE = '''
/* MAXESS_RESULT_IFRAME_RELAY_V1 — receive the authoritative result from the host consumer. */
window.addEventListener('message',function(event){
  try{
    var data=event&&event.data;
    if(!data||data.type!=='MAXESS_RESULT_READY')return;
    var result=data.result;
    if(!result||result.contractVersion!=='MAXESS_RESULT_V1')return;
    window.MAXESS_RESULT=result;
    try{sessionStorage.setItem('MAXESS_RESULT_V1',JSON.stringify(result));}catch(e){}
    try{localStorage.setItem('MAXESS_RESULT_V1',JSON.stringify(result));}catch(e){}
    window.dispatchEvent(new CustomEvent('MAXESS_RESULT_READY',{detail:result}));
    window.dispatchEvent(new CustomEvent('maxess:result-updated',{detail:result}));
  }catch(e){}
});
'''


def strip_e01_consumer(s):
    pattern = r'<script[^>]*id=["\']MAXESS_RESULT_CONSUMER_V1["\'][^>]*>.*?</script>\s*'
    out, n = re.subn(pattern, '', s, count=1, flags=re.S | re.I)
    if n > 1:
        raise SystemExit('E01 consumer duplication: more than one embedded consumer found')
    return out


def strip_e01_text_fallback(s):
    old = """function getScore(){var sources=[];try{sources.push(window.MAXESS_RESULT)}catch(e){}try{if(window.parent&&window.parent!==window)sources.push(window.parent.MAXESS_RESULT)}catch(e){}try{if(window.top&&window.top!==window&&window.top!==window.parent)sources.push(window.top.MAXESS_RESULT)}catch(e){}for(var i=0;i<sources.length;i++){var r=sources[i];if(r&&typeof r==='object'){var s=clamp(r.overallScore);if(s!==null)return s}}var docs=[document];try{if(window.parent&&window.parent!==window)docs.push(window.parent.document)}catch(e){}for(var d=0;d<docs.length;d++){try{var text=(docs[d].body&&docs[d].body.innerText)||'';var m=text.match(/(?:^|\\n)\\s*(\\d+(?:\\.\\d+)?)\\s*(?:MAXESS\\s+SCORE|overall)\\b/i);if(m){var parsed=clamp(m[1]);if(parsed!==null)return parsed}}catch(e){}}return null}"""
    new = """function getScore(){var sources=[];try{sources.push(window.MAXESS_RESULT)}catch(e){}try{if(window.parent&&window.parent!==window)sources.push(window.parent.MAXESS_RESULT)}catch(e){}try{if(window.top&&window.top!==window&&window.top!==window.parent)sources.push(window.top.MAXESS_RESULT)}catch(e){}for(var i=0;i<sources.length;i++){var r=sources[i];if(r&&typeof r==='object'){var s=clamp(r.overallScore);if(s!==null)return s}}return null}"""
    if old not in s:
        raise SystemExit('E01 authoritative score reader pattern not found; refusing speculative mutation')
    return s.replace(old, new, 1)


def strip_e02_transport(s):
    start = s.find('function decodeResultPayload(payload){')
    mid = s.find('function render(){', start)
    if start < 0 or mid < 0:
        raise SystemExit('E02 transport block boundaries not found; refusing speculative mutation')
    s = s[:start] + s[mid:]
    s = s.replace("hydrateFromHash()||hydrateFromStorage();\n", "", 1)
    s = re.sub(r"window\.addEventListener\('hashchange',\(\)=>\{if\(hydrateFromHash\(\)\)render\(\)\}\);\n", '', s, count=1)
    s = re.sub(r"let attempts=0;const timer=setInterval\(\(\)=>\{.*?\},250\);\n", '', s, count=1, flags=re.S)
    if 'decodeResultPayload' in s or 'hydrateFromHash' in s or 'hydrateFromStorage' in s or 'location.hash' in s:
        raise SystemExit('E02 still contains a competing result transport path')
    return s


def add_iframe_relay(s, section_name):
    marker = 'MAXESS_RESULT_IFRAME_RELAY_V1'
    if marker in s:
        return s
    idx = s.rfind('</script>')
    if idx < 0:
        raise SystemExit(f'{section_name}: no closing script tag found')
    return s[:idx] + EMBED_MESSAGE + s[idx:]


def main():
    if not CONSUMER.exists():
        raise SystemExit('Standalone MAXESS_RESULT_CONSUMER_V1 artifact is missing')
    consumer = CONSUMER.read_text(encoding='utf-8')
    if consumer.count(MARKER) != 2:
        raise SystemExit('Standalone consumer identity check failed')

    e01 = strip_e01_consumer(E01.read_text(encoding='utf-8'))
    e01 = strip_e01_text_fallback(e01)
    e02 = strip_e02_transport(E02.read_text(encoding='utf-8'))
    e03 = E03.read_text(encoding='utf-8')
    e04 = E04.read_text(encoding='utf-8')

    e01 = add_iframe_relay(e01, 'E01')
    e02 = add_iframe_relay(e02, 'E02')
    e03 = add_iframe_relay(e03, 'E03')
    e04 = add_iframe_relay(e04, 'E04')

    E01.write_text(e01, encoding='utf-8')
    E02.write_text(e02, encoding='utf-8')
    E03.write_text(e03, encoding='utf-8')
    E04.write_text(e04, encoding='utf-8')

    print('Canonical transport architecture applied: standalone consumer -> host + E01 -> E02 -> E03 -> E04')
    print('E01 bytes:', len(e01.encode('utf-8')))
    print('E02 bytes:', len(e02.encode('utf-8')))
    print('E03 bytes:', len(e03.encode('utf-8')))
    print('E04 bytes:', len(e04.encode('utf-8')))


if __name__ == '__main__':
    main()