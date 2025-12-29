"""
# 백준
# No. 5637
# Python 3.11.9
# by "nno0obb"
"""

import re


def main():
    # Input
    lines = []
    while True:
        try:
            lines.append(input().strip())
        except EOFError:
            break

    # Logic
    lines[-1] = lines[-1].rstrip("E-N-D")
    text = re.sub(r"[^a-zA-Z-]", " ", " ".join(lines))
    words = text.split()
    ans = sorted(list(zip(words, range(len(words)))), key=lambda x: (-len(x[0]), x[1]))[0][0].lower()

    # Output
    print(ans)


if __name__ == "__main__":
    main()
