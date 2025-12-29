"""
# 백준
# No. 22342
# Python 3.11.9 (PyPy3)
# by "nno0obb"
"""


def main():
    # Input
    M, N = map(int, input().split())
    D = [list(map(int, list(input()))) for _ in range(M)]

    # Logic
    dp = [[0] * N for _ in range(M)]
    for i in range(M):
        dp[i][0] = D[i][0]

    ans = 0
    for j in range(1, N):
        for i in range(M):
            dp[i][j] = dp[i][j - 1]

            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])
            if i < M - 1:
                dp[i][j] = max(dp[i][j], dp[i + 1][j - 1])
            ans = max(ans, dp[i][j])
            dp[i][j] += D[i][j]

    # Output
    print(ans)


if __name__ == "__main__":
    main()
