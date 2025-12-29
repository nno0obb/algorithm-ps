"""
# 백준
# No. 13416 
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        ABC = []
        for _ in range(N):
            a, b, c = map(int, sys.stdin.readline().split())
            ABC.append([a, b, c])

        # Logic
        ans = 0
        for a, b, c in ABC:
            ans += max(a, b, c, 0)

        # Output
        print(ans)


if __name__ == "__main__":
    main()
