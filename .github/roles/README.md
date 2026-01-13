# .github/roles

This folder contains role definitions (mission, scope, inputs/outputs,
constraints) for the goa-builder kit. All roles here are exclusive to the
goa-builder seed and are meant to be templates for generated agents that will
operate on downstream projects. The Builder-Orchestrator itself only creates
and maintains these files; it does not operate on external repositories.

Roles included:

- Planner
- Researcher
- Developer
- QA
- GitAssistant
- ContextArchitect

Use these files as canonical role descriptions when generating per-project
agent instances.
