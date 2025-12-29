"""
# 백준
# No. 15990
# Python 3.11.9
# by "nno0obb"
"""

import sys

# Global Variables
max_n = 100_000
MOD = 1_000_000_009


def main():
    # Logic
    dp = [[0] * 4 for _ in range(max_n + 1)]
    dp[1] = [0, 1, 0, 0]  # 1 = 1
    dp[2] = [0, 0, 1, 0]  # 2 = 2
    dp[3] = [0, 1, 1, 1]  # 3 = 1 + 2 = 2 + 1 = 3
    for i in range(4, max_n + 1):
        dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % MOD
        dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % MOD
        dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % MOD

    # Input
    T = int(input())
    for _ in range(T):
        n = int(sys.stdin.readline())

        # Logic
        ans = (dp[n][1] + dp[n][2] + dp[n][3]) % MOD

        # Output
        print(ans)


if __name__ == "__main__":
    main()
