# POLICY: Quality Gates v1

## Purpose

Define “stop-the-line” conditions for GOA operations. If any hard gate fails, the system must not proceed to integration.

## Hard gates (must pass)

### GATE-Q1 — Generated surface validation

Command:

- `python3 .builder/builder.py validate --scope generated`

Failure condition:

- Any markdownlint failures or missing validation tooling.

### GATE-Q2 — Governance approval

Command:

- `.toolkit/validate/governance_gate.*`

Failure condition:

- governance gate emits `approved=false`

### GATE-Q3 — Required audit artifacts exist (for code changes)

Required (minimum one):

- `.logs/test/YYYY-MM-DD__code-audit__results.sarif`
- `.logs/test/YYYY-MM-DD__*.md` (human QA log)

## Soft gates (warn, do not block by default)

### GATE-S1 — Navigator freshness

If major repository structure changed, run:

- `.toolkit/scan/refresh_navigator.*`

and log to `.logs/navigation/`

## Enforcement

- CI must execute `validate_repo.*` or both: (validate + governance gate).
- Orchestrator must refuse “integrate” stage if any hard gate fails.

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
