"""
# 백준
# No. 10801
# Python 3.11.9
# by "nno0obb"
"""

from functools import reduce


def main():
    # Input
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Logic
    A_win = reduce(lambda acc, x: acc + int(x[0] > x[1]), zip(A, B), 0)
    B_win = reduce(lambda acc, x: acc + int(x[0] < x[1]), zip(A, B), 0)

    # Output
    print("A" if A_win > B_win else "B" if A_win < B_win else "D")


if __name__ == "__main__":
    main()
