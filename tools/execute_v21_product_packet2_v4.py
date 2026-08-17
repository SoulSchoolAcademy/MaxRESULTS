#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / 'tools' / 'build_v21_canonical.py'
s = BUILDER.read_text(encoding='utf-8')

# Capture live lower-page nodes before the canonical root is replaced.
build_anchor = '  function build(r){'
if build_anchor not in s:
    raise SystemExit('BUILD FUNCTION NOT FOUND')

capture = '''  function build(r){
    var legacyPlayNode=root.querySelector('#naya-playground');
    var legacyVideoNode=root.querySelector('video,iframe[src*="youtube"],iframe[src*="vimeo"],[class*="video"]');
'''
s = s.replace(build_anchor, capture, 1)

# Add a dedicated V21 video host immediately before the existing Playground host.
play_host = '<div class="v21-legacy-wrap" id="v21-playground-host"></div>'
if play_host not in s:
    raise SystemExit('PLAYGROUND HOST NOT FOUND')
video_host = '<div class="v21-legacy-wrap" id="v21-video-host"></div>'
s = s.replace(play_host, video_host + play_host, 1)

# Reattach preserved nodes after the canonical HTML is rendered.
rebind_anchor = "    var btn=root.querySelector('.v21-listen');"
if rebind_anchor not in s:
    raise SystemExit('POST-RENDER ANCHOR NOT FOUND')
rebind = '''    var videoHost=root.querySelector('#v21-video-host');
    if(legacyVideoNode && videoHost) videoHost.appendChild(legacyVideoNode);
    var playHost=root.querySelector('#v21-playground-host');
    if(legacyPlayNode && playHost) playHost.appendChild(legacyPlayNode);
'''
s = s.replace(rebind_anchor, rebind + rebind_anchor, 1)

# Add robust lower-content styling once in the canonical CSS payload.
css_anchor = '#maxess-results-10.v21-canonical .v21-cta-final{text-align:center}'
if css_anchor not in s:
    raise SystemExit('CSS ANCHOR NOT FOUND')
css = '''#maxess-results-10.v21-canonical #v21-video-host{margin-top:24px;min-height:260px;border-radius:28px;overflow:hidden;background:#050307;border:1px solid rgba(255,255,255,.12);box-shadow:0 28px 75px rgba(0,0,0,.34)}
#maxess-results-10.v21-canonical #v21-video-host iframe,#maxess-results-10.v21-canonical #v21-video-host video{display:block;width:100%;min-height:420px;border:0}
#maxess-results-10.v21-canonical #v21-playground-host{margin-top:20px}
#maxess-results-10.v21-canonical #v21-playground-host > *{max-width:100%}
'''
s = s.replace(css_anchor, css + css_anchor, 1)

BUILDER.write_text(s, encoding='utf-8')
print('V21 PRODUCT PACKET 2 V4 SOURCE PATCH COMPLETE')
print('Captured legacy video/playground nodes before root replacement')
print('Added V21 video host beside Playground host')
print('Reattached preserved nodes after canonical render')
print('Added lower-content containment styling')
