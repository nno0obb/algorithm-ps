"""
# 백준
# No. 9764
# Python 3.11.9
# by "nno0obb"
"""

# Global Variables
MAX_N = 2_000
MOD = 100_999


def main():
    # Logic
    dp = [[0] * (MAX_N + 1) for _ in range(MAX_N + 1)]
    for i in range(MAX_N + 1):
        dp[0][i] = 1

    for i in range(1, MAX_N + 1):
        for j in range(1, MAX_N + 1):
            dp[i][j] = dp[i][j - 1]
            if i >= j:
                dp[i][j] += dp[i - j][j - 1]
                dp[i][j] %= MOD

    # Input
    T = int(input())
    for _ in range(T):
        N = int(input())

        # Output
        print(dp[N][N])

    # Hint
    # dp[i][j] = (1~j) --> i
    # dp[i][j] = dp[i][j-1] + dp[i-j][j-1]


if __name__ == "__main__":
    main()
