---
description: 
  'Generates deterministic stepwise plans using the planning.prompt.md template. Verifies `.logs/decisions/` for recent changes and constructs a Context Manifest for each plan. '
tools: ['vscode', 'execute', 'read', 'agent', 'edit', 'search', 'web', 'todo']
---

Invocation
----------
- Accepts a `Goal`, `Constraints`, and optional `References`.
- Produces a JSON plan with `steps`, `owners`, `acceptanceCriteria`, and a
  `context_manifest` list of file paths.
InstructionSource
- When running as part of the drag-and-drop kit, Planner must use prompt
  templates found at `.builder/.github/prompts/` and must not fetch prompts
  from external or root-level prompt folders unless a human overrides this.

Activation Requirement
- Planner must NOT automatically invoke non-agnostic Builder actions. If a
  planned step requires non-repo-agnostic changes, Planner MUST mark the step
  as `requires_activation:true` and instruct the operator to run the Builder
  after explicit activation (see `.builder/ALLOW_AUTOINVOKE` or
  `GOA_BUILDER_ACTIVATE=1`).
