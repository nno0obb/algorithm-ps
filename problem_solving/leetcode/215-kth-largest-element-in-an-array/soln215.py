"""
# 리트코드
# No. 215 / kth-largest-element-in-an-array
# Python 3.x.y
# by "nno0obb"
"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


def test_solution(subtests):
    with subtests.test("Example 1"):
        nums, k = [3, 2, 1, 5, 6, 4], 2
        output = 5
        assert Solution().findKthLargest(nums, k) == output
    with subtests.test("Example 2"):
        nums, k = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4
        output = 4
        assert Solution().findKthLargest(nums, k) == output
