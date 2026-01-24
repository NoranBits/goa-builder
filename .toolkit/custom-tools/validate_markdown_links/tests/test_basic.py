import subprocess
import sys
import os


def test_tool_runs():
    here = os.path.dirname(__file__)
    root = os.path.abspath(os.path.join(here, '..'))
    # Run the tool in dry-run mode against its README
    proc = subprocess.run([sys.executable, os.path.join(root, 'tool.py'), '--target', root, '--dry-run'], capture_output=True)
    assert proc.returncode == 0
