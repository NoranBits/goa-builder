# RUNBOOK: Maintenance Loop v1

## Purpose

Keep the repository’s cognitive surfaces coherent over time by promoting repeated findings from `.logs/` into durable guidance in `.canon/`.

## Inputs

- `.logs/test/*` (audit and QA results)
- `.logs/navigation/*` (scan/refresh traces)
- `.logs/decisions/*` (rationale for changes)
- `.canon/evals/*` (canary/adversarial sets)

## Cadence

- Weekly (or per milestone) review by Maintainer role.

## Procedure

### Step 1 — Collect high-frequency failures

Identify repeated patterns in the last N logs:

- validation failures
- governance gate failures
- recurring SARIF rule IDs

### Step 2 — Classify root cause

Use a simple taxonomy:

- Retrieval/navigation failure (DNP)
- Instruction failure (policy conflict / missing rule)
- Format drift (schema/markdown)
- Missing tests / missing evidence

### Step 3 — Promote stable guidance

If a failure repeats ≥ 3 times:

- Update relevant policy/runbook/spec in `.canon/`
- Add/update SARIF rule mapping (if applicable)
- Add a canary test case under `.canon/evals/`

### Step 4 — Record rationale

Write a decision record in `.logs/decisions/`.

### Step 5 — Re-run gates

- `python3 .builder/builder.py validate --scope generated`
- `.toolkit/validate/validate_repo.*`

## Output

- Updated `.canon/` artifacts (semantic memory)
- New canary/adversarial eval items
- Decision record documenting why

<!-- md_autofix: processed -->
