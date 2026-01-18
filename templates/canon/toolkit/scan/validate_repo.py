#!/usr/bin/env python3
"""Minimal repository validator producing SCHEMA__structure-audit__v1.json outputs.

This script performs a small set of repository checks and emits a structure-audit JSON.
"""
import argparse
import json
import os
import sys
from datetime import datetime, timezone


def check_path(root, rel_path):
    path = os.path.join(root, rel_path)
    return os.path.exists(path)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--root", default=".", help="Repository root to scan")
    p.add_argument("--out", default="reports/structure-audit.json", help="Output path for the audit JSON")
    p.add_argument("--sarif", default=None, help="Optional SARIF output path")
    args = p.parse_args()

    root = os.path.abspath(args.root)
    violations = []

    # Check for .canon
    if not check_path(root, ".canon"):
        violations.append({
            "severity": "error",
            "path": ".canon",
            "rule_id": "structure.missing_canon",
            "message": "Missing .canon directory",
            "evidence": []
        })

    # Check for AGENTS.md in project root
    if not check_path(root, "AGENTS.md"):
        violations.append({
            "severity": "warn",
            "path": "AGENTS.md",
            "rule_id": "structure.missing_agents_md",
            "message": "AGENTS.md not found at repository root",
            "evidence": []
        })

    # Check for navigator index
    if not check_path(root, "navigator/context-index.json"):
        violations.append({
            "severity": "warn",
            "path": "navigator/context-index.json",
            "rule_id": "navigator.missing_index",
            "message": "Navigator context index missing",
            "evidence": []
        })

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "violations": violations,
    }

    out_path = os.path.abspath(args.out)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    if args.sarif:
        sarif_path = os.path.abspath(args.sarif)
        os.makedirs(os.path.dirname(sarif_path), exist_ok=True)
        sarif = {
            "version": "2.1.0",
            "$schema": "https://schemastore.azurewebsites.net/schemas/json/sarif-2.1.0.json",
            "runs": [
                {
                    "tool": {"driver": {"name": "goa-builder-validate_repo"}},
                    "results": [
                        {
                            "ruleId": v["rule_id"],
                            "message": {"text": v["message"]},
                            "level": v["severity"],
                        }
                        for v in violations
                    ],
                }
            ],
        }
        with open(sarif_path, "w", encoding="utf-8") as f:
            json.dump(sarif, f, indent=2)

    # Exit non-zero if any error severity
    has_error = any(v.get("severity") == "error" for v in violations)
    if has_error:
        print(f"validate_repo: found {len(violations)} issues (blocking). See {out_path}")
        sys.exit(2)
    else:
        print(f"validate_repo: completed with {len(violations)} issue(s). See {out_path}")
        sys.exit(0)


if __name__ == "__main__":
    main()
