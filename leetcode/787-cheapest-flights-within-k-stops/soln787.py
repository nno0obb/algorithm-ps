"""
# 리트코드
# No. 787 / cheapest-flights-within-k-stops
# Python 3.x.y
# by "nno0obb"
"""

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for _from, to, curr_price in flights:
            graph[_from].append((to, curr_price))

        que, dist = [(0, src, 0)], defaultdict(int)
        while que:
            curr_price, curr_node, stops = heapq.heappop(que)
            if dst == curr_node:
                return curr_price
            if (curr_node, stops) not in dist:
                dist[(curr_node, stops)] = curr_price
                if stops <= k:
                    for next_node, next_price in graph[curr_node]:
                        heapq.heappush(que, (curr_price + next_price, next_node, stops + 1))

        return -1


def test_solution(subtests):
    with subtests.test("Example 1"):
        n, flights, src, dst, k = 4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1
        output = 700
        assert Solution().findCheapestPrice(n, flights, src, dst, k) == output
    with subtests.test("Example 2"):
        n, flights, src, dst, k = 3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1
        output = 200
        assert Solution().findCheapestPrice(n, flights, src, dst, k) == output
    with subtests.test("Example 3"):
        n, flights, src, dst, k = 3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0
        output = 500
        assert Solution().findCheapestPrice(n, flights, src, dst, k) == output
    with subtests.test("Example 4"):
        n, flights, src, dst, k = 4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1
        output = 6
        assert Solution().findCheapestPrice(n, flights, src, dst, k) == output
