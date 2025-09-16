"""
# 백준
# No. 1697
# Python 3.11.9
# by "nno0obb"
"""

from collections import deque


def main():
    # Input
    N, K = map(int, input().split())

    # Logic
    dp = [-1] * (max(N, K) * 2 + 1)
    dp[N] = 0

    ans, que = -1, deque([N])
    while que:
        c = que.popleft()
        if c == K:
            ans = dp[c]
            break
        for n in [c - 1, c + 1, c * 2]:
            if 0 <= n < len(dp) and dp[n] == -1:
                dp[n] = dp[c] + 1
                que.append(n)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
