"""
# 백준
# No. 2139
# Python 3.11.9
# by "nno0obb"
"""

from datetime import date


def main():
    # Input
    while True:
        day, month, year = map(int, input().split())
        if (day, month, year) == (0, 0, 0):
            break

        # Logic
        ans = int(date(year, month, day).strftime("%j"))

        # Output
        print(ans)


if __name__ == "__main__":
    main()
