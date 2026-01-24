#!/usr/bin/env python3
"""
validate_ingestion.py

Validates ingestion NDJSON files under `.logs/ingestion/`.

Checks:
- presence of `.logs/ingestion/user-intents.ndjson`
- each non-empty line is valid JSON and contains required keys: `ts`, `task_id`, `user_hash`, `snippet`
"""
import glob
import json
import os
import sys

REQUIRED = ["ts", "task_id", "user_hash", "snippet"]


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
            for k in REQUIRED:
                if k not in obj:
                    print(f"{path}:{i}: missing required key: {k}")
                    ok = False
    return ok


def main():
    path = os.path.join('.logs', 'ingestion', 'user-intents.ndjson')
    if not os.path.isfile(path):
        print(f"Missing ingestion file: {path}")
        return 2
    ok = check_file(path)
    return 0 if ok else 3


if __name__ == '__main__':
    sys.exit(main())
