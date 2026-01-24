#!/usr/bin/env python3
import sys
import os

# Proxy wrapper to the kit's root builder.py

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

## Expect the kit's builder.py to live at the repo root

TARGET = os.path.join(ROOT, 'builder.py')

## Fallback: check one level up (in case this kit was nested)

if not os.path.exists(TARGET):
    TARGET = os.path.join(ROOT, '..', 'builder.py')

if not os.path.exists(TARGET):
    sys.exit('[wrapper] cannot find root builder.py')

os.execv(sys.executable, [sys.executable, TARGET] + sys.argv[1:])

<!-- md_autofix: processed -->
