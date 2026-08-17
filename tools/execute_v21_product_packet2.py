#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / 'tools' / 'build_v21_canonical.py'
s = BUILDER.read_text(encoding='utf-8')

# Capture legacy lower-page assets BEFORE V21 replaces the root DOM.
needle = "    var mastersList=masters();\n"
insert = r'''    var mastersList=masters();
    var legacyPlayHTML='';
    var legacyVideoHTML='';
    var legacyVideoButtonsHTML='';
    var legacyPlayNode=document.getElementById('naya-playground');
    if(legacyPlayNode) legacyPlayHTML=legacyPlayNode.outerHTML;
    var videoNode=root.querySelector('#naya-video,.v13-video,#naya-video-section,.v13-video-section,video,iframe[src*="youtube"],iframe[src*="youtu.be"]');
    if(videoNode){
      var videoSection=videoNode.closest('section,article,.v13-section,.mx-section') || videoNode;
      legacyVideoHTML=videoSection.outerHTML;
      var btns=videoSection.querySelectorAll('a,button');
      if(btns.length){ legacyVideoButtonsHTML=Array.prototype.map.call(btns,function(b){return b.outerHTML;}).join(''); }
    }
'''
if needle not in s:
    raise SystemExit('PACKET2 ASSET ANCHOR NOT FOUND')
s = s.replace(needle, insert, 1)

# Replace the Playground placeholder with a real captured payload.
old_play = "'<section class=\"v21-section v21-light\"><div class=\"v21-inner\"><span class=\"v21-kicker\" style=\"color:#7445ad\">PLAYGROUND</span><h2 class=\"v21-section-title\">Understand → Decide → Practice.</h2><div class=\"v21-playground\"><p>Turn your result into action. Take what you learned, choose one improvement, and practice it on a real task.</p><div class=\"v21-legacy-wrap\" id=\"v21-playground-host\"></div></div></div></section>'+"
new_play = "'<section class=\"v21-section v21-light\"><div class=\"v21-inner\"><span class=\"v21-kicker\" style=\"color:#7445ad\">PLAYGROUND</span><h2 class=\"v21-section-title\">Understand → Decide → Practice.</h2><div class=\"v21-playground\"><p>Turn your result into action. Take what you learned, choose one improvement, and practice it on a real task.</p><div class=\"v21-legacy-wrap\" id=\"v21-playground-host\">'+(legacyPlayHTML||'<p style=\"color:#5b5662\">Your Playground is ready for practice. Choose one improvement and try it on a real task.</p>')+'</div></div></div></section>'+"
if old_play not in s:
    raise SystemExit('PACKET2 PLAYGROUND MARKUP NOT FOUND')
s = s.replace(old_play, new_play, 1)

# Insert a V21-owned video section before the Playground.
play_anchor = "      '<section class=\"v21-section v21-light\"><div class=\"v21-inner\"><span class=\"v21-kicker\" style=\"color:#7445ad\">PLAYGROUND</span>"
video_section = "      '<section class=\"v21-section v21-dark\"><div class=\"v21-inner\"><span class=\"v21-kicker\">WATCH / LISTEN</span><h2 class=\"v21-section-title\">Continue with Naya.</h2><p class=\"v21-section-copy\">Use the video and audio experience to turn your result into understanding and action.</p><div class=\"v21-video-shell\" style=\"margin-top:28px;border-radius:28px;overflow:hidden;border:1px solid rgba(255,255,255,.13);background:#09070d;padding:14px;box-shadow:0 28px 80px rgba(0,0,0,.34)\">'+(legacyVideoHTML||'<div style=\"padding:70px 24px;text-align:center;color:rgba(255,255,255,.65)\">The Naya video will appear here when the host supplies it.</div>')+'</div>'+(legacyVideoButtonsHTML?'<div class=\"v21-three\" style=\"margin-top:18px\">'+legacyVideoButtonsHTML+'</div>':'')+'</div></section>'+\n"      '<section class=\"v21-section v21-light\"><div class=\"v21-inner\"><span class=\"v21-kicker\" style=\"color:#7445ad\">PLAYGROUND</span>"
if play_anchor not in s:
    raise SystemExit('PACKET2 PLAYGROUND ANCHOR NOT FOUND')
s = s.replace(play_anchor, video_section, 1)

# Remove the now-invalid post-render DOM move; captured HTML is already embedded.
s = re.sub(r"\n    var oldPlay=document\.getElementById\('naya-playground'\); var host=document\.getElementById\('v21-playground-host'\); if\(oldPlay && host\) host\.appendChild\(oldPlay\);", "", s, count=1)

# Add explicit V21 loading-complete marker.
marker = "    root.setAttribute('data-results-state','ready');"
replacement = "    root.setAttribute('data-results-state','ready');root.setAttribute('data-v21-lower-sections','complete');"
if marker not in s:
    raise SystemExit('PACKET2 READY MARKER NOT FOUND')
s = s.replace(marker, replacement, 1)

BUILDER.write_text(s, encoding='utf-8')
print('V21 PRODUCT PACKET 2 SOURCE PATCH COMPLETE')
print('Lower-page assets captured before root replacement')
print('V21-owned video section added')
print('Playground rendered from captured HTML with safe fallback')
print('Post-render legacy Playground move removed')
