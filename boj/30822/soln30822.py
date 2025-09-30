"""
# 백준
# No. 30822
# Python 3.11.9
# by "nno0obb"
"""

from collections import Counter


def main():
    # Input
    N = int(input())
    S = input()

    # Logic
    counter = Counter(S)
    ans = min([counter.get(char, 0) for char in "uospc"])

    # Output
    print(ans)


if __name__ == "__main__":
    main()
