"""
# 백준
# No. 14648
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N, _Q = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    Q = [list(map(int, sys.stdin.readline().split())) for _ in range(_Q)]

    # Logic
    for q in Q:
        if q[0] == 1:
            a, b = q[1], q[2]
            A[a], A[b] = A[b], A[a]

            # Output
            print(sum(A[a : b + 1]))

        if q[0] == 2:
            a, b, c, d = q[1], q[2], q[3], q[4]

            # Output
            print(sum(A[a : b + 1]) - sum(A[c : d + 1]))


if __name__ == "__main__":
    main()
