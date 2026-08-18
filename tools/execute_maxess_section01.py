#!/usr/bin/env python3
"""MAXESS Section 01 owner: idempotent Golden Master + narrative alignment."""
from __future__ import annotations

from pathlib import Path
import hashlib
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools" / "build_v21_canonical.py"
MARK = "/* MAXESS-SECTION-01-GOLDEN-MASTER */"
RENDER_START = "root.innerHTML='<div class=\"v21-shell\">'+"
RENDER_END = "var btn=root.querySelector('.v21-listen')"


def validate_js(text: str) -> None:
    with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as fh:
        fh.write(text)
        path = fh.name
    proc = subprocess.run(['node', '--check', path], capture_output=True, text=True)
    Path(path).unlink(missing_ok=True)
    if proc.returncode:
        raise SystemExit(proc.stderr.strip() or 'Node syntax validation failed')


def validate_python() -> None:
    subprocess.run(['python', '-m', 'py_compile', str(BUILDER)], check=True)


def align_renderer(js: str) -> str:
    start = js.find(RENDER_START)
    if start < 0:
        raise SystemExit('SECTION 01: V21 root renderer assembly missing')
    end = js.find(RENDER_END, start)
    if end < 0:
        raise SystemExit('SECTION 01: V21 root renderer closing anchor missing')

    render = js[start:end]

    # Remove obsolete chapters from the actual product renderer only.
    # These are already-clean states when count==0; do not fail an idempotent run.
    for label in ('YOUR LEVER', 'YOUR NEXT MOVE'):
        pattern = re.compile(
            r"\n\s*'(?P<section><section class=\\\"v21-section[^\n]*" +
            re.escape(label) + r"[^\n]*)</section>'\+",
            re.S,
        )
        render, count = pattern.subn('\n', render, count=1)
        if count > 1:
            raise SystemExit(f'SECTION 01: duplicate obsolete {label} sections found: {count}')

    # Replace obsolete Playground chapter with the approved existing media moment.
    playground = re.compile(
        r"\n\s*'<section class=\\\"v21-section v21-light\\\"><div class=\\\"v21-inner\\\"><span class=\\\"v21-kicker\\\" style=\\\"color:#7445ad\\\">PLAYGROUND</span>.*?</section>'\+",
        re.S,
    )
    replacement = (
        "\n      '<section class=\\\"v21-section v21-dark\\\"><div class=\\\"v21-inner\\\">"
        "<span class=\\\"v21-kicker\\\">NAYA · IN PRACTICE</span>"
        "<h2 class=\\\"v21-section-title\\\">See what your result can become.</h2>"
        "<p class=\\\"v21-section-copy\\\">Naya helps turn your MAXESS result into a practical next step.</p>"
        "<div id=\\\"v21-media-host\\\" class=\\\"v21-media-host\\\"></div>"
        "</div></section>'+"
    )
    render, count = playground.subn(replacement, render, count=1)
    if count > 1:
        raise SystemExit(f'SECTION 01: duplicate PLAYGROUND sections found: {count}')
    if count == 0 and 'NAYA · IN PRACTICE' not in render:
        raise SystemExit('SECTION 01: approved NAYA · IN PRACTICE section is missing')

    # Preserve actual media assets only; do not relocate an obsolete section tree.
    old_media = "root.querySelectorAll('video,iframe,#naya-playground,.mx-reading,.mx-section').forEach(function(n){ if(media.indexOf(n)<0) media.push(n); });"
    new_media = "root.querySelectorAll('#ny-youtube-player,video,iframe[src*=\"youtube\"],iframe[src*=\"vimeo\"]').forEach(function(n){ if(media.indexOf(n)<0) media.push(n); });"
    if old_media in js:
        js = js.replace(old_media, new_media)

    # Move preserved media into the new owner.
    old_host = "var host=root.querySelector('#v21-playground-host');if(host){media.forEach(function(n){if(n && n!==root && n.parentNode!==host)host.appendChild(n);});}"
    new_host = "var host=root.querySelector('#v21-media-host');if(host){media.forEach(function(n){if(n && n!==root && n.parentNode!==host)host.appendChild(n);});}"
    if old_host in js:
        js = js.replace(old_host, new_host)

    # The V21 Hero owns the visible Listen control.
    old_ids = "var ids=['#mx-naya-listen','#v11-naya-listen','#v13-listen','.mx-naya-listen','.v18-listen'];"
    new_ids = "var ids=['.v21-listen.b1s1-listen','.v21-listen'];"
    if old_ids in js:
        js = js.replace(old_ids, new_ids)

    return js[:start] + render + js[end:]


def main() -> int:
    if not BUILDER.exists():
        raise SystemExit('SECTION 01: builder missing')

    original = BUILDER.read_text(encoding='utf-8')
    if MARK not in original:
        raise SystemExit('SECTION 01: Golden Master layer is missing; refuse to invent it here')

    match = re.search(r'<script id="maxess-results-v21-canonical-js">(.*?)</script>', original, re.S)
    if not match:
        raise SystemExit('SECTION 01: canonical V21 runtime block missing')

    js = match.group(1)
    aligned_js = align_renderer(js)
    validate_js(aligned_js)
    updated = original[:match.start(1)] + aligned_js + original[match.end(1):]

    if updated == original:
        print('SECTION 01: renderer already aligned; Golden Master preserved')
        validate_python()
        return 0

    BUILDER.write_text(updated, encoding='utf-8')
    validate_python()

    print('MAXESS SECTION 01 PRODUCT ALIGNMENT: PASS')
    print('GOLDEN MASTER: PRESERVED')
    print('REMOVED: YOUR LEVER (if present)')
    print('REMOVED: YOUR NEXT MOVE (if present)')
    print('PLAYGROUND: REPLACED OR ALREADY ABSENT')
    print('MEDIA OWNER: EXISTING VIDEO / MEDIA ASSETS')
    print('LISTEN OWNER: V21 HERO CONTROL')
    print('NODE CHECK: PASS')
    print('PYTHON CHECK: PASS')
    print('BUILDER SHA BEFORE:', hashlib.sha256(original.encode('utf-8')).hexdigest())
    print('BUILDER SHA AFTER: ', hashlib.sha256(updated.encode('utf-8')).hexdigest())
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
