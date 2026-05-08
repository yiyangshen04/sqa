import subprocess
import sys


def test_calculator_cli_adds_two_numbers():
    result = subprocess.run(
        [sys.executable, "-m", "week7.calculator", "2", "3"],
        capture_output=True,
        check=True,
        text=True,
    )

    assert result.stdout.strip() == "5"
