# SPEC: SARIF Rule Catalog v1

## Purpose

Define the canonical set of SARIF rule IDs used by GOA Code Auditor, and map each to authoritative policy/spec references.

## Location of the map

- `.canon/config/sarif-policy-map.json` (runtime map file)
- Schema: `.canon/schemas/SCHEMA__sarif-policy-map__v1.json`

## Rule ID grammar

- Prefix: `GOA-`
- Domain: `POLICY`, `QA`, `SEC`, `STRUCT`, `DOC`
- Numeric code: 3 digits

Examples:

- `GOA-POLICY-001`
- `GOA-QA-010`

## Minimum required rules (v1)

### GOA-POLICY-001 — Dedicated Navigation Path enforced

- Default severity: `error`
- Canon refs:
  - `.canon/policies/POLICY__dedicated-navigation-path__v1.md`

Trigger examples:

- Repo-wide scanning outside `.toolkit/scan/refresh_navigator.*`
- Editing files without reading nearest `AGENTS.md` gate

### GOA-POLICY-002 — Unknowns must be explicit

- Default severity: `warning`
- Canon refs:
  - `.canon/policies/POLICY__unknowns-and-abstention__v1.md`

Trigger examples:

- Unsupported factual assertions without evidence pointers
- Missing uncertainty notes where required

### GOA-QA-010 — Validation gate missing or failing

- Default severity: `error`
- Canon refs:
  - `.canon/policies/POLICY__quality-gates__v1.md`

Trigger examples:

- `python3 .builder/builder.py validate --scope generated` not executed, or failed

## Output location conventions

- SARIF: `.logs/test/YYYY-MM-DD__code-audit__results.sarif`
- Human summary: `.logs/test/YYYY-MM-DD__code-audit__summary.md`

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
