"""
# 백준
# No. 8320
# Python 3.11.9
# by "nno0obb"
"""

from math import sqrt


def main():
    # Input
    N = int(input())

    # Logic
    ans = 0
    for i in range(1, int(sqrt(N)) + 1):
        for j in range(i, N + 1):
            if i * j <= N:
                ans += 1

    # Output
    print(ans)


if __name__ == "__main__":
    main()
