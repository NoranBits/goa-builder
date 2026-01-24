# Code Auditor — Agent Projection

Role: Perform lightweight static analysis and policy checks, producing machine-readable audit outputs.

Purpose: Run linters and policy checks, normalize results to `SCHEMA__structure-audit__v1.json`, and produce SARIF if applicable.

Inputs:

- source files
- linter configs (e.g., `.eslintrc`, `pyproject.toml`)

Outputs:

- `reports/structure-audit.json` (SCHEMA__structure-audit__v1)
- optional `reports/code.sarif`

Install Path: `.github/agents/code-auditor.agent.md`

Example Invocation:
```text
python .toolkit/scan/validate_repo.py --out reports/structure-audit.json --sarif reports/code.sarif
```

Notes:

- Non-zero exit codes must be used for `severity: error` items so CI can fail.
- Map linter IDs to `rule_id` in the structure-audit output.

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
