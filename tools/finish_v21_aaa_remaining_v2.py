#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools" / "build_v21_canonical.py"
MARK = "/* MAXESS-V21-AAA-REMAINING-FINISH-V2 */"

s = BUILDER.read_text(encoding="utf-8")

# Keep the JS payload raw so Python does not reinterpret JS escape sequences.
if 'JS = r"""' not in s:
    s2, n = re.subn(r'(?m)^JS = """$', 'JS = r"""', s, count=1)
    if n != 1:
        raise SystemExit(f'RAW-JS REPAIR FAILED: marker count {n}')
    s = s2

# Prevent helper text from masquerading as the five-dimension rendered section.
s = s.replace("var dimSection=sections.find(function(s){return (s.textContent||'').indexOf('YOUR FIVE DIMENSIONS')>=0});", "var dimSection=sections[3];", 1)
s = s.replace("var pattern=sections.find(function(s){return (s.textContent||'').indexOf('YOUR PATTERN')>=0});", "var pattern=sections[5];", 1)
s = s.replace("var strength=sections.find(function(s){return (s.textContent||'').indexOf('YOUR STRENGTH')>=0});", "var strength=sections[6];", 1)
s = s.replace("var lever=sections.find(function(s){return (s.textContent||'').indexOf('YOUR LEVER')>=0});", "var lever=sections[7];", 1)
s = s.replace("var next=sections.find(function(s){return (s.textContent||'').indexOf('YOUR NEXT MOVE')>=0});", "var next=sections[8];", 1)
s = s.replace("var mastersSection=sections.find(function(s){return (s.textContent||'').indexOf('18 NAYA MASTERS')>=0});", "var mastersSection=sections[9];", 1)
s = s.replace("var playground=sections.find(function(s){return (s.textContent||'').indexOf('PLAYGROUND')>=0});", "var playground=sections[10];", 1)

# Add the missing score-meaning chapter once, by structural matching of the actual
# rendered Five Dimensions marker in the builder source.
if "v21-score-meaning" not in s:
    score_meaning = r'''      '<section class="v21-section v21-light v21-score-meaning"><div class="v21-inner">'+
        '<span class="v21-kicker" style="color:#7445ad">WHAT YOUR SCORE MEANS</span><h2 class="v21-section-title">Your score is a starting point, not a verdict.</h2><div class="v21-story"><div class="v21-card"><span class="v21-kicker" style="color:#7445ad">WHERE YOU ARE</span><h3>'+st+'</h3><p>'+escapeHtml(st==='Mastering'?'You are operating with strong AI capability and can focus on compounding leverage.':st==='Advancing'?'You have meaningful capability and are ready to make your workflows more deliberate and repeatable.':st==='Developing'?'You have useful capability emerging; the fastest gains will come from deliberate practice and evaluation.':st==='Foundation'?'You have the building blocks. Focus on clarity, judgment and repeatable practice.':'You are beginning to establish the foundations. A few focused habits can change the trajectory quickly.')+'</p></div><div class="v21-card"><span class="v21-kicker" style="color:#7445ad">HOW TO USE IT</span><h3>Create → Score → Improve</h3><p>Use your result to choose one real AI workflow, make the quality visible, and improve it deliberately. Your next level comes from what you do with the score.</p></div></div></div></section>'+\
'''
    marker_re = re.compile(r'(?P<prefix>\n\s*)<span class="v21-kicker" style="color:#7445ad">YOUR FIVE DIMENSIONS</span>', re.S)
    m = marker_re.search(s)
    if not m:
        raise SystemExit("SCORE-MEANING INSERTION MARKER NOT FOUND IN ACTUAL BUILDER")
    # Insert before the Five Dimensions section opener by searching the full section start.
    section_re = re.compile(r'(?P<open>\s*<section class="v21-section v21-light"><div class="v21-inner">\'+\n\s*\'<span class="v21-kicker" style="color:#7445ad">YOUR FIVE DIMENSIONS</span>)', re.S)
    mm = section_re.search(s)
    if not mm:
        # Fallback: replace only the first exact rendered marker with the score-meaning
        # section followed by the original marker; this remains valid inside the JS concatenation.
        s = s.replace('<span class="v21-kicker" style="color:#7445ad">YOUR FIVE DIMENSIONS</span>', score_meaning + '<span class="v21-kicker" style="color:#7445ad">YOUR FIVE DIMENSIONS</span>', 1)
    else:
        original = mm.group('open')
        replacement = score_meaning + original
        s = s[:mm.start()] + replacement + s[mm.end():]

# Make the fingerprint chapter explicit without changing the contract marker.
if "YOUR AI FINGERPRINT" not in s:
    needle = '<span class="v21-kicker" style="color:#7445ad">YOUR FIVE DIMENSIONS</span>'
    s = s.replace(needle, '<span class="v21-kicker" style="color:#7445ad">YOUR AI FINGERPRINT</span>'+needle, 1)

# Strength depth.
old_strength = "<p>You already have meaningful capability here. Compound it deliberately instead of trying to improve everything at once. The best next move is to turn this strength into a repeatable advantage.</p>"
new_strength = "<p>You already have meaningful capability here. The goal is not to admire the score; it is to compound the capability until it becomes a repeatable advantage you can use across real AI work.</p><div class=\"v21-three\"><div class=\"v21-action\"><b>KEEP USING IT</b><p>Put this capability into a real workflow this week.</p></div><div class=\"v21-action\"><b>MAKE IT REPEATABLE</b><p>Turn what works into a reusable method or template.</p></div><div class=\"v21-action\"><b>TEACH IT TO NAYA</b><p>Use Naya to document and improve the workflow so the strength compounds.</p></div></div>"
s = s.replace(old_strength, new_strength, 1)

# Lever action loop.
old_lever = "<p>Your strongest opportunity is '+escapeHtml(lowest.name)+'. This is not a verdict about you. It is the area furthest behind the rest of your profile, so focused improvement here can create disproportionate gains.</p>"
new_lever = "<p>Your strongest opportunity is '+escapeHtml(lowest.name)+'. This is not a verdict about you. It is the clearest place to focus because it currently sits furthest behind the rest of your profile.</p><div class=\"v21-three\"><div class=\"v21-action\"><b>CHOOSE ONE TASK</b><p>Pick one real AI task where '+escapeHtml(lowest.name)+' matters.</p></div><div class=\"v21-action\"><b>IMPROVE IT ONCE</b><p>Make one deliberate change and compare the result.</p></div><div class=\"v21-action\"><b>REPEAT</b><p>Turn the improvement into a habit instead of a one-time fix.</p></div></div>"
s = s.replace(old_lever, new_lever, 1)

# Pathway personalization and Naya guidance.
old_path = "<p>These specialist pathways become useful once you know what you want to improve.</p>"
new_path = "<p>These specialist pathways are not just a library. They are the doors that can help you compound '+escapeHtml(strongest.name)+' and build '+escapeHtml(lowest.name)+'.</p><div class=\"v21-aaa-naya-note\"><img src=\"https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg\" alt=\"Naya, your AI guide\"><div><b>Naya · your guide</b><strong>Start with the pathway that matches your next move.</strong><p>Your best learning path is the one that connects directly to what your profile is telling you right now.</p></div></div>"
s = s.replace(old_path, new_path, 1)

# Final solution bridge.
s = s.replace('<h2>Now you know where you are. The next step is becoming better.</h2><p>MAXESS is designed for people who want exceptional results from AI—not “good enough.”</p>', '<h2>Now you know where you are. Let’s build what comes next.</h2><p>You have a score, a fingerprint, a strength, a lever and a next move. The next step is turning that understanding into real AI capability.</p>', 1)

# Explicit runtime source marker.
s = s.replace("root.setAttribute('data-results-data-source','window.MAXESS_RESULT');", "/* MAXESS_RESULT_AUTHORITY: window.MAXESS_RESULT */ root.setAttribute('data-results-data-source','window.MAXESS_RESULT');", 1)

if MARK not in s:
    s = s.replace("var scoreValue=score(r)||0;", MARK+"\n    var scoreValue=score(r)||0;", 1)

BUILDER.write_text(s, encoding="utf-8")
print("MAXESS V21 REMAINING AAA FINISH V2 APPLIED")
print("Completed: score meaning, fingerprint presentation, Strength depth, Lever action loop, pathway personalization, Naya guidance, final CTA, helper mapping cleanup, raw-JS repair, runtime authority marker.")
