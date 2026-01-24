# POLICY: Design Principles (GOA builder) v1

Purpose
-------
Capture the non-negotiable design principles that govern how agents operate in this repository. These rules are authoritative: follow them before acting.

Key principles
--------------

- Memory stratification: keep long-term truth, history, and procedures separate.
  - Semantic memory (authoritative truth) → `.canon/`
  - Episodic memory (append-only history) → `.logs/`
  - Procedural memory (how to operate; roles; constraints) → `AGENTS.md`, `.canon/policies/`, `.canon/roles/`, (optional) `.github/agents/`

- Dedicated Navigation Path (DNP): agents must navigate deterministically using a small set of canonical entrypoints. Scanning the repo arbitrarily is prohibited; use only the approved refresh tool (see POLICY__dedicated-navigation-path__v1.md).

- Governance-as-constraint: enforce policies continuously during Plan → Build → QA. Policies are code (policy-as-code) and must be consulted programmatically where possible.

- Machine-usable outputs: artifacts intended for programmatic gating must use schemas (JSON Schema) or SARIF (for code audit findings). Human prose is acceptable for context, but gates rely on structured outputs.

Why these matter
-----------------

- Reduces context-window waste by presenting only high-signal context to LLM agents.
- Prevents instruction drift by making procedure and authority explicit and versioned.
- Enables automated gating (CI, governance) because outputs are machine-validated.

References
----------

- See role profiles under `docs/` and `.canon/roles/` for responsibilities (`general_role_profile__senior_context_architect.txt`, `02_Prompt_Engineer_*.txt`, `01_LLM_Data_Scientist_*.txt`).
- See builder CLI (`builder.py`) for supported commands: `generate`, `validate`, `validate-kit`, `external`.

Operational notes
-----------------

- When starting a task follow the DNP read order (root `AGENTS.md` → `.canon/navigator/README.md` → `.canon/policies/POLICY__dedicated-navigation-path__v1.md` → relevant `.canon/*`).
- Always write append-only logs under `.logs/` for navigation, decisions, tests, and changes.
- Prefer read-only analysis; any write must be minimal, justified, and recorded in `.logs/navigation/` or `.logs/decisions/`.

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
