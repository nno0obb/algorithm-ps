"""
# 백준
# No. 1890
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    B = [list(map(int, input().split())) for _ in range(N)]

    # Logic
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N):
            if B[i][j] == 0:
                continue
            b = B[i][j]
            if i + b < N:
                dp[i + b][j] += dp[i][j]
            if j + b < N:
                dp[i][j + b] += dp[i][j]

    # Output
    print(dp[N - 1][N - 1])


if __name__ == "__main__":
    main()
