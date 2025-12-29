"""
# 리트코드
# No. 238 / product-of-array-except-self
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l2r = [1] * len(nums)
        l2r[0] = nums[0]
        for i in range(1, len(nums) - 1):
            l2r[i] = l2r[i - 1] * nums[i]

        r2l = [1] * len(nums)
        r2l[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, 0, -1):
            r2l[i] = r2l[i + 1] * nums[i]

        res = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[i] = r2l[i + 1]
            elif i == len(nums) - 1:
                res[i] = l2r[i - 1]
            else:
                res[i] = l2r[i - 1] * r2l[i + 1]

        return res


def test_solution(subtests):
    with subtests.test("Example 1"):
        nums = [1, 2, 3, 4]
        output = [24, 12, 8, 6]
        assert Solution().productExceptSelf(nums) == output
    with subtests.test("Example 2"):
        nums = [-1, 1, 0, -3, 3]
        output = [0, 0, 9, 0, 0]
        assert Solution().productExceptSelf(nums) == output
