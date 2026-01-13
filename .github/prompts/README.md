# .github/prompts

This folder contains prompt templates and system guidance used by the
Builder-Orchestrator and the role templates in `.github/roles/`.

Structure
---------

- `planning.prompt.md` — planning template for the Planner role.
- `refactor.prompt.md` — safe refactor template for Developer workflows.
- `validate.prompt.md` — QA validation template.
- `copilot_system_guidance.md` — notes and condensed guidance derived from
  authoritative Copilot/VS Code docs (fetched via `fetch_webpage`).

Usage
-----

1. The Builder-Orchestrator or Planner fills the placeholders in a prompt and
   issues it to the target role or agent.
2. Prefer structured outputs (JSON/YAML) for machine-readability.
3. Keep prompts short and include only the necessary context; reference
   `.docs/` entries for longer background.
