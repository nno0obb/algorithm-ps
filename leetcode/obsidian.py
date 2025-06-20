import argparse
import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

with open("data.json", "r", encoding="utf-8") as h:
    data = json.load(h)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--no", type=int, required=True)
    args = parser.parse_args()
    pno = args.no  # Problem No
    pslug = data[str(pno)]

    leetcode_base = Path(__file__).parent / f"{pno}-{pslug}"
    obsidian_base = Path.home() / "Obsidian" / "nno0obb" / "algorithm" / "ps" / "leetcode"
    if (leetcode_base / f"soln{pno}.py").exists():
        with open(leetcode_base / f"soln{pno}.py", "r", encoding="utf-8") as f:
            with open(obsidian_base / f"{pno}-{pslug}.md", "w", encoding="utf-8") as g:
                code = f.read()
                env = Environment(loader=FileSystemLoader("."))
                template = env.get_template("template.md.j2")
                g.write(template.render(no=pno, title=pslug, code=code))


if __name__ == "__main__":
    main()
