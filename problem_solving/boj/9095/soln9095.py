"""
# 백준
# No. 9095
# Python 3.11.9
# by "nno0obb"
"""

MAX_N = 11


def main():
    # Logic
    dp = [0] * (MAX_N + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, MAX_N + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    # Input
    T = int(input())
    for _ in range(T):
        n = int(input())

        # Output
        print(dp[n])


if __name__ == "__main__":
    main()
