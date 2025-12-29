"""
# 리트코드
# No. 56 / merge-intervals
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            if merged[-1][1] >= intervals[i][0]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])
        return list(merged)


def test_solution(subtests):
    with subtests.test("Example 1"):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        output = [[1, 6], [8, 10], [15, 18]]
        assert Solution().merge(intervals) == output
    with subtests.test("Example 2"):
        intervals = [[1, 4], [4, 5]]
        output = [[1, 5]]
        assert Solution().merge(intervals) == output
    with subtests.test("Example 3"):
        intervals = [[1, 4], [2, 3]]
        output = [[1, 4]]
        assert Solution().merge(intervals) == output
