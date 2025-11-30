"""
# 백준
# No. 11660
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    Q = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

    # Logic
    S = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        S[i][1] = S[i - 1][1] + A[i - 1][0]
        S[1][i] = S[1][i - 1] + A[0][i - 1]

    for i in range(2, N + 1):
        for j in range(2, N + 1):
            S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] + A[i - 1][j - 1]

    # Output
    for x1, y1, x2, y2 in Q:
        print(S[x2][y2] - S[x1 - 1][y2] - S[x2][y1 - 1] + S[x1 - 1][y1 - 1])


if __name__ == "__main__":
    main()
