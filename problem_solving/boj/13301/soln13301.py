"""
# 백준
# No. 13301
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())

    # Logic
    dp = [0] * max(3, N + 1)
    dp[1], dp[2] = 1, 1
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    if N == 1:
        ans = 4
    elif N == 2:
        ans = 6
    else:
        ans = 4 * dp[N] + 2 * dp[N - 1]

    # Output
    print(ans)


if __name__ == "__main__":
    main()
