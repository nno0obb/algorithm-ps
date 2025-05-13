"""
# 백준
# No. 10989
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N = int(sys.stdin.readline())
    lst = [0] * (10_000 + 1)
    for _ in range(N):
        n = int(sys.stdin.readline())

        # Logic
        lst[n] += 1

    # Output
    for i in range(1, 10_000 + 1):
        for _ in range(lst[i]):
            print(i)


if __name__ == "__main__":
    main()
