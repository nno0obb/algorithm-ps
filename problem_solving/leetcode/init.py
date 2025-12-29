import argparse
import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

with open("data.json", "r", encoding="utf-8") as g:
    data = json.load(g)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--no", type=int, required=True)
    args = parser.parse_args()
    pno = args.no  # Problem No
    pslug = data[str(pno)]

    base_path = Path(__file__).parent / f"{pno}-{pslug}"
    base_path.mkdir(parents=True, exist_ok=True)
    if not (base_path / f"soln{pno}.py").exists():
        with open(base_path / f"soln{pno}.py", "w", encoding="utf-8") as f:
            env = Environment(loader=FileSystemLoader("."))
            template = env.get_template("template.py.j2")
            f.write(template.render(no=pno, slug=pslug))


if __name__ == "__main__":
    main()
