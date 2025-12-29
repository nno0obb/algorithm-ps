"""
# 리트코드
# No. 134 / gas-station
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        idx, tank = 0, 0
        for i in range(len(gas)):
            if gas[i] + tank < cost[i]:
                idx = i + 1
                tank = 0
            else:
                tank += gas[i] - cost[i]
        return idx


def test_solution(subtests):
    with subtests.test("Example 1"):
        gas, cost = [1, 2, 3, 4, 5], [3, 4, 5, 1, 2]
        output = 3
        assert Solution().canCompleteCircuit(gas, cost) == output
    with subtests.test("Example 2"):
        gas, cost = [2, 3, 4], [3, 4, 3]
        output = -1
        assert Solution().canCompleteCircuit(gas, cost) == output
