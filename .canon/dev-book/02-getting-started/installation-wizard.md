# Installation Wizard (Builder)

## Purpose

Provide a deterministic, confirmation-driven “installer” workflow for setting up the GOA Builder in a new or existing repository.

This is an interaction pattern, not an external dependency: the wizard can be followed by a human, or used as a structured prompt for an agent.

## Inputs

- Target repository root path.
- Project constraints: engine, language(s), build tools, platforms.
- Governance constraints: logging/audit expectations, safety rules, required validators.

## Outputs

- A generated `.canon/**` knowledge base.
- A generated `.toolkit/**` tool surface.
- A stable VS Code validation task (`validate:markdownlint`).

## Wizard flow (Decision Card at every write)

1. **Detect**

   - Locate entry points (packages, build scripts, CI).
   - Identify languages and tooling (Node, Python, Rust, etc.).
   - Identify high-signal constraints (monorepo, game engine, asset pipeline).

1. **Align**

   - Read the nearest `AGENTS.md` gate for any file you plan to edit.
   - Confirm what the repo treats as authoritative documentation.
   - Confirm what is considered “generated” vs “source-of-truth”.

1. **Generate**

   - Run `python3 .builder/builder.py generate`.
   - Confirm the created scaffolds: `.canon/**`, `.toolkit/**`.

1. **Validate**

   - Run `python3 .builder/builder.py validate-kit`.
   - Run `python3 .builder/builder.py validate`.

1. **Adapt**

   - Add small, repo-specific notes to `.canon/**` (never guess).
   - Add new tools only under `.toolkit/**/custom-tools/` until proven.

## Confirmation checklist

- Are we allowed to modify root governance files (like `AGENTS.md`)?
- What must remain unchanged (agent/chatmode counts, CI contracts, etc.)?
- Where should runtime logs go (`.logs/`, `.local/`, or a repo-specific path)?

## Failure modes

- If validation fails, fix the root cause instead of excluding failing files.
- If a policy conflict exists (for example, docs vs `.canon`), stop and request human resolution.

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
