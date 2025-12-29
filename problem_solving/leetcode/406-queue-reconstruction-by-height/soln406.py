"""
# 리트코드
# No. 406 / queue-reconstruction-by-height
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        ret = []
        for h, k in people:
            ret.insert(k, [h, k])
        return ret


def test_solution(subtests):
    with subtests.test("Example 1"):
        people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
        output = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
        assert Solution().reconstructQueue(people) == output
