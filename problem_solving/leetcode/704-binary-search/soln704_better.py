"""
# 리트코드
# No. 704 / binary-search
# Python 3.x.y
# by "nno0obb"
"""

import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        if idx < len(nums) and nums[idx] == target:
            return idx
        return -1


def test_solution(subtests):
    with subtests.test("Example 1"):
        nums, target = [-1, 0, 3, 5, 9, 12], 9
        output = 4
        assert Solution().search(nums, target) == output
    with subtests.test("Example 2"):
        nums, target = [-1, 0, 3, 5, 9, 12], 2
        output = -1
        assert Solution().search(nums, target) == output
