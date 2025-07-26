"""
# 리트코드
# No. 561 / array-partition
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])


def test_solution(subtests):
    with subtests.test("Example 1"):
        nums = [1, 4, 3, 2]
        assert Solution().arrayPairSum(nums) == 4
    with subtests.test("Example 2"):
        nums = [6, 2, 6, 5, 1, 2]
        assert Solution().arrayPairSum(nums) == 9
