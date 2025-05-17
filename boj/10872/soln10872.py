"""
# 백준
# No. 10872 
# Python 3.11.9
# by "nno0obb"
"""

from functools import reduce


def main():
    # Input
    N = int(input())

    # Logic
    ans = reduce(lambda x, y: x * y, range(1, N + 1), 1)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
