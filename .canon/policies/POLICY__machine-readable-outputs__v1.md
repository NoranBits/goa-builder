# POLICY: Machine-Readable Outputs v1

Purpose
-------
Require machine-usable artifacts for any output that will be used as an automated gate or as structured input to downstream agents.

Scope
-----
Applies to Planner outputs, Structure/Code audits, Governance gates, and any tool-run summaries intended for programmatic checks.

Rules
-----

- Use JSON Schema for planner/report contracts (place schemas under `.canon/schemas/`).
- Use SARIF 2.1.0 for code-audit findings intended for GitHub Code Scanning. Write SARIF files under `.logs/test/`.
- Validators must be present in `.toolkit/validate/` or be part of the builder toolchain.

Examples
--------

- Planner: must validate against `SCHEMA__planner-plan__v1.json` before being accepted.
- Code Auditor: emit `.logs/test/YYYY-MM-DD__code-audit__results.sarif` and optional human summary `.logs/test/YYYY-MM-DD__code-audit__summary.md`.

Enforcement
-----------
Governance Sentinel will consider missing or invalid structured outputs as a failing gate (see `POLICY__quality-gates__v1.md`).

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
