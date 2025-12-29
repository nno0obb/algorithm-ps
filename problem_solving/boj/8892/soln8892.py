"""
# 백준
# No. 8892
# Python 3.11.9
# by "nno0obb"
"""

import sys
from itertools import combinations


def main():
    # Input
    T = int(input())
    for _ in range(T):
        K = int(input())
        words = [sys.stdin.readline().strip() for _ in range(K)]

        # Logic
        ans = "0"
        for comb in combinations(words, 2):
            w1, w2 = comb
            c1, c2 = w1 + w2, w2 + w1
            if c1 == c1[::-1]:
                ans = c1
                break
            if c2 == c2[::-1]:
                ans = c2
                break

        # Output
        print(ans)


if __name__ == "__main__":
    main()
