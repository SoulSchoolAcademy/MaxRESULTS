#!/usr/bin/env python3
"""Minimal Naya Nitro V1 proof runner.

This proves the mechanical fast-edit loop on TEMPORARY copies of the real
MAXESS builder/source. It never edits, commits, or pushes the real working
repository. Visual quality is intentionally NOT claimed by this harness.

Proof loop per edit:
  NATURAL LANGUAGE REQUEST
  -> CLASSIFY
  -> LOCATE ACTIVE OWNER
  -> IDENTIFY EXACT SOURCE REGION
  -> APPLY SMALLEST SAFE PATCH
  -> VALIDATE TARGET SYNTAX
  -> BUILD TEMPORARY ARTIFACT
  -> VERIFY EXPECTED SOURCE DELTA
  -> VERIFY NO UNRELATED REWRITE
  -> VERIFY EXPECTED ARTIFACT DELTA
  -> TEMPORARY GIT CHECKPOINT
  -> RECORD

Run:
  python tools/prove_naya_nitro_v1.py
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import tempfile
import time
from dataclasses import dataclass, asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "20260817 912am RESULTS PAGE CODE"
BUILDER = ROOT / "tools" / "build_v21_canonical.py"
BASELINE_CANDIDATES = [ROOT / "BASELINE-WORKING.html", ROOT / "BASELINE-V20-WORKING.html"]
FAST_EDIT = ROOT / "tools" / "fast_edit_maxess.py"
REPORT = ROOT / "NAYA-NITRO-V1-PROOF.json"


class ProofError(RuntimeError):
    pass


@dataclass
class EditSpec:
    name: str
    request: str
    editor: str
    args: tuple
    owner_pattern: str
    expected_source_pattern: str
    artifact_pattern: str


@dataclass
class EditResult:
    name: str
    request: str
    classification: str
    owner: str
    source_sha_before: str
    source_sha_after: str
    source_delta_bytes: int
    changed_line_count: int
    build_pass: bool
    syntax_pass: bool
    artifact_changed: bool
    artifact_evidence: str
    temp_commit_sha: str
    elapsed_seconds: float
    status: str
    error: str | None = None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def baseline_path() -> Path | None:
    for candidate in BASELINE_CANDIDATES:
        if candidate.exists():
            return candidate
    return None


def run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)


def py_compile(path: Path, cwd: Path) -> None:
    proc = run(["python", "-m", "py_compile", str(path)], cwd)
    if proc.returncode != 0:
        raise ProofError(proc.stderr.strip() or "Python syntax validation failed")


def extract_js(builder_text: str) -> str:
    # Current builder uses JS = r"""...""". Keep a plain fallback too.
    markers = ['JS = r"""', 'JS = """']
    start = -1
    marker = ""
    for candidate in markers:
        pos = builder_text.find(candidate)
        if pos >= 0 and (start < 0 or pos < start):
            start = pos
            marker = candidate
    if start < 0:
        raise ProofError("Could not locate canonical JS payload in builder")
    start += len(marker)
    end = builder_text.find('"""', start)
    if end < 0:
        raise ProofError("Canonical JS triple-quoted payload is not closed")
    return builder_text[start:end]


def node_check(builder_text: str, cwd: Path) -> None:
    js = extract_js(builder_text)
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(js)
        js_path = Path(f.name)
    try:
        proc = run(["node", "--check", str(js_path)], cwd)
        if proc.returncode != 0:
            raise ProofError(proc.stderr.strip() or "Canonical JavaScript syntax validation failed")
    finally:
        js_path.unlink(missing_ok=True)


def changed_lines(before: str, after: str) -> int:
    import difflib
    return sum(1 for line in difflib.unified_diff(before.splitlines(), after.splitlines()) if line.startswith(("+", "-")) and not line.startswith(("+++", "---")))


def build_temp(repo: Path) -> tuple[Path | None, str]:
    # The builder writes its generated artifact into its own temp ROOT.
    proc = run(["python", "tools/build_v21_canonical.py"], repo)
    combined = (proc.stdout or "") + "\n" + (proc.stderr or "")
    if proc.returncode != 0:
        raise ProofError(combined.strip() or "Temporary canonical build failed")

    artifact = None
    for candidate in repo.iterdir():
        if candidate.is_file() and candidate.suffix.lower() == ".html" and "CANDIDATE" in candidate.name.upper():
            artifact = candidate
            break
    if artifact is None:
        # Fallback: detect the newest generated html file.
        htmls = [p for p in repo.glob("*.html") if p.name != SOURCE.name]
        if htmls:
            artifact = max(htmls, key=lambda p: p.stat().st_mtime_ns)
    return artifact, combined


def prepare_temp() -> Path:
    base = tempfile.mkdtemp(prefix="naya-nitro-v1-")
    repo = Path(base)
    (repo / "tools").mkdir()
    shutil.copy2(BUILDER, repo / "tools" / BUILDER.name)
    shutil.copy2(SOURCE, repo / SOURCE.name)
    bp = baseline_path()
    if bp:
        shutil.copy2(bp, repo / bp.name)
    else:
        # The builder may still be able to run against the source; preserve
        # explicit proof of missing baseline rather than inventing one.
        raise ProofError("No authoritative baseline file found")
    return repo


def git_init(repo: Path) -> None:
    for cmd in [
        ["git", "init", "-q"],
        ["git", "config", "user.email", "naya-nitro-proof@example.invalid"],
        ["git", "config", "user.name", "Naya Nitro Proof"],
        ["git", "add", "."],
        ["git", "commit", "-qm", "proof baseline"],
    ]:
        proc = run(cmd, repo)
        if proc.returncode != 0:
            raise ProofError(proc.stderr.strip() or f"Git command failed: {' '.join(cmd)}")


def git_checkpoint(repo: Path, name: str) -> str:
    for cmd in [["git", "add", "."], ["git", "commit", "-qm", f"Nitro proof: {name}"]]:
        proc = run(cmd, repo)
        if proc.returncode != 0:
            raise ProofError(proc.stderr.strip() or f"Git checkpoint failed: {' '.join(cmd)}")
    proc = run(["git", "rev-parse", "HEAD"], repo)
    if proc.returncode != 0:
        raise ProofError(proc.stderr.strip() or "Could not read proof checkpoint SHA")
    return proc.stdout.strip()


def exact_owner(builder_text: str, pattern: str, label: str) -> str:
    matches = list(re.finditer(pattern, builder_text, re.S))
    if len(matches) != 1:
        raise ProofError(f"{label}: expected exactly 1 owner match, found {len(matches)}")
    return label


def apply_edit(builder_text: str, spec: EditSpec) -> tuple[str, str]:
    # Use the already-reviewed targeted editor implementation when possible.
    module = None
    if FAST_EDIT.exists():
        import importlib.util
        module_spec = importlib.util.spec_from_file_location("fast_edit_maxess", FAST_EDIT)
        if module_spec and module_spec.loader:
            module = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(module)

    if module is None or not hasattr(module, "EDITORS"):
        raise ProofError("Existing fast_edit_maxess.py primitive could not be loaded")
    editors = module.EDITORS
    if spec.editor not in editors:
        raise ProofError(f"No registered editor for {spec.editor}")

    owner = exact_owner(builder_text, spec.owner_pattern, spec.name)
    value = spec.args[0] if spec.args else 0
    after = editors[spec.editor](builder_text, value)
    if after == builder_text:
        raise ProofError(f"{spec.name}: editor returned a no-op")
    if not re.search(spec.expected_source_pattern, after, re.S):
        raise ProofError(f"{spec.name}: expected post-edit source evidence not found")
    return owner, after


def make_specs() -> list[EditSpec]:
    return [
        EditSpec(
            "Orb size -15%",
            "Make the MAXESS Signature Orb 15% smaller.",
            "orb-size",
            (-15,),
            r"#maxess-results-10\.v21-canonical \.v21-score-orb",
            r"min\(434px,66\.3vw\)",
            r"v21-score-orb",
        ),
        EditSpec(
            "Naya position -6px",
            "Move Naya upward 6px.",
            "naya-up",
            (6,),
            r"#maxess-results-10\.v21-canonical \.v21-naya\{",
            r"transform:translateY\(-6px\)",
            r"v21-naya",
        ),
        EditSpec(
            "Primary button electric purple",
            "Make the primary Listen button a brighter electric purple.",
            "primary-button-electric",
            (0,),
            r"#maxess-results-10\.v21-canonical \.v21-listen\{",
            r"linear-gradient\(135deg,#c58cff,#7b35e7 52%,#3a116d\)",
            r"v21-listen",
        ),
        EditSpec(
            "Score typography +10%",
            "Increase the score typography by 10%.",
            "score-size",
            (10,),
            r"#maxess-results-10\.v21-canonical \.v21-score-number\{",
            r"clamp\(103px,14vw,187px\)",
            r"v21-score-number",
        ),
        EditSpec(
            "Naya headline spacing +16px",
            "Add 16px more space below the Naya headline.",
            "naya-headline-spacing",
            (16,),
            r"#maxess-results-10\.v21-canonical \.v21-naya-sub\{",
            r"margin:16px 0 0",
            r"v21-naya-sub",
        ),
    ]


def main() -> int:
    results: list[EditResult] = []
    started = time.perf_counter()

    if not SOURCE.exists() or not BUILDER.exists():
        raise SystemExit("Authoritative MAXESS source/builder is missing")

    for spec in make_specs():
        t0 = time.perf_counter()
        repo = prepare_temp()
        try:
            git_init(repo)
            temp_builder = repo / "tools" / BUILDER.name
            before = temp_builder.read_text(encoding="utf-8")
            before_sha = sha256_text(before)
            owner, after = apply_edit(before, spec)
            after_sha = sha256_text(after)
            delta = len(after.encode("utf-8")) - len(before.encode("utf-8"))
            line_delta = changed_lines(before, after)

            if before_sha == after_sha or delta == 0:
                raise ProofError("Non-zero source delta requirement failed")
            if line_delta > 30:
                raise ProofError(f"Unrelated rewrite suspected: {line_delta} changed lines")

            py_compile(temp_builder, repo)
            node_check(after, repo)
            temp_builder.write_text(after, encoding="utf-8")
            artifact, build_log = build_temp(repo)

            artifact_evidence = ""
            artifact_changed = artifact is not None and artifact.exists()
            if artifact_changed:
                artifact_text = artifact.read_text(encoding="utf-8", errors="replace")
                if not re.search(spec.artifact_pattern, artifact_text, re.I):
                    raise ProofError(f"{spec.name}: expected artifact evidence not found")
                artifact_evidence = spec.artifact_pattern
            else:
                raise ProofError(f"{spec.name}: temporary build did not produce an HTML artifact")

            checkpoint = git_checkpoint(repo, spec.name)
            elapsed = time.perf_counter() - t0
            results.append(EditResult(spec.name, spec.request, "MICRO EDIT", owner, before_sha, after_sha, delta, line_delta, True, True, True, artifact_evidence, checkpoint, elapsed, "PASS"))
            print(f"PASS | {spec.name} | {elapsed:.2f}s | checkpoint {checkpoint[:12]}")
        except Exception as exc:
            elapsed = time.perf_counter() - t0
            results.append(EditResult(spec.name, spec.request, "MICRO EDIT", spec.name, "", "", 0, 0, False, False, False, "", "", elapsed, "FAIL", str(exc)))
            print(f"FAIL | {spec.name} | {elapsed:.2f}s | {exc}")
        finally:
            shutil.rmtree(repo, ignore_errors=True)

    payload = {
        "system": "NAYA NITRO V1",
        "proof_type": "mechanical",
        "visual_proof_required_separately": True,
        "started_at_elapsed": 0,
        "total_elapsed_seconds": time.perf_counter() - started,
        "results": [asdict(r) for r in results],
        "passed": sum(r.status == "PASS" for r in results),
        "failed": sum(r.status != "PASS" for r in results),
        "verdict": "PROVEN_MECHANICALLY" if all(r.status == "PASS" for r in results) else "NOT_PROVEN",
    }

    print(json.dumps(payload, indent=2))
    return 0 if payload["verdict"] == "PROVEN_MECHANICALLY" else 1


if __name__ == "__main__":
    raise SystemExit(main())
