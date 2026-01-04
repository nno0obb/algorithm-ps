"""
# 백준
# No. 1743
# Python 3.11.9
# by "nno0obb"
"""

import sys
from collections import deque


def main():
    # Input
    N, M, K = map(int, input().split())
    B = [["."] * (M + 1) for _ in range(N + 1)]
    for _ in range(K):
        r, c = map(int, sys.stdin.readline().strip().split())
        B[r][c] = "#"

    # Logic
    is_visited = [[False] * (M + 1) for _ in range(N + 1)]
    ans = -1
    for i in range(1, N + 1):
        for j in range(1, M + 1):

            cnt = 0
            if B[i][j] == "#" and not is_visited[i][j]:
                que = deque()
                que.append((i, j))
                is_visited[i][j] = True
                cnt += 1

                while que:
                    cy, cx = que.popleft()
                    for dy, dx in [(-1, 0), (0, -1), (+1, 0), (0, +1)]:
                        ny, nx = cy + dy, cx + dx
                        if 1 <= ny <= N and 1 <= nx <= M:
                            if B[ny][nx] == "#" and not is_visited[ny][nx]:
                                que.append((ny, nx))
                                is_visited[ny][nx] = True
                                cnt += 1

                ans = max(ans, cnt)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
