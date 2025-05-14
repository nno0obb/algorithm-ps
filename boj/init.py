import argparse
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

ACCEPT = "text/html;"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--no", type=int, required=True)
    args = parser.parse_args()
    pno = args.no  # Problem No

    base = Path(__file__).parent / str(pno)
    (base / "inputs").mkdir(parents=True, exist_ok=True)
    (base / "outputs").mkdir(parents=True, exist_ok=True)
    if not (base / f"soln{pno}.py").exists():
        with open(base / f"soln{pno}.py", "w", encoding="utf-8") as f:
            env = Environment(loader=FileSystemLoader("."))
            template = env.get_template("template.py.j2")
            f.write(template.render(no=pno))

    headers = {"User-Agent": USER_AGENT, "Accept": ACCEPT}
    response = requests.get(f"https://www.acmicpc.net/problem/{pno}", headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    for _, tag in enumerate(soup.find_all("pre")):
        if tag.has_attr("id"):
            if tag["id"].startswith("sample-input"):
                tcno = tag["id"].split("-")[-1]  # TestCase No
                with open(base / "inputs" / f"input{tcno}", "w", encoding="utf-8") as f:
                    f.write(tag.text.strip())
            elif tag["id"].startswith("sample-output"):
                tcno = tag["id"].split("-")[-1]  # TestCase No
                with open(base / "outputs" / f"output{tcno}", "w", encoding="utf-8") as f:
                    f.write(tag.text.strip())


if __name__ == "__main__":
    main()
