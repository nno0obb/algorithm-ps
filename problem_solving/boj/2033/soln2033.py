"""
# 백준
# No. 2033
# Python 3.11.9
# by "nno0obb"
"""

from decimal import ROUND_HALF_UP, Decimal


def main():
    # Input
    N = int(input())

    # Logic
    M = 0
    while True:
        M += 1
        temp = int(Decimal(str(N)).quantize(Decimal(f"1e+{M}"), rounding=ROUND_HALF_UP))
        if N < 10**M:
            break
        N = temp

    # Output
    print(N)


if __name__ == "__main__":
    main()
