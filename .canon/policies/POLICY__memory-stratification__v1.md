# POLICY: Memory Stratification v1

Purpose
-------
Define where different classes of knowledge and artifacts must live so agents can find authoritative sources without scanning indiscriminately.

Mapping
-------

- Semantic memory (authoritative truth) → `.canon/`
  - long-form specs, policies, schemas, runbooks, role definitions
- Episodic memory (append-only history) → `.logs/`
  - sessions, navigation runs, decisions, test/audit outputs, changes
- Procedural memory (how to operate; roles; constraints) → `AGENTS.md`, `.canon/policies/`, `.canon/roles/`, and optionally `.github/agents/`

Guidelines
----------

- Writes to `.canon/` are controlled and must be accompanied by a decision record in `.logs/decisions/`.
- `.logs/` is append-only: never rewrite existing entries; add new records instead.
- `.github/agents/` (optional) is a Copilot-friendly projection of procedural roles; `.canon/roles/` remains the authoritative long-form source.

Rationale
---------
Separation reduces context-window waste, prevents instruction drift, and enables programmatic gating by making authoritative sources easy to locate and validate.

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
