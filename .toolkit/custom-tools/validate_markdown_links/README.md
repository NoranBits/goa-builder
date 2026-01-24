## Purpose

This tool scans Markdown files under a target path and reports broken relative links.

## Usage

```bash
python3 tool.py --target docs/ --dry-run true
```

## Risks

- Operates read-only by default. When run without `--dry-run`, ensure `tool.spec.yml` write_scope is correctly set.

## Example

Run a dry-run to see findings, then run without `--dry-run` after review.

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
