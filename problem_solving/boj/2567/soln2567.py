"""
# 백준
# No. 2567
# Python 3.11.9
# by "nno0obb"
"""

# Global Variables
MAX_N = 100
UP, LEFT, DOWN, RIGHT, FILLED = 0, 1, 2, 3, 4


def main():
    # Input
    N = int(input())
    C = [list(map(int, input().split())) for _ in range(N)]

    # Logic
    B = [[[False] * 5 for _ in range(MAX_N + 1)] for _ in range(MAX_N + 1)]

    for x, y in C:
        for i in range(10):
            for j in range(10):
                for k in range(5):
                    B[x + i][y + j][k] = True

    ans = 0
    for i in range(MAX_N + 1):
        for j in range(MAX_N + 1):
            if not B[i][j][FILLED]:
                for k in range(4):
                    dx, dy = [(0, +1), (-1, 0), (0, -1), (+1, 0)][k]
                    ax, ay = i + dx, j + dy
                    if 0 <= ax <= MAX_N and 0 <= ay <= MAX_N:
                        if B[ax][ay][FILLED]:
                            ans += 1

    # Output
    print(ans)


if __name__ == "__main__":
    main()
