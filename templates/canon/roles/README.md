# roles

> **Context**: Definition of the specialized personas that collaborate within the Game Creator Agent System. These are not just "jobs" but "modes of operation" for AI agents.

## Purpose

`roles/` contains role playbooks for the automated agent system.

Each role describes:

- Mission and responsibilities.
- Required checks and outputs.
- Collaboration expectations (who it hands off to).

## Authority

Role files are guidance, but `AGENTS.md` is the operational gate.

## Included Roles

- **Orchestrator**: High-level planner and gatekeeper.
- **Planner**: Detailed implementation strategist.
- **Researcher**: Knowledge gatherer and summarizer.
- **QA**: Quality assurance and test engineer.
- **LogHandler**: Telemetry and audit specialist.
- **GitAssistant**: Version control manager.
- **Maintainer**: Long-term health and refactoring specialist.

## Suggested Workflow

- Use the **Orchestrator** to define the plan and enforce gates.
- Use specialist roles to do focused work and report back.

## External Context (For Generators)

> **Note**: These links are just examples. Upon scanning the repository and digesting the stack, this section should be updated with accurate external context matching the project.

- **RACI Matrix**: [Wiki Definition](https://en.wikipedia.org/wiki/RACI_matrix) - Responsible, Accountable, Consulted, Informed model for role clarity.
- **Autonomous Agents**: [Lilian Weng's Blog](https://lilianweng.github.io/posts/2023-06-23-agent/) - Deep dive into LLM-powered autonomous agent systems.
- **Role-Based Access Control (RBAC)**: [NIST Definition](https://csrc.nist.gov/glossary/term/role_based_access_control) - Concept of permissions tied to roles.
