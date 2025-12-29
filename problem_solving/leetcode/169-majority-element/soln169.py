"""
# 리트코드
# No. 169 / majority-element
# Python 3.x.y
# by "nno0obb"
"""

from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]


def test_solution(subtests):
    with subtests.test("Example 1"):
        nums = [3, 2, 3]
        output = 3
        assert Solution().majorityElement(nums) == output
    with subtests.test("Example 2"):
        nums = [2, 2, 1, 1, 1, 2, 2]
        output = 2
        assert Solution().majorityElement(nums) == output
