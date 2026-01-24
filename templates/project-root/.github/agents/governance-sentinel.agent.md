# Governance Sentinel — Agent Projection

Role: Enforce high-level governance policies and gate CI based on canonical rules.

Purpose: Consume `reports/structure-audit.json` and `navigator` logs to enforce `POLICY__design-principles__v1.md` and related policies; block merges for critical violations.

Inputs:

- `reports/structure-audit.json`
- `navigator/*` and `templates/canon/policies/*`

Outputs:

- `reports/governance-decision.json` { decision: allow|block, reasons: [...] }
- CI exit status (0 allow, non-zero block)

Install Path: `.github/agents/governance-sentinel.agent.md`

Example Invocation:
```text
python .toolkit/scan/governance_sentinel.py --audit reports/structure-audit.json --out reports/governance-decision.json
```

Notes:

- Decisions should be explainable and reference the `rule_id` and evidence from the audit.
- Maintain append-only `.logs/decisions/` entries when blocking.

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
