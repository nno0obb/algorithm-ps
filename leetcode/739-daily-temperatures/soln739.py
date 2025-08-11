"""
# 리트코드
# No. 739 / daily-temperatures
# Python 3.x.y
# by "nno0obb"
"""

from typing import List, Tuple


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: List[Tuple[int, int]] = []
        ans = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                _, day = stack.pop()
                ans[day] = i - day
            stack.append((temperature, i))

        return ans


def test_solution(subtests):
    with subtests.test("Example 1"):
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        output = [1, 1, 4, 2, 1, 1, 0, 0]
        assert Solution().dailyTemperatures(temperatures) == output
    with subtests.test("Example 2"):
        temperatures = [30, 40, 50, 60]
        output = [1, 1, 1, 0]
        assert Solution().dailyTemperatures(temperatures) == output
    with subtests.test("Example 3"):
        temperatures = [30, 60, 90]
        output = [1, 1, 0]
        assert Solution().dailyTemperatures(temperatures) == output
