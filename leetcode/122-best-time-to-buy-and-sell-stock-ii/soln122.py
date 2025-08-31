"""
# 리트코드
# No. 122 / best-time-to-buy-and-sell-stock-ii
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, prices[i + 1] - prices[i]) for i in range(0, len(prices) - 1))


def test_solution(subtests):
    with subtests.test("Example 1"):
        prices = [7, 1, 5, 3, 6, 4]
        output = 7
        assert Solution().maxProfit(prices) == output
    with subtests.test("Example 2"):
        prices = [1, 2, 3, 4, 5]
        output = 4
        assert Solution().maxProfit(prices) == output
    with subtests.test("Example 3"):
        prices = [7, 6, 4, 3, 1]
        output = 0
        assert Solution().maxProfit(prices) == output
