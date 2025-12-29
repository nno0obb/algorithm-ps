"""
# 리트코드
# No. 455 / assign-cookies
# Python 3.x.y
# by "nno0obb"
"""

import heapq
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = [-x for x in g]
        s = [-x for x in s]
        heapq.heapify(g)
        heapq.heapify(s)

        cnt = 0
        while g and s:
            _g = heapq.heappop(g)
            _s = heapq.heappop(s)
            if -_g <= -_s:
                cnt += 1
            else:
                heapq.heappush(s, _s)
        return cnt


def test_solution(subtests):
    with subtests.test("Example 1"):
        g, s = [1, 2, 3], [1, 1]
        output = 1
        assert Solution().findContentChildren(g, s) == output
    with subtests.test("Example 2"):
        g, s = [1, 2], [1, 2, 3]
        output = 2
        assert Solution().findContentChildren(g, s) == output
    with subtests.test("Example 3"):
        g, s = [10, 9, 8, 7], [5, 6, 7, 8]
        output = 2
        assert Solution().findContentChildren(g, s) == output
