"""
# 백준
# No. 15624
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    n = int(input())

    # Logic
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= 1_000_000_007

    # Output
    print(dp[n])


if __name__ == "__main__":
    main()
