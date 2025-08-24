"""
# 리트코드
# No. 743 / network-delay-time
# Python 3.x.y
# by "nno0obb"
"""

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        que, dist = [(0, k)], defaultdict(int)
        while que:
            time, node = heapq.heappop(que)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    heapq.heappush(que, (time + w, v))

        if len(dist) == n:
            return max(dist.values())
        else:
            return -1


def test_solution(subtests):
    with subtests.test("Example 1"):
        times, n, k = [[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2
        output = 2
        assert Solution().networkDelayTime(times, n, k) == output
    with subtests.test("Example 2"):
        times, n, k = [[1, 2, 1]], 2, 1
        output = 1
        assert Solution().networkDelayTime(times, n, k) == output
    with subtests.test("Example 3"):
        times, n, k = [[1, 2, 1]], 2, 2
        output = -1
        assert Solution().networkDelayTime(times, n, k) == output
