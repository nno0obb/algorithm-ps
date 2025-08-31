"""
# 리트코드
# No. 240 / search-a-2d-matrix-ii
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        y, x = 0, n - 1
        while 0 <= y < m and 0 <= x < n:
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] < target:
                y += 1
            elif matrix[y][x] > target:
                x -= 1
            else:
                raise RuntimeError()

        return False


def test_solution(subtests):
    with subtests.test("Example 1"):
        matrix, target = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ], 2
        output = True
        assert Solution().searchMatrix(matrix, target) == output
    with subtests.test("Example 2"):
        matrix, target = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ], 20
        output = False
        assert Solution().searchMatrix(matrix, target) == output
    with subtests.test("Example 3"):
        matrix, target = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ], 19
        output = True
        assert Solution().searchMatrix(matrix, target) == output
    with subtests.test("Example 4"):
        matrix, target = [
            [1, 3, 5, 7, 9],
            [2, 4, 6, 8, 10],
            [11, 13, 15, 17, 19],
            [12, 14, 16, 18, 20],
            [21, 22, 23, 24, 25],
        ], 13
        output = True
        assert Solution().searchMatrix(matrix, target) == output
