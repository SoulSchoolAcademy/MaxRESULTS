# 🔒 MAXESS RESULTS — CANONICAL REPOSITORY LOCK

**STATUS: AUTHORITATIVE EXECUTION REPOSITORY**

This file exists to prevent repository drift, stale-build selection, and accidental work in the legacy MAXESS repository.

## 1. THIS IS THE ONLY ACTIVE MAXESS RESULTS REPOSITORY

Canonical repository:

`https://github.com/SoulSchoolAcademy/MaxRESULTS`

Canonical working branch for the current V21 Results work:

`maxess-results-v21-working`

Organization / owner:

`SoulSchoolAcademy`

Repository name:

`MaxRESULTS`

## 2. DO NOT USE THE LEGACY REPOSITORY FOR CURRENT RESULTS IMPLEMENTATION

Legacy repository:

`https://github.com/SoulSchoolAcademy/maxess`

The legacy repository contains historical MAXESS work, older Results builds, experiments, prototypes, and previous source-of-truth states.

**Do not select, edit, build from, or deliver a Results artifact from the legacy repository unless the human explicitly instructs you to perform historical comparison or recovery work.**

A file found in the legacy repository is never authoritative merely because it is newer-looking, larger, named FINAL/MASTER, or previously deployed.

## 3. REQUIRED REPOSITORY RESOLUTION GATE

Before ANY consequential Results work, explicitly verify all of the following:

- [ ] Repository owner = `SoulSchoolAcademy`
- [ ] Repository name = `MaxRESULTS`
- [ ] Repository URL = `https://github.com/SoulSchoolAcademy/MaxRESULTS`
- [ ] Current Results branch = `maxess-results-v21-working` unless the current human directive explicitly changes it
- [ ] Current task is Results work
- [ ] `NAYA-OS.md` has been read
- [ ] `README.md` has been read
- [ ] The canonical artifact has been located by path, not guessed from filename
- [ ] The current working artifact has been inspected before modification
- [ ] Historical/legacy repositories have NOT been substituted for this repository

If any check fails, **STOP. Do not edit. Resolve repository identity first.**

## 4. SOURCE-OF-TRUTH RULE

Do not infer authority from:

- filename age
- filename size
- `FINAL`
- `MASTER`
- `10/10`
- `FULL BUILD`
- timestamps
- previous conversation claims
- a public URL
- an old successful deployment

Authority is determined by the current repository governance and explicit artifact state.

## 5. NO BACKWARD MOVEMENT

A newer task must never silently return the project to an older artifact.

Before replacing or restoring an artifact:

1. identify its exact commit SHA;
2. identify its branch;
3. identify its file path;
4. compare it against the current working artifact;
5. prove which state is newer and why;
6. preserve the existing working state before replacement;
7. document the reason for any rollback.

If this cannot be proven, **do not roll back.**

## 6. DELIVERY RULE

Any delivered Results artifact must include:

- exact repository;
- exact branch;
- exact file path;
- exact commit SHA;
- explicit state (`UPDATED EDITED FILE`, `QA`, `APPROVED`, or `PRODUCTION`);
- verification evidence;
- public/Groove URL only when that deployment has actually been verified.

Never provide an old raw file and describe it as the current updated build.

## 7. HUMAN DIRECTOR OVERRIDE

The human director may explicitly designate another repository, branch, artifact, or historical version. That explicit instruction overrides this lock for that task only.

Otherwise, this lock is mandatory.

## 8. FAILURE SAFEGUARD

If repository identity is ever uncertain, do not guess.

Ask/verify first.

**Wrong repository + correct-looking work = failed work.**

**Correct repository + unverified work = incomplete work.**

**Correct repository + verified artifact + verified deployment = valid delivery.**
