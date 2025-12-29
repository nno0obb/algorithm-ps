"""
# 백준
# No. 13877
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    T = int(input())
    for _ in range(T):
        K, S = sys.stdin.readline().split()

        # Logic
        try:
            _8 = int(S, 8)
        except ValueError:
            _8 = "0"
        _10 = int(S)
        _16 = int(S, 16)

        # Output
        print(K, _8, _10, _16)


if __name__ == "__main__":
    main()
