## Rolekit PR Checklist

- [ ] `manifest.schema.yml` referenced or updated (if schema change)
- [ ] Each manifest includes `provenance.builder`, `commit`, and `timestamp` (or has justification)
- [ ] `validate_rolekit_schema.py` passes locally or CI in dry-run (`--fix` not run in CI)
- [ ] Any executable tools listed in `tool_usage` are in `.toolkit/custom-tools/` and have a CODEOWNERS entry for review
- [ ] Decision / rationale linked in `.logs/decisions/`
- [ ] License field present in manifest if external code/examples are referenced

Add reviewer note: if this PR includes `--fix` changes, prefer creating a follow-up PR that contains only the auto-fixed manifests and a link to the validation run.

<!-- md_autofix: processed -->
