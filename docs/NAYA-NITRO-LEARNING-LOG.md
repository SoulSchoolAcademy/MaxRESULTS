# NAYA NITRO LEARNING LOG

Purpose: durable memory of execution-system lessons that materially improve future work.

## 2026-08-17 — Clean repository / Codespace workflow

### Lesson
A large production HTML file should live in the repository and be edited in a proper workspace rather than repeatedly transported through chat.

### Validated workflow
GitHub repository → Codespace → local synchronization (`git pull`) → protected baseline → isolated working branch → batch transformation → automated validation → commit/push → human/public verification.

### Important constraints discovered
- A Codespace can exist before its local worktree has the latest repository contents; `git pull origin main` synchronized the workspace.
- GitHub repository state and Codespace local state are related but not identical; verify the local branch/worktree before operating.
- A GitHub commit proves repository state, not Groove publication or live public behavior.
- Large-file GitHub contents operations are a poor place to perform repeated whole-file reconstruction when a complete workspace is available.

### Preservation lesson
Always protect the known-good working source before transformation. Use `main` as the safety baseline and an isolated branch for active engineering.

### Execution lesson
Do not make the user manually debug a large source one tiny defect at a time. Build diagnostics and validators that expose exact failures, then repair the underlying tool/process.

### Product lesson
The goal is not merely a prettier page. The Results experience must connect data to interpretation, action, capability, and a professionally designed saved report.

### Rule promoted into Nitro
Use the largest safe coherent batch available. Minimize user intervention. Never claim completion before the release gate passes.

## Logging rule
Only durable lessons belong here. Temporary command output, one-off errors, and transient infrastructure failures do not become permanent law unless they reveal a repeatable constraint or workflow improvement.
