"""
# 백준
# No. 1924
# Python 3.11.9
# by "nno0obb"
"""

from datetime import datetime


def main():
    # Input
    x, y = map(int, input().split())

    # Logic
    ans = datetime(year=2007, month=x, day=y).strftime("%a").upper()

    # Output
    print(ans)


if __name__ == "__main__":
    main()
