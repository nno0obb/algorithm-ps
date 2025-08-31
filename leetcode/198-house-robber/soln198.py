"""
# 리트코드
# No. 198 / house-robber
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[len(nums) - 1]


def test_solution(subtests):
    with subtests.test("Example 1"):
        nums = [1, 2, 3, 1]
        output = 4
        assert Solution().rob(nums) == output
    with subtests.test("Example 2"):
        nums = [2, 7, 9, 3, 1]
        output = 12
        assert Solution().rob(nums) == output
