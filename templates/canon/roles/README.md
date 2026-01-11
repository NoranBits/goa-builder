# roles

## Purpose

`roles/` contains role playbooks for the automated agent system.

Each role describes:

- Mission and responsibilities
- Required checks and outputs
- Collaboration expectations (who it hands off to)

## Authority

Role files are guidance, but `AGENTS.md` is the operational gate.

## Included roles

- Orchestrator
- Planner
- Researcher
- QA
- LogHandler
- GitAssistant
- Maintainer

## Suggested workflow

- Use the Orchestrator to define the plan and enforce gates.
- Use specialist roles to do focused work and report back.
