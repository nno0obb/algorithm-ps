"""
# 백준
# No. 1669
# Python 3.11.9
# by "nno0obb"
"""

from math import sqrt


def main():
    # Input
    X, Y = map(int, input().split())

    # Logic
    D = Y - X
    N = int(sqrt(D))

    ans = -1
    if D == 0:
        ans = 0
    elif D == N * N:
        ans = N * 2 - 1
    elif D <= N * (N + 1):
        ans = N * 2
    else:
        ans = N * 2 + 1

    # Output
    print(ans)

    # Hint
    # 0 - 0 (0)
    # 1 - 1 (1)
    # 1 1 - 2 (2)
    # 1 2 1 - 4 (3)
    # 1 2 2 1 - 6 (4)
    # 1 2 3 2 1 - 9 (5)
    # 1 2 3 3 2 1 - 12 (6)
    # 1 2 3 4 3 2 1 - 16 (7)
    # 1 2 3 4 4 3 2 1 - 20 (8)
    # 1 2 3 4 5 4 3 2 1 - 25 (9)


if __name__ == "__main__":
    main()
