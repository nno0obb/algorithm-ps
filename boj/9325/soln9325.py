"""
# 백준
# No. 9325
# Python 3.11.9
# by "nno0obb"
"""

import sys
from functools import reduce


def main():
    # Input
    T = int(sys.stdin.readline())
    for _ in range(T):
        S = int(sys.stdin.readline())
        N = int(sys.stdin.readline())
        A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

        # Logic
        ans = S + reduce(lambda x, y: x + y[0] * y[1], A, 0)

        # Output
        print(ans)


if __name__ == "__main__":
    main()
