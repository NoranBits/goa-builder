# Markdown Policy (Project Root)

This repository uses strict Markdown rules.

## Rules (summary)

- Surround headings with a blank line (before and after).
- Surround lists with a blank line (before the first item, after the last item).
- Surround fenced code blocks with a blank line.
- Fenced code blocks MUST specify a language (use `text` if unsure).
- Avoid bare URLs; use Markdown links.
- Files MUST end with exactly one trailing newline.

## Enforcement

- Install lint tool:

```bash
npm install --save-dev markdownlint-cli2
```

- Run validation:

```bash
python3 .builder/tools/run_markdownlint.py
```

- Or run VS Code task: `validate:markdownlint`

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
