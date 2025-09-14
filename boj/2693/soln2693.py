"""
# 백준
# No. 2693
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    T = int(input())
    for _ in range(T):
        A = list(map(int, sys.stdin.readline().split()))

        # Logic
        _3rd = sorted(A)[-3]

        # Output
        print(_3rd)


if __name__ == "__main__":
    main()
