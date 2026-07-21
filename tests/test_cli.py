import subprocess
import sys


def test_main_runs():
    result = subprocess.run(
        [sys.executable, "main.py", "--help"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0