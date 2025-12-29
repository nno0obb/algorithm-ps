"""
# 백준
# No. 1377
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N = int(input())
    A = [int(sys.stdin.readline()) for _ in range(N)]

    # Logic
    S = [(num, i1) for i1, num in enumerate(A)]
    S.sort()

    ans = 0
    for i2, (num, i1) in enumerate(S):
        ans = max(ans, i1 - i2 + 1)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
