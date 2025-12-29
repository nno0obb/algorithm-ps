"""
# 백준
# No. 23027
# Python 3.11.9
# by "nno0obb"
"""

import re


def main():
    # Input
    S = input()

    # Logic
    if "A" in S:
        S = re.sub(r"[BCDF]", "A", S)
    elif "B" in S:
        S = re.sub(r"[CDF]", "B", S)
    elif "C" in S:
        S = re.sub(r"[DF]", "C", S)
    else:
        S = re.sub(r".", "A", S)

    # Output
    print(S)


if __name__ == "__main__":
    main()
