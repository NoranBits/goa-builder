# `.github` (agent prompts & roles)

This folder contains canonical agent roles, prompt templates, and internal
guidance used by the goa-builder kit. It is the repository-visible place for
role definitions and shared prompt templates that are *repo-agnostic*.

Policy summary
--------------

- The Builder-Orchestrator's internal instruction set for the drag-and-drop
  payload is stored under `.builder/.github/` and must be used by the
  payload's internal agents.
- Generated agents operating in a target project MUST NOT automatically invoke
  the internal Builder-Orchestrator or its internal instructions.

Activation (human consent)
--------------------------

To run non-repo-agnostic Builder tasks (structural changes, template
installation, canonical updates), the operator must explicitly enable the
Builder by either creating the marker file at the repository root:

```text
.builder/ALLOW_AUTOINVOKE
```text

or exporting the environment variable:

```bash
export GOA_BUILDER_ACTIVATE=1
```text

Agents and scripts should call `tools/require_activation.py` and respect its
exit code before proceeding with non-agnostic operations.

<!-- md_autofix: processed -->
