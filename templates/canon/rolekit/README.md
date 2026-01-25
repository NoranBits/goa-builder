# Rolekit — manifest spec (templates/canon/rolekit)

Purpose
-------
This folder provides the Rolekit manifest schema and examples used to bootstrap
` .canon/rolekit/` in projects. A Rolekit manifest is a machine-readable contract
that describes an agent role (identity, capabilities, runtime hints, and provenance).

Location & Usage
------------------

- Template schema: `templates/canon/rolekit/manifest.schema.yml`
- Project manifests should live under `.canon/rolekit/` (one YAML per role).
- Human-readable playbooks remain under `.canon/roles/*.role.md`.

Naming & Versioning
-------------------

- Role `name` must be snake_case, lowercase (regex: `^[a-z0-9_]+$`).
- `version` uses semantic versioning `MAJOR.MINOR.PATCH`.
- `level` must be one of `L0`, `L1`, `L2`.

Key fields
----------

- `spec.skills` — dot-notation capability ids (e.g., `code.generation.unity.csharp`).
- `provenance` — minimal SLSA-style provenance (builder id, commit, timestamp).
- `canon_refs` — relative paths to `.canon/` artifacts the role uses or produces.

Guidelines
----------

- Keep manifests concise; put operational details and examples in `.canon/roles/*.role.md`.
- Use the validator `.toolkit/validate/validate_rolekit_schema.py` before merging changes.
- Declarative by default: executable scripts must be listed in `tool_usage` and placed

  under `.toolkit/custom-tools/` and require explicit promotion in AGENTS.md.

<!-- md_autofix: processed -->
