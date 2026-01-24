# AGENTS — Procedural Memory & Authority Boundaries

This repository uses a governed agent model. This file is the procedural manifest that links agents, roles, and authority boundaries.

Principles

- Agents must read `.canon/README.md` and `.canon/project_facts.json` before taking action.
- Agents must follow the Dedicated Navigation Path (DNP) listed in `.canon/navigator/ENTRYPOINTS.md`.
- All automated scans and navigations must append a log entry under `.logs/`.

Agent authority map

- Orchestrator (CSO): coordination authority for multi-agent plans and long-running tasks; may trigger workflows and cross-check other agents.
- Context-Indexer: read-only authority over content indexing; writes indices under `.canon/00_Index/` or `.logs/`.
- Structure-Architect: may propose structural changes under a PR; write authority limited to `.canon/` and `.github/` artifacts after human review.
- Code-Auditor: read-only by default; may create reports and remediation PRs but requires human approval to merge fixes.
- Governance-Sentinel: policy enforcer; may block CI runs via checks and open issues for policy violations.

Agent manifests live under `.github/agents/` and role definitions under `.github/roles/`.

DNP (short)

1. Read `.canon/README.md`
2. Read `.canon/project_facts.json`
3. Read `.canon/navigator/ENTRYPOINTS.md` if present
4. Read `.canon/policies/`
5. Read `.github/agents/` manifests

Acceptance: Agents must read this file first when beginning repo automation tasks.

## AGENTS

This repository uses the GOA builder governance model. Agents must follow the Dedicated Navigation Path (DNP) and respect the procedural, semantic and episodic memory separation defined in .canon/ and .logs/.

## Dedicated Navigation Path (DNP)

Purpose: Prevent uncontrolled repo-wide searching and stabilize agent behavior in sessions.

### The only allowed navigation order (read in sequence)

1) `AGENTS.md` (this file)
2) `.canon/navigator/README.md` (repo map index)
3) `.canon/navigator/ENTRYPOINTS.md` (what files to open first per subsystem)
4) `.canon/policies/POLICY__dedicated-navigation-path__v1.md` (the rules)
5) `.canon/modules/engine/` (engine-specific rules, if the task touches engine code)
6) `.canon/policies/` and `.canon/roles/` (if role/policy constraints are relevant)

### Scanning rule (hard stop)

Agents must NOT scan the repository arbitrarily.

The only permitted scan action is running the repo-approved script:

- `.toolkit/scan/refresh_navigator.*`

Any other scanning must be treated as out-of-policy and stopped.

### Logging rule

Any navigation or scan must be logged (append-only) in:

- `.logs/navigation/`

### Acceptance

- Agents must read this file first and follow DNP before taking actions that read or write repository files.

## CSO Context

- The Contextual Systems Orchestrator (CSO) is initialized with the OCS knowledge base and OCS instructions and coordinates multi-agent workflows. The CSO's role and mission are recorded under `.canon/` artifacts.

## Numbering Policy

- New policy: All plans, logs, and agent-produced artifacts must use the MM.SS.TT (zero-padded) milestone/step/task numbering scheme. See `.canon/policies/POLICY__step-id-and-task-numbering.md` for details and examples.
- Constraint: Engine-agnostic, sequential execution, and append-only logging are required for orchestrated actions.

## MM.SS.TT Usage Examples

- Plan item example:

	```yaml

	- id: "00.01.01"

		title: "Ingest CSO instructions"
		owner: "CSO"
		status: "todo"
	```

- Changelog entry example (NDJSON):

	{"ts":"2026-01-24T12:00:00Z","task_id":"00.01.02","change_id":"CHG-001","author":"Maintainer","reason":"Initial promotion","changes":["Promoted validate_tool_contracts"],"tests_passed":true}

- Commit message convention: prefix commits with the Task ID. Example:

	[00.01.03] Add validate_tool_contracts CI workflow

Agents must follow the numbering policy when producing plans, logs, and commit messages. Validators under `.toolkit/` will check for MM.SS.TT compliance where applicable.

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
