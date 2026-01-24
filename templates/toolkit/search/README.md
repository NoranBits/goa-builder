# search

> **Context**: Fast, precise lookup tools for specific code patterns or symbols.

## Purpose

Search tools help agents find needles in the haystack without reading every file.

## Suggested Tools

- **`grep_code.sh`**: optimized wrapper around `git grep` or `rg` (ripgrep).
- **`find_function.py`**: robust symbol search using simple heuristics.
- **`search_docs.py`**: search only markdown/documentation.

## Works Well With

- **`scan/`**: Use scan to find *where* to search.
- **`.canon`**: Search the knowledge base for existing answers.

## Custom Tools

Use `custom-tools/` for regex libraries or fuzzy matchers.

## Safety

- Respect `.gitignore` to avoid finding matches in build artifacts.

## External Context (For Generators)

> **Note**: These links are just examples. Upon scanning the repository and digesting the stack, this section should be updated with accurate external context matching the project.

- **Ripgrep**: [User Guide](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md) - The gold standard for code search performance.
- **Regular Expressions**: [Regex101](https://regex101.com/) - Tool for crafting correct search patterns.
- **Git Grep**: [Docs](https://git-scm.com/docs/git-grep) - Built-in repository search.

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
