from pathlib import Path


def pytest_addoption(parser):
    parser.addoption("--no", action="store", default=None, help="NO")


def get_test_cases(no):
    base = Path(__file__).parent / str(no)
    inputs = list(map(lambda x: x.read_text().strip(), sorted((base / "inputs").iterdir())))
    outputs = list(map(lambda x: x.read_text().strip(), sorted((base / "outputs").iterdir())))
    return [(no, x, y) for x, y in zip(inputs, outputs)]


def pytest_generate_tests(metafunc):
    pno = metafunc.config.getoption("no")  # Problem No
    if "no" in metafunc.fixturenames and pno is not None:
        test_cases = get_test_cases(pno)
        ids = [f"{pno}-#{tcno}" for tcno in range(1, len(test_cases) + 1)]
        metafunc.parametrize("no, input, output", test_cases, ids=ids)
