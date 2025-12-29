"""
# 백준
# No. 32642
# Python 3.11.9
# by "nno0obb"
"""

from functools import reduce


def main():
    # Input
    N = int(input())
    W = list(map(int, input().split()))

    # Logic
    ans = reduce(lambda acc, x: acc + {1: +1, 0: -1}[x[1]] * (N - x[0]), enumerate(W), 0)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
