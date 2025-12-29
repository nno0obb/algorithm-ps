import subprocess
from pathlib import Path


def test_case(no, input, output, request):
    solution = Path(__file__).parent / no / f"soln{no}.py"

    rel_err = request.config.getoption("--relative-error")
    if rel_err is not None:
        rel_err = eval(rel_err)  # eval("10**-2")
        sol_output = float(subprocess.check_output(["python3", solution], input=input, text=True).strip())
        ans_output = float(output)
        assert abs(sol_output - ans_output) <= rel_err
    else:
        sol_output = subprocess.check_output(["python3", solution], input=input, text=True).strip()
        ans_output = output
        assert sol_output == ans_output
