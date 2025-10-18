"""
# 백준
# No. 2121
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N = int(input())
    A, B = map(int, input().split())
    C = set()
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        C.add((x, y))

    # Logic
    ans = 0
    for c in C:
        x, y = c
        if (x, y + B) in C and (x + A, y) in C and (x + A, y + B) in C:
            ans += 1

    # Output
    print(ans)


if __name__ == "__main__":
    main()
