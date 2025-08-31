"""
# 리트코드
# No. 167 / two-sum-ii-input-array-is-sorted
# Python 3.x.y
# by "nno0obb"
"""

import bisect
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(1, len(numbers)):
            idx = bisect.bisect_left(numbers, target - numbers[i], lo=0, hi=i)
            if idx < i and numbers[idx] == target - numbers[i]:
                return [idx + 1, i + 1]
        raise RuntimeError()


def test_solution(subtests):
    with subtests.test("Example 1"):
        numbers, target = [2, 7, 11, 15], 9
        output = [1, 2]
        assert Solution().twoSum(numbers, target) == output
    with subtests.test("Example 2"):
        numbers, target = [2, 3, 4], 6
        output = [1, 3]
        assert Solution().twoSum(numbers, target) == output
    with subtests.test("Example 3"):
        numbers, target = [-1, 0], -1
        output = [1, 2]
        assert Solution().twoSum(numbers, target) == output
