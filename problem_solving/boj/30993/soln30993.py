"""
# 백준
# No. 30993
# Python 3.11.9
# by "nno0obb"
"""

from math import factorial


def main():
    # Input
    N, A, B, C = map(int, input().split())

    # Logic
    ans = factorial(N) // factorial(A) // factorial(N - A)
    ans *= factorial(N - A) // factorial(B) // factorial(N - A - B)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
