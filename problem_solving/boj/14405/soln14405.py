"""
# 백준
# No. 14405
# Python 3.11.9
# by "nno0obb"
"""

import re


def main():
    # Input
    S = input()

    # Logic
    ans = "YES" if re.fullmatch(r"^(pi|ka|chu)*$", S) else "NO"

    # Output
    print(ans)


if __name__ == "__main__":
    main()
