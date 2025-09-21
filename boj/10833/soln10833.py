"""
# 백준
# No. 10833
# Python 3.11.9
# by "nno0obb"
"""

from functools import reduce


def main():
    # Input
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    # Logic
    ans = reduce(lambda x, y: x + y[1] % y[0], A, 0)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
