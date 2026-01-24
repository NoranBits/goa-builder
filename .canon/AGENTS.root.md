# AGENTS.md (Root Gate)

This file is the root authority for agent behavior in this repository.

## Authority rule (nearest wins)

When multiple `AGENTS.md` files exist, the **nearest** one to the file being changed is authoritative.

- Example: `packages/server/AGENTS.md` overrides this root gate for files under `packages/server/**`.
- If a subtree gate exists, agents MUST read it before making any changes in that subtree.

## Required workflow

### Read-before-change

- Read `.logs/changes/INDEX.md`.
- Read the newest relevant change logs.
- Read the nearest applicable `AGENTS.md`.

### Decision Card + explicit confirmation

- Before editing any files, produce exactly one Decision Card.
- Stop and wait for explicit human approval.

### Logging (append-only)

- Any file-touching change MUST create a change log entry under `.logs/changes/YYYY/MM/DD/`.
- Update `.logs/changes/INDEX.md` (append-only).

### Validation

- Prefer stable VS Code tasks and repo validators.
- Validation should fail rather than silently skipping required checks.

## Subtree gates

A subtree may define its own gate by adding an `AGENTS.md` in that folder.

Subtree gates should:

- Narrow scope to that subtree.
- Add additional safety rules specific to the domain.
- Keep rules actionable and testable.

## Safety defaults

- Prefer read-only behavior unless a write mode is explicit.
- Never write outside the repo root.
- Avoid large blast-radius edits.

<!-- md_autofix: processed -->
