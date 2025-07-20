"""
# 백준
# No. 1455
# Python 3.11.9
# by "nno0obb"
"""

# Global Variables
max_N, max_M = 100, 100
B = [[0] * max_M for _ in range(max_N)]


def flip(n, m):
    for i in range(n + 1):
        for j in range(m + 1):
            B[i][j] = 1 - B[i][j]


def main():
    # Input
    N, M = map(int, input().split())
    for i in range(N):
        B[i] = list(map(int, list(input())))

    # Logic
    ans, idx = 0, N * M - 1
    while idx >= 0:
        n, m = divmod(idx, M)
        if B[n][m] == 1:
            ans += 1
            flip(n, m)
        idx -= 1

    # Output
    print(ans)


if __name__ == "__main__":
    main()
