#!/usr/bin/env python3
"""
validate_logs.py

Checks per-tool NDJSON changelogs for valid JSON lines and required fields.
"""
import json
import glob
import sys

required = ["ts", "change_id"]


def check_file(path):
    ok = True
    with open(path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except Exception as e:
                print(f"{path}:{i}: invalid json: {e}")
                ok = False
                continue
            for k in required:
                if k not in obj:
                    print(f"{path}:{i}: missing required key: {k}")
                    ok = False
    return ok


def main():
    files = glob.glob('.logs/tools/**/CHANGELOG.ndjson', recursive=True)
    if not files:
        print('No changelogs found under .logs/tools/')
        return 1
    overall = True
    for p in files:
        ok = check_file(p)
        overall = overall and ok
    return 0 if overall else 2


if __name__ == '__main__':
    sys.exit(main())
