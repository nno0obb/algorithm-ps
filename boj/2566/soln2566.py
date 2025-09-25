"""
# 백준
# No. 2566
# Python 3.11.9
# by "nno0obb"
"""

from itertools import chain


def main():
    # Input
    M = [list(map(int, input().split())) for _ in range(9)]

    # Logic
    F = list(chain.from_iterable(M))
    max_idx, max_val = max(enumerate(F), key=lambda x: x[1])
    max_row, max_col = max_idx // 9 + 1, max_idx % 9 + 1

    # Output
    print(max_val)
    print(max_row, max_col)


if __name__ == "__main__":
    main()
