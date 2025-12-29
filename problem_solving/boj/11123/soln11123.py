"""
# 백준
# No. 11123 
# Python 3.11.9
# by "nno0obb"
"""

import sys

sys.setrecursionlimit(1_000_000)


# Global Variables
H, W, grid, is_visited = -1, -1, [], []


def dfs(x, y):
    global H, W, grid, is_visited

    if 0 <= x < H and 0 <= y < W:
        if grid[x][y] == "#" and not is_visited[x][y]:
            is_visited[x][y] = True
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)


def main():
    global H, W, grid, is_visited

    # Input
    T = int(input())
    for _ in range(T):
        H, W = map(int, input().split())
        grid = [list(input()) for _ in range(H)]

        # Logic
        flock_count = 0
        is_visited = [[False] * W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if grid[i][j] == "#" and not is_visited[i][j]:
                    dfs(i, j)
                    flock_count += 1

        # Output
        print(flock_count)


if __name__ == "__main__":
    main()
