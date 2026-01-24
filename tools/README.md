tools/ utilities and helpers
=================================

This folder contains small CLI helpers and toolkit utilities used by the
goa-builder kit.

git_commit_helper
-----------------

Small helper to commit changes grouped by top-level path, inspect older commits,
and generate concise summaries for commits. Located at `tools/git_commit_helper.py`.

Examples:

```text
python3 tools/git_commit_helper.py --group-commit --push
python3 tools/git_commit_helper.py --dry-run --group-commit
python3 tools/git_commit_helper.py --show-old HEAD~1
```

Use `--dry-run` to preview actions before allowing the tool to stash/apply/commit.

New flags:

- `--include-diffs`: Include small unified-diff excerpts for changed files in the commit message.
- `--max-diff-lines N`: Maximum number of diff lines to include per file (default 200).
- `--diff-files-limit N`: Maximum number of files to include diffs for per group (default 3).

Example including diffs:

```text
python3 tools/git_commit_helper.py --group-commit --include-diffs --max-diff-lines 120 --diff-files-limit 2
```

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
