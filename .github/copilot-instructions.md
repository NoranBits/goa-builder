<!-- Short, actionable guidance for AI coding agents working in this repository -->

# Copilot instructions — goa-builder

Purpose: give AI coding agents concise, repo-specific rules so they can be productive and safe.

- **Read-before-change:** always locate and read the nearest `AGENTS.md` before editing a folder. The canonical examples live under `templates/` (e.g. [templates/canon/AGENTS.md](templates/canon/AGENTS.md#L1)).

- **Source of truth:** `.canon` holds policies, schemas, and canonical artifacts. Prefer updating `.canon` (not ad-hoc docs) when changing policies or contracts.

- **Append-only logs:** write session notes, navigation traces, and decisions as new entries under `.logs/navigation/`, `.logs/decisions/`, and `.logs/changes/`. Do not rewrite or delete historical log entries.

- **Safe-by-default edits:** prefer read-only analysis. Any write must be minimal, localized, and justified in `.logs/navigation/` with the files inspected and the reason for the write.

- **Tooling conventions:** `.toolkit` scripts must be idempotent and documented. See [templates/toolkit/AGENTS.md](templates/toolkit/AGENTS.md#L1) for examples. When creating or modifying scripts, document inputs/outputs in the nearest `README.md`.

- **Hydration & validation commands (explicit examples):**
  - Hydrate builder payload: `python3 bootstrap.py /path/to/target` ([bootstrap.py](bootstrap.py#L1)).
  - Validate markdown templates: `npm run validate-md` (see [package.json](package.json#L1)).

- **Navigation & generated helpers:** `builder.py` contains heuristics for navigator pages and a gitignore block for `.logs/` — consult it when adding navigation or log rules ([builder.py](builder.py#L1)).

- **Naming & placement invariants:** engine templates and engine-toolkit assets are expected at `.canon/modules/engine/` and `.toolkit/modules/engine/` (see templates and docs). Preserve those install slots when adding engine templates.

- **Structured outputs & prompts:** prefer schema-first outputs and prompt modules found in `templates/canon/` (schemas, prompts, roles). Follow examples in `templates/canon/schemas` and `templates/canon/roles` when adding or validating contract files.

- **Decision & change flow:** if a change affects behavior, add a decision record under `.logs/decisions/` and update `.canon/` accordingly; record short rationale and links to changed files.

- **Tests/build:** this repo provides a minimal lint task for templates; there is no implicit long-running build. Ask maintainers before adding heavy CI or test tasks.

- **When unsure:** record investigative steps in `.logs/navigation/` and open a short ADR in `.logs/decisions/` or request human review via a PR. Prefer small iterative changes.

If any of these items are unclear or you'd like more examples (specific files, workflows, or tests), say which area to expand and I'll update this guidance.

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
