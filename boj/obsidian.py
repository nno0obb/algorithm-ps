import argparse
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

ACCEPT = "text/html;"
ACCEPT_ENCODING = "gzip, deflate, br"
SEC_FETCH_DEST = "document"
SEC_FETCH_MODE = "navigate"
SEC_FETCH_SITE = "none"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--no", type=int, required=True)
    args = parser.parse_args()
    pno = args.no  # Problem No

    headers = {
        "User-Agent": USER_AGENT,
        "Accept": ACCEPT,
        "Accept-Encoding": ACCEPT_ENCODING,
        "Sec-Fetch-Dest": SEC_FETCH_DEST,
        "Sec-Fetch-Mode": SEC_FETCH_MODE,
        "Sec-Fetch-Site": SEC_FETCH_SITE,
        "Referer": f"https://www.acmicpc.net/problem/{pno}",
        "Priority": "u=0, i",
    }
    response = requests.get(f"https://www.acmicpc.net/problem/{pno}", headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find(id="problem_title").text.strip()

    boj_base = Path(__file__).parent / str(pno)
    obsidian_base = Path.home() / "Obsidian" / "nno0obb" / "algorithm" / "ps" / "boj"
    if (boj_base / f"soln{pno}.py").exists():
        with open(boj_base / f"soln{pno}.py", "r", encoding="utf-8") as f:
            with open(obsidian_base / f"{pno}.md", "w", encoding="utf-8") as g:
                code = f.read()
                env = Environment(loader=FileSystemLoader("."))
                template = env.get_template("template.md.j2")
                g.write(template.render(no=pno, title=title, code=code))


if __name__ == "__main__":
    main()
