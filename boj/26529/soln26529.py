"""
# 백준
# No. 26529
# Python 3.11.9
# by "nno0obb"
"""

# Global Variables
MAX_X = 45


def main():
    # Logic
    dp = [0] * (MAX_X + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, MAX_X + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    # Input
    T = int(input())
    for _ in range(T):
        N = int(input())

        # Output
        print(dp[N])


if __name__ == "__main__":
    main()
