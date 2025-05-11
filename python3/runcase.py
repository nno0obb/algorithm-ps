import subprocess
from pathlib import Path


def test_case(no, _input, output):
    solution = Path(__file__).parent / no / f"{no}.py"
    assert subprocess.check_output(["python3", solution], input=_input, text=True).strip() == output
