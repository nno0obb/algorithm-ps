"""
# 리트코드
# No. 121 / best-time-to-buy-and-sell-stock
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack, max_profit = [], 0
        for price in prices:
            if not stack:
                stack.append(price)
            elif stack[-1] > price:
                stack.append(price)
            else:
                max_profit = max(max_profit, price - stack[-1])
        return max_profit


def test_solution(subtests):
    with subtests.test("Example 1"):
        prices = [7, 1, 5, 3, 6, 4]
        output = 5
        assert Solution().maxProfit(prices) == output

    with subtests.test("Example 2"):
        prices = [7, 6, 4, 3, 1]
        output = 0
        assert Solution().maxProfit(prices) == output
