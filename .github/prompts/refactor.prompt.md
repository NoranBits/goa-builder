# Refactor prompt template

Task: |
  <Short statement of what to refactor>

Context: |

  - Provide the exact code snippet or path and any test commands to verify

Constraints: |

  - Preserve external behavior
  - Keep changes minimal and reversible
  - Provide tests or ensure existing tests still pass

Deliverables: |

  - Patch diff or modified file
  - Short rationale and complexity note

OutputFormat: json

Example:
```text
{
  "patch": "diff --git a/src/foo.py b/src/foo.py\n...",
  "rationale": "Reduced allocations by reusing buffer",
  "tests": ["pytest tests/test_foo.py"]
}
```

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
