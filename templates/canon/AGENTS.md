# AGENTS.md

Builder-Orchestrator
--------------------

Mission: Produce the goa-builder kit components (roles, prompts, templates)
and enforce the Context Manifest protocol. This agent is part of the kit — it
must not operate on external game repositories directly.

System directives (summary):

- Generate a `Context Manifest` before any task.
- Prefer recent `.logs/decisions/` entries over older `.canon/` entries when
  conflicts arise, unless explicitly told otherwise.
- After milestones instruct the Log Handler to summarize and update `.canon/`.

Planner, Researcher, Developer, QA, GitAssistant, ContextArchitect
---------------------------------------------------------------

See their role files under `.canon/roles/` for detailed missions and
constraints. These roles are templates for generated agents in target
projects.

## AGENTS.md (Canon Subtree Gate)

This gate applies to files under `.canon/**`.

## Authority (nearest wins)

When multiple `AGENTS.md` files exist, the **nearest** one is authoritative.

## Read-before-change

- Read `.canon/README.md` for system entry points.
- Read `.logs/INDEX.md` for how to write append-only logs.
- Read the nearest `AGENTS.md` before editing any files.

## Logging

- Write append-only records under `.logs/**`.
- Do not rewrite history; only add new entries.
- Use `.logs/navigation/**` to record how you navigated the repo (what you checked and why).

## Safety defaults

- Prefer read-only work unless a write mode is explicit.
- Keep changes minimal and localized.

## Placeholders (adjust per repo)

- Owner team: `{{CANON_OWNER_TEAM}}`
- Validation command/task: `{{CANON_VALIDATE_TASK}}`

<!-- md_autofix: processed -->
