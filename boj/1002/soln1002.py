"""
# 백준
# No. 1002 
# Python 3.11.9
# by "nno0obb"
"""

from math import sqrt


def logic(x1, y1, r1, x2, y2, r2):

    d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if d == 0:
        if r1 == r2:
            return -1
        elif r1 != r2:
            return 0

    if d > 0:
        if r1 + r2 < d:
            return 0
        elif r1 + r2 == d:
            return 1
        elif abs(r1 - r2) < d < r1 + r2:
            return 2
        elif abs(r1 - r2) == d:
            return 1
        elif abs(r1 - r2) > d:
            return 0


def main():
    # Input
    T = int(input())
    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())

        # Logic
        ans = logic(x1, y1, r1, x2, y2, r2)

        # Output
        print(ans)


if __name__ == "__main__":
    main()
