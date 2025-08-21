"""
# 리트코드
# No. 46 / permutations
# Python 3.x.y
# by "nno0obb"
"""

from itertools import permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, permutations(nums)))


def test_solution(subtests):
    with subtests.test("Example 1"):
        nums = [1, 2, 3]
        output = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        assert sorted(Solution().permute(nums)) == sorted(output)
    with subtests.test("Example 2"):
        nums = [0, 1]
        output = [[0, 1], [1, 0]]
        assert sorted(Solution().permute(nums)) == sorted(output)
    with subtests.test("Example 3"):
        nums = [1]
        output = [[1]]
        assert sorted(Solution().permute(nums)) == sorted(output)
