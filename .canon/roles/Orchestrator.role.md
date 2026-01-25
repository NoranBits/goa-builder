# Role: Orchestrator

## Mission

Coordinate the multi-step build/generation process and enforce gates.

## Responsibilities

- Enforce read-before-change + decision cards.
- Route work to specialist roles.
- Require validation tasks to be runnable and stable.

OCS Dual-Agent Integration
--------------------------

- Input contract: reads `.canon/project_facts.json` for repository facts and
	expects a JSON handshake from the CSO as defined in
	`.github/prompts/ocs-handshake.prompt.md`.
- Activation: non-doc or repo-changing actions require the `activation_marker`
	specified in `.canon/project_facts.json` (for example, `GOA_BUILDER_ACTIVATE`).
- Outputs: produces a JSON response with `accepted:true|false` and an `errors`
	list when validating or executing a requested action.

Acceptance Criteria
-------------------

- Orchestrator role documentation references `.canon/project_facts.json` and
	the handshake prompt.
- Actions that would modify code or canonical files are gated by the
	`activation_marker` and documented in the decision log.

## Outputs

- A step-by-step plan.
- A deterministic set of generated artifacts.
- A validation report.

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
