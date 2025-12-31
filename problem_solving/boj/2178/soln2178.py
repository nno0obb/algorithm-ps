"""
# 백준
# No. 2178
# Python 3.11.9
# by "nno0obb"
"""

from collections import deque


def main():
    # Input
    N, M = map(int, input().split())
    B = [list(map(int, list(input()))) for _ in range(N)]

    # Logic
    is_visited = [[False] * M for _ in range(N)]
    que = deque()

    que.append((0, 0, 1))
    is_visited[0][0] = True

    ans = -1
    while que:
        cy, cx, cl = que.popleft()

        if cy == N - 1 and cx == M - 1:
            ans = cl
            break

        for dy, dx in [(+1, 0), (0, -1), (-1, 0), (0, +1)]:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < M:
                if B[ny][nx] == 1 and not is_visited[ny][nx]:
                    que.append((ny, nx, cl + 1))
                    is_visited[ny][nx] = True

    # Output
    print(ans)


if __name__ == "__main__":
    main()
