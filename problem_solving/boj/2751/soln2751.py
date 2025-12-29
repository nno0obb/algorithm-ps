"""
# 백준
# No. 2751
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N = int(input())
    A = [int(sys.stdin.readline().strip()) for _ in range(N)]

    # Logic
    A.sort()

    # Output
    print(*A, sep="\n")


if __name__ == "__main__":
    main()
