"""
# 리트코드
# No. 136 / single-number
# Python 3.x.y
# by "nno0obb"
"""

from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


def test_solution(subtests):
    with subtests.test("Example 1"):
        nums = [2, 2, 1]
        output = 1
        assert Solution().singleNumber(nums) == output
    with subtests.test("Example 2"):
        nums = [4, 1, 2, 1, 2]
        output = 4
        assert Solution().singleNumber(nums) == output
    with subtests.test("Example 3"):
        nums = [1]
        output = 1
        assert Solution().singleNumber(nums) == output
