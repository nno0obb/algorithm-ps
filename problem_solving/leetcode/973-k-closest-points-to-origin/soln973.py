"""
# 리트코드
# No. 973 / k-closest-points-to-origin
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:k]


def test_solution(subtests):
    with subtests.test("Example 1"):
        points, k = [[1, 3], [-2, 2]], 1
        output = [[-2, 2]]
        assert Solution().kClosest(points, k) == output
    with subtests.test("Example 2"):
        points, k = [[3, 3], [5, -1], [-2, 4]], 2
        output = [[3, 3], [-2, 4]]
        assert Solution().kClosest(points, k) == output
