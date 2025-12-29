"""
# 리트코드
# No. 347 / top-k-frequent-elements
# Python 3.x.y
# by "nno0obb"
"""

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, _ in Counter(nums).most_common(k)]


def test_solution(subtests):
    with subtests.test("Example 1"):
        nums, k = [1, 1, 1, 2, 2, 3], 2
        output = [1, 2]
        assert Solution().topKFrequent(nums, k) == output
    with subtests.test("Example 2"):
        nums, k = [1], 1
        output = [1]
        assert Solution().topKFrequent(nums, k) == output
