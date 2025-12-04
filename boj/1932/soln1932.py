"""
# 백준
# No. 1932
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    n = int(input())
    P = [list(map(int, input().split())) for _ in range(n)]

    # Logic
    dp = [[0] * i for i in range(1, n + 1)]
    dp[0][0] = P[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + P[i][0]
        dp[i][i] = dp[i - 1][i - 1] + P[i][i]
        for j in range(1, i):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + P[i][j]

    ans = max(dp[n - 1])

    # Output
    print(ans)


if __name__ == "__main__":
    main()
