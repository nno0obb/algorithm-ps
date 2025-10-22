"""
# 백준
# No. 13311
# Python 3.11.9
# by "nno0obb"
"""

from functools import reduce
from math import lcm


def main():
    # Logic
    ans = reduce(lcm, range(2, 1000 + 1), 1) - 1  # 433자리
    ans = -1  # n ≡ a-1 ≡ -1 (mod a)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
