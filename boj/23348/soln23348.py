"""
# 백준
# No. 23348
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    A, B, C = map(int, input().split())
    N = int(input())
    D = [[map(int, sys.stdin.readline().split()) for _ in range(3)] for _ in range(N)]

    # Logic
    ans = -1
    for d in D:
        score = 0
        for a, b, c in d:
            score += a * A + b * B + c * C
        ans = max(ans, score)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
