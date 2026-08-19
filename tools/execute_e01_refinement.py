from pathlib import Path

# Deterministic E01 mutation: this file is the executable patch, not a renderer.
TARGET = Path("E01-SECTION-01-WORKING.html")

REQUIRED_OLD = [
    'maxess-version" content="nitro-e01-v27"',
    'data-maxess-version="nitro-e01-v27"',
    'padding:clamp(24px,3vw,34px);border:1px solid rgba(208,168,255,.48);border-radius:32px',
    'width:108px;height:108px;display:grid;place-items:center',
    'Hi. I’ve looked at your results.',
    'I’m here to help you understand what your score actually means — and what it reveals about the way you work with AI.',
    'This number is a starting point — <strong>not a verdict.</strong> It shows where your current AI capability stands and where your next level begins.',
]

PROTECTED = [
    'animation:orb-breathe 6s ease-in-out infinite',
    'translateX(220px)',
    'translateX(140px)',
    'width:14px;height:14px',
    'width:11px;height:11px',
    'width:min(280px,78%)',
    'prefers-reduced-motion:reduce',
    'window.MAXESS_RESULT',
    'overallScore',
    'maxess:naya-listen',
]

REPLACEMENTS = [
    ('maxess-version" content="nitro-e01-v27"', 'maxess-version" content="nitro-e01-v28"'),
    ('data-maxess-version="nitro-e01-v27"', 'data-maxess-version="nitro-e01-v28"'),
    ('padding:clamp(24px,3vw,34px);border:1px solid rgba(208,168,255,.48);border-radius:32px', 'padding:clamp(26px,3.2vw,38px);border:1px solid rgba(208,168,255,.62);border-radius:34px'),
    ('box-shadow:0 42px 120px rgba(0,0,0,.60),inset 0 1px rgba(255,255,255,.16),inset 0 -1px rgba(166,108,255,.10),0 0 78px rgba(155,99,255,.14)', 'box-shadow:0 46px 132px rgba(0,0,0,.66),inset 0 1px rgba(255,255,255,.18),inset 0 -1px rgba(166,108,255,.12),0 0 92px rgba(155,99,255,.18)'),
    ('width:108px;height:108px;display:grid;place-items:center', 'width:116px;height:116px;display:grid;place-items:center'),
    ('width:108px;height:108px;border-radius:50%', 'width:116px;height:116px;border-radius:50%'),
    ('font-size:clamp(27px,3.2vw,42px);line-height:1.02;letter-spacing:-.048em', 'font-size:clamp(29px,3.35vw,44px);line-height:1.01;letter-spacing:-.052em'),
    ('This isn’t your judgment. It’s your map.', 'This isn’t your judgment. It’s your map — it’s your starting point.'),
    ('I’m here to help you understand what your score actually means — and what it reveals about the way you work with AI.', 'I’m here to help you understand what your score means, what you already do well, and where your next level of AI capability begins.'),
    ('This number is a starting point — <strong>not a verdict.</strong> It shows where your current AI capability stands and where your next level begins.', 'This number is a starting point — <strong>not a verdict.</strong> It shows your current AI capability and gives you a clear place to begin your next level.'),
    ('padding-top:clamp(42px,5vw,62px)', 'padding-top:clamp(48px,5.6vw,70px)'),
    ('margin:clamp(-4px,-.2vw,2px) auto 0', 'margin:clamp(-10px,-.55vw,-2px) auto 0'),
]

s = TARGET.read_text(encoding="utf-8")
for needle in REQUIRED_OLD:
    if needle not in s:
        raise SystemExit(f"E01 refinement guard failed; expected source fragment missing: {needle}")

for old, new in REPLACEMENTS:
    if old not in s:
        raise SystemExit(f"E01 refinement guard failed; replacement source fragment missing: {old}")
    s = s.replace(old, new, 1)

if s.count('nitro-e01-v28') != 2:
    raise SystemExit('Expected exactly two v28 identity markers')

for token in PROTECTED:
    if token not in s:
        raise SystemExit(f"Protected E01 behavior missing after refinement: {token}")

if 'nitro-e01-v27' in s:
    raise SystemExit('Stale v27 identity remains in E01 source')

TARGET.write_text(s, encoding="utf-8")
print(f"E01 refined in place: {len(s.encode('utf-8'))} bytes")
print("Version: nitro-e01-v28")
print("Protected behavior checks: PASS")
