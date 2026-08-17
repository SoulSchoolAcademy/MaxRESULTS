#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import hashlib
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "BASELINE-WORKING.html"
SOURCE = ROOT / "20260817 912am RESULTS PAGE CODE"
REPORT = ROOT / "V21-CLEAN-BUILD-RESULT.md"
V21_MARKER = 'id="maxess-results-v21-authority-js"'
RECOGNITION_SCRIPT = '<script id="maxess-recognition-flow-10-4-js">'


def sha_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_packet2_fragments():
    import importlib.util
    p = ROOT / "tools" / "apply_v21_packet2.py"
    spec = importlib.util.spec_from_file_location("packet2", p)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load apply_v21_packet2.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.V21_CSS.replace("\\n", "\n"), mod.V21_JS.replace("\\n", "\n")


def repair_recognition_flow(text: str) -> str:
    start = text.find(RECOGNITION_SCRIPT)
    if start < 0:
        return text
    end = text.find("</script>", start)
    if end < 0:
        raise RuntimeError("Recognition flow script closing tag not found")
    block = text[start:end + len("</script>")]
    # Remove the malformed runtime CSS injection. The same CSS already exists in
    # the preceding style block, so runtime injection is redundant and unsafe.
    block = re.sub(
        r"\n\s*const s=document\.createElement\('style'\);s\.id='maxess-recognition-flow-10-4';s\.textContent=.*?document\.head\.appendChild\(s\);\n",
        "\n",
        block,
        flags=re.S,
    )
    if "s.textContent" in block or "document.createElement('style')" in block:
        raise RuntimeError("Recognition flow repair did not remove runtime style injection")
    return text[:start] + block + text[end + len("</script>"):]


def extract_scripts(text: str):
    return re.finditer(r"<script(?:\s[^>]*)?>(.*?)</script>", text, re.I | re.S)


def validate_scripts(text: str):
    failures = []
    blocks = list(extract_scripts(text))
    for idx, m in enumerate(blocks, 1):
        body = m.group(1)
        if not body.strip():
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as fh:
            fh.write(body)
            path = fh.name
        proc = subprocess.run(["node", "--check", path], capture_output=True, text=True)
        Path(path).unlink(missing_ok=True)
        if proc.returncode != 0:
            first = proc.stderr.strip().splitlines()
            failures.append(f"script {idx}: {first[0] if first else 'syntax failure'}")
    return failures, len(blocks)


def main() -> int:
    if not BASELINE.exists():
        print("ERROR: BASELINE-WORKING.html missing")
        return 2
    baseline = BASELINE.read_text(encoding="utf-8")
    if not baseline.strip():
        print("ERROR: baseline is empty")
        return 3
    text = repair_recognition_flow(baseline)
    css, js = load_packet2_fragments()
    if V21_MARKER in text:
        raise RuntimeError("V21 authority marker unexpectedly exists in baseline")
    insertion = css + "\n" + js
    if "</body>" in text:
        text = text.replace("</body>", insertion + "\n</body>", 1)
    else:
        text += "\n" + insertion + "\n"
    marker_count = text.count(V21_MARKER)
    if marker_count != 1:
        print(f"ERROR: V21 marker count={marker_count}, expected 1")
        return 4
    failures, script_count = validate_scripts(text)
    if failures:
        print("ERROR: clean build failed JavaScript syntax validation")
        for f in failures:
            print("FAIL:", f)
        return 5
    SOURCE.write_text(text, encoding="utf-8")
    REPORT.write_text(
        "# MAXESS V21 — CLEAN BUILD\n\n"
        f"- Baseline SHA-256: `{sha_text(baseline)}`\n"
        f"- Candidate SHA-256: `{sha_text(text)}`\n"
        f"- Candidate lines: `{len(text.splitlines())}`\n"
        f"- Inline scripts: `{script_count}`\n"
        f"- V21 authority marker count: `{marker_count}`\n"
        "- Recognition 10.4 runtime-style injection: `REMOVED`\n"
        "- JavaScript syntax gate: `PASS`\n",
        encoding="utf-8",
    )
    print("V21 CLEAN BUILD COMPLETE")
    print(f"Baseline SHA-256: {sha_text(baseline)}")
    print(f"Candidate SHA-256: {sha_text(text)}")
    print(f"Lines: {len(text.splitlines())}")
    print(f"Inline scripts: {script_count}")
    print("Recognition 10.4 runtime-style injection: REMOVED")
    print("JS SYNTAX GATE: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
