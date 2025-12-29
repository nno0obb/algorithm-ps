"""
# 리트코드
# No. 53 / maximum-subarray
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


def test_solution(subtests):
    with subtests.test("Example 1"):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        output = 6
        assert Solution().maxSubArray(nums) == output
    with subtests.test("Example 2"):
        nums = [1]
        output = 1
        assert Solution().maxSubArray(nums) == output
    with subtests.test("Example 3"):
        nums = [5, 4, -1, 7, 8]
        output = 23
        assert Solution().maxSubArray(nums) == output
