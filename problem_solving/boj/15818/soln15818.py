"""
# 백준
# No. 15818
# Python 3.11.9
# by "nno0obb"
"""

from functools import reduce


def main():
    # Input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # Logic
    ans = reduce(lambda x, y: (x % M) * (y % M) % M, A, 1) % M

    # Output
    print(ans)


if __name__ == "__main__":
    main()
