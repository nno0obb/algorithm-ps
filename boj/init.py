import argparse
import os
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader

load_dotenv()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--no", type=int, required=True)
    args = parser.parse_args()
    pno = args.no  # Problem No

    base_path = Path(__file__).parent / str(pno)
    base_path.mkdir(parents=True, exist_ok=True)
    if not (base_path / f"soln{pno}.py").exists():
        with open(base_path / f"soln{pno}.py", "w", encoding="utf-8") as f:
            env = Environment(loader=FileSystemLoader("."))
            template = env.get_template("template.py.j2")
            f.write(template.render(no=pno))
    # if not (base_path / f"soln{pno}.go").exists():
    #     with open(base_path / f"soln{pno}.go", "w", encoding="utf-8") as f:
    #         env = Environment(loader=FileSystemLoader("."))
    #         template = env.get_template("template.go.j2")
    #         f.write(template.render(no=pno))

    (base_path / "inputs").mkdir(parents=True, exist_ok=True)
    (base_path / "outputs").mkdir(parents=True, exist_ok=True)
    base_url = "https://acmicpc.net"
    headers = {
        "User-Agent": os.getenv("USER_AGENT"),
        "Accept": os.getenv("ACCEPT"),
        "Accept-Encoding": os.getenv("ACCEPT_ENCODING"),
        "Sec-Fetch-Dest": os.getenv("SEC_FETCH_DEST"),
        "Sec-Fetch-Mode": os.getenv("SEC_FETCH_MODE"),
        "Sec-Fetch-Site": os.getenv("SEC_FETCH_SITE"),
        "Priority": os.getenv("PRIORITY"),
        "Referer": f"{base_url}/problem/{pno}",
    }
    response = requests.get(f"{base_url}/problem/{pno}", headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    for _, tag in enumerate(soup.find_all("pre")):
        if tag.has_attr("id"):
            if tag["id"].startswith("sample-input"):
                tcno = tag["id"].split("-")[-1]  # TestCase No
                with open(base_path / "inputs" / f"input{tcno}", "w", encoding="utf-8") as f:
                    f.write(tag.text.strip("\n").strip("\r"))
            elif tag["id"].startswith("sample-output"):
                tcno = tag["id"].split("-")[-1]  # TestCase No
                with open(base_path / "outputs" / f"output{tcno}", "w", encoding="utf-8") as f:
                    f.write(tag.text.strip("\n").strip("\r"))


if __name__ == "__main__":
    main()
