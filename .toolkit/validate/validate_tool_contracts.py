#!/usr/bin/env python3
"""
validate_tool_contracts.py

Lightweight validator for tool.spec.yml contracts.

Checks performed:
- required fields exist
- write_scope does not contain wildcard global scopes
- README.md exists and contains required sections
- tool entrypoint exists

Usage: python3 validate_tool_contracts.py /path/to/tooldir
"""
import sys
import os
import re
import json

try:
    import yaml
except Exception:
    yaml = None

REQ_FIELDS = ["tool_id", "version", "permissions", "inputs_schema", "entrypoint"]
REQUIRED_README_SECTIONS = ["## Purpose", "## Usage", "## Risks", "## Example"]


def load_yaml(path):
    if yaml:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    else:
        raise RuntimeError("PyYAML is required to run this validator. Install with: pip install pyyaml")


def has_wildcard_write_scope(write_scope):
    if not write_scope:
        return False
    for s in write_scope:
        if s.strip() == "**/*" or s.strip() == "*" or s.strip().startswith("/") or "**" in s or s.strip() == "/":
            return True
    return False


def check_readme(tool_path):
    readme = os.path.join(tool_path, "README.md")
    if not os.path.isfile(readme):
        return False, "README.md not found"
    text = open(readme, "r", encoding="utf-8").read()
    missing = [s for s in REQUIRED_README_SECTIONS if s not in text]
    if missing:
        return False, f"Missing README sections: {missing}"
    return True, "OK"


def validate(tool_path):
    spec_path = os.path.join(tool_path, "tool.spec.yml")
    if not os.path.isfile(spec_path):
        print(json.dumps({"ok": False, "error": "tool.spec.yml missing", "path": tool_path}))
        return 2

    try:
        spec = load_yaml(spec_path)
    except Exception as e:
        print(json.dumps({"ok": False, "error": f"YAML load error: {e}"}))
        return 2

    missing = [f for f in REQ_FIELDS if f not in spec]
    if missing:
        print(json.dumps({"ok": False, "error": f"Missing fields: {missing}"}))
        return 2

    write_scope = spec.get("permissions", {}).get("write_scope")
    if has_wildcard_write_scope(write_scope):
        print(json.dumps({"ok": False, "error": "Wildcard or global write_scope forbidden"}))
        return 3

    # README check
    ok, msg = check_readme(tool_path)
    if not ok:
        print(json.dumps({"ok": False, "error": msg}))
        return 4

    # entrypoint check
    entry = spec.get("entrypoint")
    entry_path = os.path.join(tool_path, entry)
    if not os.path.isfile(entry_path):
        print(json.dumps({"ok": False, "error": f"entrypoint not found: {entry}"}))
        return 5

    print(json.dumps({"ok": True, "tool_id": spec.get("tool_id"), "version": spec.get("version")}))
    return 0


def main(argv):
    if len(argv) < 2:
        print("Usage: validate_tool_contracts.py /path/to/tooldir")
        return 1
    path = argv[1]
    return validate(path)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
