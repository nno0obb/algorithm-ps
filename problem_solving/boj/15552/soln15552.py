"""
# 백준
# No. 15552 
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    T = int(input())
    for _ in range(T):
        A, B = map(int, sys.stdin.readline().split())

        # Logic
        ans = A + B

        # Output
        print(ans)


if __name__ == "__main__":
    main()
