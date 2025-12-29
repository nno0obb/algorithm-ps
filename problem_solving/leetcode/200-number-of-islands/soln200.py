"""
# 리트코드
# No. 200 / number-of-islands
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        is_visited = [[False] * n for _ in range(m)]

        island_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not is_visited[i][j]:
                    island_count += 1

                    que = []
                    que.append((i, j))
                    while que:
                        y, x = que.pop()
                        is_visited[y][x] = True
                        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            ny, nx = y + dy, x + dx
                            if 0 <= ny < m and 0 <= nx < n:
                                if grid[ny][nx] == "1" and not is_visited[ny][nx]:
                                    que.append((ny, nx))
        return island_count


def test_solution(subtests):
    with subtests.test("Example 1"):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        output = 1
        assert Solution().numIslands(grid) == output
    with subtests.test("Example 2"):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        output = 3
        assert Solution().numIslands(grid) == output
