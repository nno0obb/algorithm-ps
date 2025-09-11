"""
# 백준
# No. 1247
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    for _ in range(3):
        N = int(sys.stdin.readline())
        nums = [int(sys.stdin.readline()) for _ in range(N)]

        # Logic
        total = sum(nums)
        ans = "0" if total == 0 else "+" if total > 0 else "-"

        # Output
        print(ans)


if __name__ == "__main__":
    main()
