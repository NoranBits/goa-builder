#!/usr/bin/env python3
"""Simple placeholder Code Auditor that emits a minimal SARIF 2.1.0 file.

Intended as a first-class CI signal for GitHub Code Scanning in `goa-code-audit`.
Replace this with your real analyzer in future iterations.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


def sarif_stub(tool_name: str, out_path: Path) -> None:
    now = datetime.now(timezone.utc).isoformat()
    sarif = {
        "version": "2.1.0",
        "runs": [
            {
                "tool": {"driver": {"name": tool_name, "informationUri": "https://example.org/goa"}},
                "results": [],
                "invocations": [{"startTimeUtc": now}],
            }
        ],
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(sarif, indent=2), encoding="utf-8")


def write_metadata(meta_path: Path, sarif_path: Path, step_id: str | None) -> None:
    meta = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "sarif_file": str(sarif_path.as_posix()),
        "tool": "goa-code-auditor",
        "category": "goa-code-auditor",
        "step_id": step_id,
    }
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")


def main() -> int:
    root = Path.cwd()
    out_dir = root / ".logs" / "validation"
    sarif_path = out_dir / "code-auditor.sarif.json"
    meta_path = out_dir / "code-auditor.metadata.json"

    # simple stub
    sarif_stub("goa-code-auditor", sarif_path)
    write_metadata(meta_path, sarif_path, None)

    print(f"Wrote SARIF -> {sarif_path}")
    print(f"Wrote metadata -> {meta_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

<!-- md_autofix: processed -->
