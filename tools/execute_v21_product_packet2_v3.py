#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / 'tools' / 'build_v21_canonical.py'
s = BUILDER.read_text(encoding='utf-8')

# Snapshot live lower-page assets before root.innerHTML replaces the legacy DOM.
build_header = re.compile(r"function build\(r\)\{\s*", re.S)
match = build_header.search(s)
if not match:
    raise SystemExit('BUILD FUNCTION NOT FOUND')
insert = '''function build(r){
    var legacyPlayNode = root.querySelector('#naya-playground');
    var legacyVideoAnchor = root.querySelector('video,iframe[src*="youtube"],iframe[src*="vimeo"],[class*="video"]');
    var legacyVideoNode = legacyVideoAnchor ? (legacyVideoAnchor.closest ? (legacyVideoAnchor.closest('section') || legacyVideoAnchor.parentNode) : legacyVideoAnchor.parentNode) : null;
    if(legacyPlayNode && legacyPlayNode.parentNode) legacyPlayNode.parentNode.removeChild(legacyPlayNode);
    if(legacyVideoNode && legacyVideoNode !== root && legacyVideoNode.parentNode) legacyVideoNode.parentNode.removeChild(legacyVideoNode);
'''
s = s[:match.start()] + insert + s[match.end():]

# Replace the existing Playground section with V21-owned walkthrough + Playground sections.
play_pattern = re.compile(
    r"\s*'<section class=\\\"v21-section v21-light\\\"><div class=\\\"v21-inner\\\"><span class=\\\"v21-kicker\\\" style=\\\"color:#7445ad\\\">PLAYGROUND</span>.*?</section>'\+",
    re.S,
)
play_replacement = '''
      '<section class=\\"v21-section v21-dark\\"><div class=\\"v21-inner\\"><span class=\\"v21-kicker\\">NAYA · WALKTHROUGH</span><h2 class=\\"v21-section-title\\">Hear the result in context.</h2><p class=\\"v21-section-copy\\">Use the guided Naya experience to turn the report into understanding and action.</p><div class=\\"v21-legacy-wrap\\" id=\\"v21-video-host\\"></div></div></section>'+\n
      '<section class=\\"v21-section v21-light\\"><div class=\\"v21-inner\\"><span class=\\"v21-kicker\\" style=\\"color:#7445ad\\">PLAYGROUND</span><h2 class=\\"v21-section-title\\">Understand → Decide → Practice.</h2><div class=\\"v21-playground\\"><p>Turn your result into action. Take what you learned, choose one improvement, and practice it on a real task.</p><div class=\\"v21-legacy-wrap\\" id=\\"v21-playground-host\\"></div></div></div></section>'+'''
s2, n = play_pattern.subn(play_replacement, s, count=1)
if n != 1:
    raise SystemExit(f'PLAYGROUND SECTION PATCH FAILED: {n}')
s = s2

# Replace the legacy post-render rebind with preserved-node reattachment.
rebind_pattern = re.compile(
    r"\s*var oldPlay=.*?root\.setAttribute\('data-results-state','ready'\);",
    re.S,
)
rebind_replacement = """
    var playHost=root.querySelector('#v21-playground-host');
    if(legacyPlayNode && playHost) playHost.appendChild(legacyPlayNode);
    var videoHost=root.querySelector('#v21-video-host');
    if(legacyVideoNode && videoHost) videoHost.appendChild(legacyVideoNode);
    root.setAttribute('data-results-version','v21-canonical');
    root.setAttribute('data-results-data-source',window.MAXESS_RESULT?'window.MAXESS_RESULT':'legacy-dom-migration');
    root.setAttribute('data-results-state','ready');"""
s2, n = rebind_pattern.subn(lambda _m: rebind_replacement, s, count=1)
if n != 1:
    raise SystemExit(f'REBIND PATCH FAILED: {n}')
s = s2

# Add robust containment styling once.
marker = "#maxess-results-10.v21-canonical .v21-cta-final{text-align:center}"
if marker not in s:
    raise SystemExit('CSS INSERT MARKER NOT FOUND')
css = """#maxess-results-10.v21-canonical #v21-video-host{margin-top:24px;min-height:260px;border-radius:28px;overflow:hidden;background:#050307;border:1px solid rgba(255,255,255,.12);box-shadow:0 28px 75px rgba(0,0,0,.34)}
#maxess-results-10.v21-canonical #v21-video-host iframe,#maxess-results-10.v21-canonical #v21-video-host video{display:block;width:100%;min-height:420px;border:0}
#maxess-results-10.v21-canonical #v21-playground-host{margin-top:20px}
#maxess-results-10.v21-canonical #v21-playground-host > *{max-width:100%}
"""
s = s.replace(marker, css + marker, 1)

BUILDER.write_text(s, encoding='utf-8')
print('V21 PRODUCT PACKET 2 V3 SOURCE PATCH COMPLETE')
print('Structural build targeting: PASS')
print('Legacy video/playground snapshot before root replacement: PASS')
print('V21-owned reattachment: PASS')
print('Walkthrough + Playground sections: PASS')
