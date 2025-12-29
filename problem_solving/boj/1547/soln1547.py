"""
# 백준
# No. 1547
# Python 3.11.9
# by "nno0obb"
"""

# Global Variables
DUMMY, BALL, EMPTY = -1, 1, 0


def main():
    # Input
    M = int(input())
    Z = [list(map(int, input().split())) for _ in range(M)]

    # Logic
    P = [DUMMY, BALL, EMPTY, EMPTY]
    for X, Y in Z:
        P[X], P[Y] = P[Y], P[X]
    ans = P.index(BALL)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
