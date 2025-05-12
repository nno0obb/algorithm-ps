import subprocess
from pathlib import Path


def test_case(no, input, output):
    solution = Path(__file__).parent / no / f"soln{no}.py"
    assert subprocess.check_output(["python3", solution], input=input, text=True).strip() == output
