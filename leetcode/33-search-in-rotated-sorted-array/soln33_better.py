"""
# 리트코드
# No. 33 / search-in-rotated-sorted-array
# Python 3.x.y
# by "nno0obb"
"""

import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ldx, rdx = 0, len(nums) - 1
        while ldx < rdx:
            mdx = (ldx + rdx) // 2
            if nums[mdx] < nums[rdx]:
                rdx = mdx
            else:
                ldx = mdx + 1
        k = ldx

        idx = bisect.bisect_left(nums[:k], target)
        if idx < len(nums[:k]) and nums[idx] == target:
            return idx
        idx = bisect.bisect_left(nums[k:], target) + k
        if idx < len(nums) and nums[idx] == target:
            return idx
        return -1


def test_solution(subtests):
    with subtests.test("Example 1"):
        nums, target = [4, 5, 6, 7, 0, 1, 2], 0
        output = 4
        assert Solution().search(nums, target) == output
    with subtests.test("Example 2"):
        nums, target = [4, 5, 6, 7, 0, 1, 2], 3
        output = -1
        assert Solution().search(nums, target) == output
    with subtests.test("Example 3"):
        nums, target = [1], 0
        output = -1
        assert Solution().search(nums, target) == output
