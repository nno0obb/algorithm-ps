"""
# 백준
# No. 17203
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, Q = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    K = [list(map(int, input().split())) for _ in range(Q)]

    # Logic
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + abs(A[i] - A[i - 1])

    # Output
    for s, e in K:
        print(dp[e] - dp[s])


if __name__ == "__main__":
    main()
