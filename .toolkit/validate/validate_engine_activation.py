#!/usr/bin/env python3
"""
validate_engine_activation.py

Validator enforcing the one-engine invariant and ACTIVE_ENGINE pointer consistency.

Checks:
- `.canon/modules/engine/ACTIVE_ENGINE.yml` exists and contains `engine: <id|none>`
- If engine == 'none': no active engine directories must exist under `.canon/modules/engine/` (except `_retired`)
- If engine == '<id>': the directory `.canon/modules/engine/<id>/` must exist and exactly one active engine directory should be present (excluding `_retired` and special files)
"""
import os
import sys
import glob
import json

try:
    import yaml
except Exception:
    yaml = None


def load_active(path):
    p = os.path.join(path, 'ACTIVE_ENGINE.yml')
    if not os.path.isfile(p):
        return None, f"Missing {p}"
    if yaml:
        with open(p, 'r', encoding='utf-8') as f:
            doc = yaml.safe_load(f)
        return doc.get('engine'), None
    # fallback simple parser
    with open(p, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip().startswith('engine:'):
                return line.split(':', 1)[1].strip().strip('"\'"'), None
    return None, 'No engine key found'


def list_engine_dirs(path):
    entries = []
    if not os.path.isdir(path):
        return entries
    for name in os.listdir(path):
        if name in ('ACTIVE_ENGINE.yml', '_retired'):
            continue
        full = os.path.join(path, name)
        if os.path.isdir(full):
            entries.append(name)
    return entries


def main():
    base = os.path.join('.canon', 'modules', 'engine')
    engine, err = load_active(base)
    if err:
        print(json.dumps({"ok": False, "error": err}))
        return 2

    dirs = list_engine_dirs(base)

    if engine in (None, ''):
        print(json.dumps({"ok": False, "error": "ACTIVE_ENGINE.yml missing or invalid engine value"}))
        return 3

    if engine == 'none':
        if dirs:
            print(json.dumps({"ok": False, "error": "Engine pointer is 'none' but engine directories exist: %s" % dirs}))
            return 4
        print(json.dumps({"ok": True, "engine": "none", "active_dirs": dirs}))
        return 0

    # engine is set to a value
    if engine not in dirs:
        print(json.dumps({"ok": False, "error": f"ACTIVE_ENGINE.yml points to '{engine}' but directory '.canon/modules/engine/{engine}/' not found", "dirs": dirs}))
        return 5

    # ensure only one active engine dir exists (excluding retired)
    if len(dirs) > 1:
        # allow multiple retired entries but not multiple active ones
        print(json.dumps({"ok": False, "error": "Multiple active engine directories found", "dirs": dirs}))
        return 6

    print(json.dumps({"ok": True, "engine": engine, "active_dirs": dirs}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
