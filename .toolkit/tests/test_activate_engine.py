import os
import sys
import subprocess
import yaml


def test_activate_engine_dry_run_preserves_active_pointer(tmp_path):
    # Read ACTIVE_ENGINE.yml before
    active_path = os.path.join('.canon', 'modules', 'engine', 'ACTIVE_ENGINE.yml')
    assert os.path.exists(active_path)
    with open(active_path, 'r', encoding='utf-8') as f:
        before = yaml.safe_load(f)

    # Run dry-run activation for unity
    proc = subprocess.run([sys.executable, os.path.join('.toolkit', 'activate_engine.py'), '--engine', 'unity', '--dry-run'], capture_output=True, text=True)
    assert proc.returncode == 0, f"activate_engine.py failed: {proc.stdout}\n{proc.stderr}"
    # output should mention Dry-run
    assert 'DRY-RUN' in proc.stdout or 'Dry-run completed' in proc.stdout

    # Read ACTIVE_ENGINE.yml after and ensure unchanged
    with open(active_path, 'r', encoding='utf-8') as f:
        after = yaml.safe_load(f)
    assert before == after
