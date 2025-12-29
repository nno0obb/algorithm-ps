"""
# 백준
# No. 11659
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    Q = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

    # Logic
    S = [0] * (N + 1)
    S[1] = A[0]
    for i in range(2, N + 1):
        S[i] = S[i - 1] + A[i - 1]

    # Output
    for i, j in Q:
        print(S[j] - S[i - 1])


if __name__ == "__main__":
    main()
