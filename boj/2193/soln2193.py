"""
# 백준
# No. 2193
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())

    # Logic
    dp = [[-1, -1] for _ in range(max(3, N + 1))]
    dp[1] = [0, 1]
    dp[2] = [1, 0]
    for i in range(3, N + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
        dp[i][1] = dp[i - 1][0]
    ans = dp[N][0] + dp[N][1]

    # Output
    print(ans)


if __name__ == "__main__":
    main()
