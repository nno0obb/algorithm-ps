"""
# 리트코드
# No. 77 / combinations
# Python 3.x.y
# by "nno0obb"
"""

from itertools import combinations
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(map(list, combinations(range(1, n + 1), k)))


def test_solution(subtests):
    with subtests.test("Example 1"):
        n, k = 4, 2
        output = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        assert sorted(Solution().combine(n, k)) == sorted(output)
    with subtests.test("Example 2"):
        n, k = 1, 1
        output = [[1]]
        assert sorted(Solution().combine(n, k)) == sorted(output)
