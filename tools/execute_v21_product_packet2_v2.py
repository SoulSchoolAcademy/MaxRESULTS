#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / 'tools' / 'build_v21_canonical.py'
s = BUILDER.read_text(encoding='utf-8')

# Capture live legacy nodes before V21 replaces root.innerHTML. Detached nodes retain listeners/state.
needle = "  function build(r){\n    var s=score(r), ds=dimensions(r), name=person(r), st=stage(s);"
insert = """  function build(r){
    var legacyPlayNode = root.querySelector('#naya-playground');
    var legacyVideoNode = root.querySelector('#v13-video,.v13-video,#maxess-video,.mx-video-section,video,iframe[src*='youtube'],iframe[src*='vimeo']');
    if(legacyPlayNode && legacyPlayNode.parentNode) legacyPlayNode.parentNode.removeChild(legacyPlayNode);
    if(legacyVideoNode && legacyVideoNode.parentNode) legacyVideoNode.parentNode.removeChild(legacyVideoNode);
    var s=score(r), ds=dimensions(r), name=person(r), st=stage(s);"""
if needle not in s:
    raise SystemExit('BUILD HEADER MARKER NOT FOUND')
s = s.replace(needle, insert, 1)

# Add a V21-owned video section before Playground.
old_play = "      '<section class=\\\"v21-section v21-light\\\"><div class=\\\"v21-inner\\\"><span class=\\\"v21-kicker\\\" style=\\\"color:#7445ad\\\">PLAYGROUND</span><h2 class=\\\"v21-section-title\\\">Understand → Decide → Practice.</h2><div class=\\\"v21-playground\\\"><p>Turn your result into action. Take what you learned, choose one improvement, and practice it on a real task.</p><div class=\\\"v21-legacy-wrap\\\" id=\\\"v21-playground-host\\\"></div></div></div></section>'+"
new_play = """      '<section class=\\\"v21-section v21-dark\\\"><div class=\\\"v21-inner\\\"><span class=\\\"v21-kicker\\\">NAYA · WALKTHROUGH</span><h2 class=\\\"v21-section-title\\\">Hear the result in context.</h2><p class=\\\"v21-section-copy\\\">Use the guided Naya walkthrough to turn the report into understanding and action.</p><div class=\\\"v21-legacy-wrap\\\" id=\\\"v21-video-host\\\"></div></div></section>'+
      '<section class=\\\"v21-section v21-light\\\"><div class=\\\"v21-inner\\\"><span class=\\\"v21-kicker\\\" style=\\\"color:#7445ad\\\">PLAYGROUND</span><h2 class=\\\"v21-section-title\\\">Understand → Decide → Practice.</h2><div class=\\\"v21-playground\\\"><p>Turn your result into action. Take what you learned, choose one improvement, and practice it on a real task.</p><div class=\\\"v21-legacy-wrap\\\" id=\\\"v21-playground-host\\\"></div></div></div></section>'+"""
if old_play not in s:
    raise SystemExit('PLAYGROUND SECTION MARKER NOT FOUND')
s = s.replace(old_play, new_play, 1)

# Reattach the preserved live nodes into the V21-owned hosts after render.
old_rebind = "    var oldPlay=document.getElementById('naya-playground'); var host=document.getElementById('v21-playground-host'); if(oldPlay && host) host.appendChild(oldPlay);\n    root.setAttribute('data-results-version','v21-canonical');root.setAttribute('data-results-data-source','window.MAXESS_RESULT');root.setAttribute('data-results-state','ready');"
new_rebind = "    var playHost=root.querySelector('#v21-playground-host'); if(legacyPlayNode && playHost) playHost.appendChild(legacyPlayNode);\n    var videoHost=root.querySelector('#v21-video-host'); if(legacyVideoNode && videoHost) videoHost.appendChild(legacyVideoNode);\n    root.setAttribute('data-results-version','v21-canonical');root.setAttribute('data-results-data-source',window.MAXESS_RESULT?'window.MAXESS_RESULT':'legacy-dom-migration');root.setAttribute('data-results-state','ready');"
if old_rebind not in s:
    raise SystemExit('REATTACH MARKER NOT FOUND')
s = s.replace(old_rebind, new_rebind, 1)

# Improve lower-section styling so detached legacy content visually belongs to V21.
marker = "#maxess-results-10.v21-canonical .v21-cta-final{text-align:center}"
css = """#maxess-results-10.v21-canonical #v21-video-host{margin-top:24px;min-height:260px;border-radius:28px;overflow:hidden;background:#050307;border:1px solid rgba(255,255,255,.12);box-shadow:0 28px 75px rgba(0,0,0,.34)}
#maxess-results-10.v21-canonical #v21-video-host iframe,#maxess-results-10.v21-canonical #v21-video-host video{display:block;width:100%;min-height:420px;border:0}
#maxess-results-10.v21-canonical #v21-playground-host{margin-top:20px}
#maxess-results-10.v21-canonical #v21-playground-host > *{max-width:100%}
"""
if marker not in s:
    raise SystemExit('CSS INSERT MARKER NOT FOUND')
s = s.replace(marker, css + marker, 1)

BUILDER.write_text(s, encoding='utf-8')
print('V21 PRODUCT PACKET 2 V2 SOURCE PATCH COMPLETE')
print('Detached live legacy video/playground nodes before root replacement')
print('Reattached them into V21-owned sections after render')
print('Added dedicated V21 walkthrough section')
print('Added lower-section containment styling')
