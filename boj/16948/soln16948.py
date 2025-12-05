"""
# 백준
# No. 16948
# Python 3.11.9
# by "nno0obb"
"""

from collections import deque


def main():
    # Input
    N = int(input())
    r1, c1, r2, c2 = map(int, input().split())

    # Logic
    dp = [[-1] * N for _ in range(N)]
    dp[r1][c1] = 0

    drs = [-2, -2, 0, 0, +2, +2]
    dcs = [-1, +1, -2, +2, -1, +1]

    ans = -1
    que = deque([(r1, c1)])
    while que:
        cr, cc = que.popleft()
        if cr == r2 and cc == c2:
            ans = dp[cr][cc]
            break

        for dr, dc in zip(drs, dcs):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N:
                if dp[nr][nc] == -1:
                    dp[nr][nc] = dp[cr][cc] + 1
                    que.append((nr, nc))

    # Output
    print(ans)


if __name__ == "__main__":
    main()
