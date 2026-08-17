from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / 'tools' / 'build_v21_canonical.py'

CSS_MARK = '/* MAXESS-AAA-CONSOLIDATED-CSS */'
JS_MARK = '/* MAXESS-AAA-CONSOLIDATED-JS */'

CSS = r'''
/* MAXESS-AAA-CONSOLIDATED-CSS */
#maxess-results-10.v21-canonical .v21-aaa-fingerprint{display:grid;grid-template-columns:minmax(260px,.9fr) minmax(0,1.1fr);gap:34px;align-items:center;margin-top:30px;padding:26px;border-radius:34px;background:linear-gradient(145deg,rgba(155,99,255,.10),rgba(255,255,255,.78));border:1px solid rgba(80,45,120,.12);box-shadow:0 30px 90px rgba(30,15,50,.12)}
#maxess-results-10.v21-canonical .v21-fingerprint-visual{position:relative;aspect-ratio:1;display:grid;place-items:center}
#maxess-results-10.v21-canonical .v21-fingerprint-visual svg{width:100%;height:100%;overflow:visible}
#maxess-results-10.v21-canonical .v21-fp-core{position:absolute;inset:0;display:grid;place-items:center;text-align:center;pointer-events:none}
#maxess-results-10.v21-canonical .v21-fp-core b{display:block;font-size:clamp(54px,8vw,92px);line-height:.8;letter-spacing:-.08em;color:#17131d}
#maxess-results-10.v21-canonical .v21-fp-core span{display:block;margin-top:12px;font-size:9px;font-weight:950;letter-spacing:.18em;text-transform:uppercase;color:#7445ad}
#maxess-results-10.v21-canonical .v21-fp-reading{display:grid;gap:12px}
#maxess-results-10.v21-canonical .v21-fp-reading .v21-card{padding:20px;background:#fff}
#maxess-results-10.v21-canonical .v21-aaa-naya-note{display:grid;grid-template-columns:auto 1fr;gap:14px;align-items:start;margin-top:24px;padding:18px 20px;border-radius:24px;background:linear-gradient(135deg,rgba(155,99,255,.10),rgba(255,255,255,.92));border:1px solid rgba(115,68,170,.14);box-shadow:0 18px 45px rgba(35,18,60,.10)}
#maxess-results-10.v21-canonical .v21-aaa-naya-note img{width:52px;height:52px;border-radius:50%;object-fit:cover;border:2px solid #fff;box-shadow:0 8px 22px rgba(30,15,50,.18)}
#maxess-results-10.v21-canonical .v21-aaa-naya-note b{display:block;font-size:9px;letter-spacing:.15em;text-transform:uppercase;color:#7445ad}
#maxess-results-10.v21-canonical .v21-aaa-naya-note strong{display:block;margin-top:4px;font-size:17px;color:#17131d}
#maxess-results-10.v21-canonical .v21-aaa-naya-note p{margin:6px 0 0;color:#5d5764;font-size:14px;line-height:1.55}
#maxess-results-10.v21-canonical .v21-aaa-orb-live{animation:v21AaaOrb 7s ease-in-out infinite}
#maxess-results-10.v21-canonical .v21-masters .v21-master{position:relative;overflow:hidden;transition:transform .2s ease,box-shadow .2s ease,border-color .2s ease}
#maxess-results-10.v21-canonical .v21-masters .v21-master:hover{transform:translateY(-5px);box-shadow:0 28px 60px rgba(0,0,0,.25);border-color:rgba(201,166,255,.42)}
#maxess-results-10.v21-canonical .v21-master-match{display:inline-flex;margin-bottom:10px;padding:6px 9px;border-radius:999px;background:rgba(202,168,255,.12);border:1px solid rgba(202,168,255,.22);color:#e4d2ff;font-size:8px;font-weight:950;letter-spacing:.12em;text-transform:uppercase}
#maxess-results-10.v21-canonical .v21-media-section{position:relative;overflow:hidden}
#maxess-results-10.v21-canonical .v21-media-host{display:grid;gap:18px;margin-top:28px}
#maxess-results-10.v21-canonical .v21-media-host>section,#maxess-results-10.v21-canonical .v21-media-host>.mx-reading,#maxess-results-10.v21-canonical .v21-media-host>.mx-section{margin:0!important;max-width:none!important;width:100%!important}
#maxess-results-10.v21-canonical .v21-aaa-pulse{box-shadow:inset 0 0 80px rgba(155,99,255,.16),0 30px 100px rgba(0,0,0,.52),0 0 100px var(--v21-orb-color,rgba(155,99,255,.14))}
@keyframes v21AaaOrb{0%,100%{transform:scale(1);filter:saturate(1)}50%{transform:scale(1.012);filter:saturate(1.08)}}
@media(max-width:820px){#maxess-results-10.v21-canonical .v21-aaa-fingerprint{grid-template-columns:1fr}}
@media(prefers-reduced-motion:reduce){#maxess-results-10.v21-canonical .v21-aaa-orb-live{animation:none!important}}
@media print{#maxess-results-10.v21-canonical .v21-aaa-naya-note,#maxess-results-10.v21-canonical .v21-aaa-fingerprint{break-inside:avoid;page-break-inside:avoid}.v21-media-section .v21-media-host{display:block}}
'''

JS = r'''
/* MAXESS-AAA-CONSOLIDATED-JS */
  function aaaScoreColor(value){
    var s=Math.max(0,Math.min(100,Number(value)||0));
    var h=178+(s*1.05), l=55+(s*.10);
    return 'hsl('+h.toFixed(0)+' 78% '+l.toFixed(0)+'%)';
  }
  function aaaNayaNote(title,body){
    var el=document.createElement('div');
    el.className='v21-aaa-naya-note';
    el.innerHTML='<img src="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg" alt="Naya, your AI guide"><div><b>Naya · your guide</b><strong>'+escapeHtml(title)+'</strong><p>'+escapeHtml(body)+'</p></div>';
    return el;
  }
  function aaaFingerprint(ds,total){
    var wrap=document.createElement('section');
    wrap.className='v21-section v21-light v21-aaa-fingerprint-section';
    wrap.innerHTML='<div class="v21-inner"><span class="v21-kicker" style="color:#7445ad">YOUR AI FINGERPRINT</span><h2 class="v21-section-title">See the shape of your capability.</h2><p class="v21-section-copy">Your five dimensions are not isolated scores. Their shape shows how your strengths and opportunities work together.</p><div class="v21-aaa-fingerprint"><div class="v21-fingerprint-visual"><svg viewBox="0 0 430 430" role="img" aria-label="Your five-dimension AI capability fingerprint"><defs><radialGradient id="v21FpFill"><stop offset="0" stop-color="#9b63ff" stop-opacity=".38"/><stop offset="1" stop-color="#44d9ce" stop-opacity=".10"/></radialGradient></defs><g class="v21-fp-grid">'+[1,2,3,4].map(function(k){var rr=42*k;var pts=[];for(var i=0;i<5;i++){var a=-Math.PI/2+i*Math.PI*2/5;pts.push((215+Math.cos(a)*rr)+','+(215+Math.sin(a)*rr))}return '<polygon points="'+pts.join(' ')+'" fill="none" stroke="rgba(30,20,40,.12)"/>';}).join('')+'</g><g>'+ds.map(function(d,i){var a=-Math.PI/2+i*Math.PI*2/5;return '<line x1="215" y1="215" x2="'+(215+Math.cos(a)*168)+'" y2="'+(215+Math.sin(a)*168)+'" stroke="rgba(30,20,40,.10)"/>';}).join('')+'</g><polygon points="'+ds.map(function(d,i){var a=-Math.PI/2+i*Math.PI*2/5,r=168*(Number(d.score)||0)/100;return (215+Math.cos(a)*r)+','+(215+Math.sin(a)*r)}).join(' ')+'" fill="url(#v21FpFill)" stroke="#7445ad" stroke-width="3"/><g>'+ds.map(function(d,i){var a=-Math.PI/2+i*Math.PI*2/5,r=168*(Number(d.score)||0)/100;return '<circle cx="'+(215+Math.cos(a)*r)+'" cy="'+(215+Math.sin(a)*r)+'" r="7" fill="'+aaaScoreColor(d.score)+'" stroke="#fff" stroke-width="3"/>';}).join('')+'</g></svg><div class="v21-fp-core"><b>'+Math.round(total)+'</b><span>MAXESS SCORE</span></div></div><div class="v21-fp-reading">'+ds.map(function(d){return '<div class="v21-card"><span class="v21-kicker" style="color:#7445ad">'+escapeHtml(d.name)+'</span><h3 style="font-size:34px;margin-top:7px">'+Math.round(d.score||0)+'</h3><p style="margin-top:6px">'+escapeHtml(d.description||dimCopy(d.name,d.score))+'</p></div>';}).join('')+'</div></div></div></section>';
    return wrap;
  }
  function aaaEnhance(r,ds,strongest,lowest,preservedPlay,preservedMedia){
    var scoreValue=score(r)||0;
    var sections=[].slice.call(root.querySelectorAll('.v21-section'));
    var dimSection=sections.find(function(s){return (s.textContent||'').indexOf('YOUR FIVE DIMENSIONS')>=0});
    if(dimSection && !root.querySelector('.v21-aaa-fingerprint-section')) dimSection.parentNode.insertBefore(aaaFingerprint(ds,scoreValue),dimSection);
    var orb=root.querySelector('.v21-score-orb');
    if(orb){orb.classList.add('v21-aaa-orb-live','v21-aaa-pulse');orb.style.setProperty('--v21-orb-color',aaaScoreColor(scoreValue));orb.style.borderColor=aaaScoreColor(scoreValue)}
    var report=root.querySelector('.v21-report');if(report&&!report.querySelector('.v21-aaa-naya-note'))report.appendChild(aaaNayaNote('Here is the part I want you to notice.', 'Your score tells you where you are. The pattern, strength and lever tell you what to do with that information.'));
    var pattern=sections.find(function(s){return (s.textContent||'').indexOf('YOUR PATTERN')>=0});if(pattern&&!pattern.querySelector('.v21-aaa-naya-note'))pattern.appendChild(aaaNayaNote('Your pattern is the story between the numbers.', 'Look for the capability that is naturally supporting the others—and the one that, when strengthened, could change the shape of the whole profile.'));
    var strength=sections.find(function(s){return (s.textContent||'').indexOf('YOUR STRENGTH')>=0});if(strength&&!strength.querySelector('.v21-aaa-naya-note'))strength.appendChild(aaaNayaNote('Protect what is already working.', 'Your strongest capability is a resource. The goal is not to admire it; the goal is to compound it until it becomes leverage.'));
    var lever=sections.find(function(s){return (s.textContent||'').indexOf('YOUR LEVER')>=0});if(lever&&!lever.querySelector('.v21-aaa-naya-note'))lever.appendChild(aaaNayaNote('This is an opportunity, not a verdict.', 'The lowest dimension is simply the clearest place to focus. One deliberate improvement here can create a disproportionate return.'));
    var next=sections.find(function(s){return (s.textContent||'').indexOf('YOUR NEXT MOVE')>=0});if(next&&!next.querySelector('.v21-aaa-naya-note'))next.appendChild(aaaNayaNote('Small actions beat abstract ambition.', 'Protect your strength. Build your lever. Then create, score and improve one real AI workflow.'));
    var mastersSection=sections.find(function(s){return (s.textContent||'').indexOf('18 NAYA MASTERS')>=0});
    if(mastersSection){var cards=[].slice.call(mastersSection.querySelectorAll('.v21-master'));cards.forEach(function(card){var txt=(card.textContent||'').toLowerCase(),rel=0;if(txt.indexOf(String(lowest.name||'').toLowerCase())>=0)rel+=60;if(txt.indexOf(String(strongest.name||'').toLowerCase())>=0)rel+=35;if(/practice|workflow|prompt|system|evaluation|communication/.test(txt))rel+=5;card.dataset.v21Relevance=String(rel)});cards.sort(function(a,b){return Number(b.dataset.v21Relevance)-Number(a.dataset.v21Relevance)}).forEach(function(card,i){var pill=card.querySelector('.v21-master-match');if(pill)pill.remove();if(i<3){var p=document.createElement('span');p.className='v21-master-match';p.textContent=i===0?'BEST MATCH':'STRONG MATCH';card.insertBefore(p,card.firstChild)}mastersSection.querySelector('.v21-masters').appendChild(card)})}
    var host=document.createElement('section');host.className='v21-section v21-dark v21-media-section';host.innerHTML='<div class="v21-inner"><span class="v21-kicker">NAYA · IN PRACTICE</span><h2 class="v21-section-title">Turn insight into experience.</h2><p class="v21-section-copy">Use the existing walkthrough, video and working controls here. Nothing valuable from the original experience should disappear.</p><div class="v21-media-host"></div></div>';
    var playground=sections.find(function(s){return (s.textContent||'').indexOf('PLAYGROUND')>=0});if(playground&&!root.querySelector('.v21-media-section'))playground.parentNode.insertBefore(host,playground);
    var mediaHost=root.querySelector('.v21-media-host');if(mediaHost){if(preservedPlay)mediaHost.appendChild(preservedPlay);(preservedMedia||[]).forEach(function(n){if(n&&n.parentNode!==mediaHost)mediaHost.appendChild(n)})}
    var listens=root.querySelectorAll('.v21-listen');for(var i=listens.length-1;i>0;i--)listens[i].remove();
  }
'''

def replace_once(text, pattern, replacement, label):
    new, n = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if n != 1:
        raise SystemExit(f'{label}: matched {n}')
    return new

s = BUILDER.read_text(encoding='utf-8')
if JS_MARK not in s:
    s = replace_once(s, r'(?m)^JS\s*=\s*(r?)"""', lambda m: 'JS = r"""', 'JS RAW STRING')
    s = replace_once(s, r'function stage\(s\)\{.*?(?=function dimCopy)', """function stage(s){\n    if(s==null) return '';\n    return s>=91?'Mastering':s>=76?'Advancing':s>=51?'Developing':s>=21?'Foundation':'Supporting';\n  }\n  """, 'STAGE MODEL')
    s = s.replace("Math.round(s)+' / 100</b>", "Math.round(s)+'</b>")
    s = s.replace("Math.round(d.score||0)+' / 100</b>", "Math.round(d.score||0)+'</b>")
    s = s.replace("Math.round(d.score||0)+' / 100</b>", "Math.round(d.score||0)+'</b>")
    s = replace_once(s, r'(</style>)', lambda m: CSS + '\n' + m.group(1), 'AAA CSS')
    s = replace_once(s, r'(function build\(r\)\{)', lambda m: JS + '\n  ' + m.group(1), 'AAA JS')
    s = replace_once(s, r'(function build\(r\)\{\n\s*var s=score\(r\), ds=dimensions\(r\), name=person\(r\), st=stage\(s\);)', lambda m: m.group(1)+"\n    var preservedPlay=document.getElementById('naya-playground');\n    var preservedMedia=[];\n    root.querySelectorAll('video,iframe[src*=youtube],iframe[src*=vimeo],audio').forEach(function(media){var holder=media.closest('section,.mx-section,.mx-reading,.mx-wide')||media.parentElement;if(holder&&holder!==root&&!preservedMedia.includes(holder)&&!(preservedPlay&&holder.contains(preservedPlay)))preservedMedia.push(holder)});", 'MEDIA SNAPSHOT')
    s = replace_once(s, r"(root\.setAttribute\('data-results-version','v21-canonical'\);root\.setAttribute\('data-results-data-source','window\.MAXESS_RESULT'\);root\.setAttribute\('data-results-state','ready'\);)", lambda m: "aaaEnhance(r,ds,strongest,lowest,preservedPlay,preservedMedia);\n    "+m.group(1), 'AAA POST RENDER')
    s = replace_once(s, r"text = re\.sub\(r'<script id=\"maxess-results-v21-canonical-js\">.*?", lambda m: m.group(0), 'NOOP') if False else s
    # remove previously-generated Nitro block from baseline during future canonical builds
    s = replace_once(s, r"def remove_old_v21\(text: str\) -> str:\n", "def remove_old_v21(text: str) -> str:\n", 'REMOVE OLD FUNCTION')
    marker = "    text = re.sub(r'<!-- MAXESS-NITRO-AAA-UPGRADE v3 -->.*?<!-- /MAXESS-NITRO-AAA-UPGRADE -->\\s*', '', text, flags=re.S)\n"
    s = s.replace("def remove_old_v21(text: str) -> str:\n", "def remove_old_v21(text: str) -> str:\n"+marker, 1)
    BUILDER.write_text(s,encoding='utf-8')
    print('MAXESS AAA CONSOLIDATED EXECUTION PATCH APPLIED')
    print('Integrated: fingerprint, Naya interpretation, dynamic Masters relevance, media preservation, Orb response, lower-page hosting, five-stage mastery, /100 cleanup')
else:
    print('MAXESS AAA CONSOLIDATED PATCH ALREADY PRESENT')
