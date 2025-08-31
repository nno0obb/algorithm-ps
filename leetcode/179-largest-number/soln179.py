"""
# 리트코드
# No. 179 / largest-number
# Python 3.x.y
# by "nno0obb"
"""

from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x: str, y: str) -> bool:
            return int(x + y) - int(y + x)

        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(compare), reverse=True)
        return str(int("".join(nums)))


def test_solution(subtests):
    with subtests.test("Example 1"):
        nums = [10, 2]
        output = "210"
        assert Solution().largestNumber(nums) == output
    with subtests.test("Example 2"):
        nums = [3, 30, 34, 5, 9]
        output = "9534330"
        assert Solution().largestNumber(nums) == output
    with subtests.test("Example 3"):
        nums = [0, 0]
        output = "0"
        assert Solution().largestNumber(nums) == output
