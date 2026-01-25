#!/usr/bin/env python3
"""Lightweight rolekit <-> project_facts validator.

Checks that `project_facts.json` contains required fields and that a role
manifest YAML contains minimal expected keys. Exits with non-zero on failure.

Usage: python3 tools/validate_rolekit.py --role <role_manifest.yml> --project <.canon/project_facts.json>
"""
import argparse
import json
import sys
from pathlib import Path

try:
    import yaml
except Exception:
    print(json.dumps({"error": "PyYAML required: pip install pyyaml"}))
    sys.exit(2)


def load_json(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--role", required=True)
    p.add_argument("--project", required=True)
    args = p.parse_args()

    errors = []
    # project facts
    proj_path = Path(args.project)
    if not proj_path.exists():
        print(json.dumps({"error": f"project_facts not found: {proj_path}"}))
        sys.exit(2)
    proj = load_json(proj_path)
    for key in ("id", "repo_name", "roles_enabled"):
        if key not in proj:
            errors.append(f"project_facts.json missing '{key}'")

    # role manifest
    role_path = Path(args.role)
    if not role_path.exists():
        errors.append(f"role manifest not found: {role_path}")
    else:
        try:
            role = load_yaml(role_path)
        except Exception as e:
            errors.append(f"error parsing role manifest: {e}")
            role = None
        if role is not None:
            # minimal heuristics: expect 'name' or top-level 'rolekit' metadata
            if not (isinstance(role, dict) and ("name" in role or "rolekit" in role)):
                errors.append("role manifest missing top-level 'name' or 'rolekit' key")

    if errors:
        print(json.dumps({"accepted": False, "errors": errors}, indent=2))
        sys.exit(2)

    print(json.dumps({"accepted": True, "errors": []}))
    sys.exit(0)


if __name__ == "__main__":
    main()
