"""
# 리트코드
# No. 310 / minimum-height-trees
# Python 3.x.y
# by "nno0obb"
"""

from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        last_leaves = []
        remain_nodes = set(range(n))

        while remain_nodes:
            leaves = []
            for i in remain_nodes:
                if len(graph[i]) <= 1:
                    leaves.append(i)
            last_leaves = leaves

            for leaf in leaves:
                remain_nodes.remove(leaf)
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)
                del graph[leaf]

        return last_leaves


def test_solution(subtests):
    with subtests.test("Example 1"):
        n, edges = 4, [[1, 0], [1, 2], [1, 3]]
        output = [1]
        assert sorted(Solution().findMinHeightTrees(n, edges)) == sorted(output)
    with subtests.test("Example 2"):
        n, edges = 6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
        output = [3, 4]
        assert sorted(Solution().findMinHeightTrees(n, edges)) == sorted(output)
    with subtests.test("Example 3"):
        n, edges = 1, []
        output = [0]
        assert sorted(Solution().findMinHeightTrees(n, edges)) == sorted(output)
    with subtests.test("Example 4"):
        n, edges = 2, [[0, 1]]
        output = [0, 1]
        assert sorted(Solution().findMinHeightTrees(n, edges)) == sorted(output)
    with subtests.test("Example 5"):
        n, edges = 10, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 3], [4, 6], [4, 7], [5, 8], [5, 9]]
        output = [3]
        assert sorted(Solution().findMinHeightTrees(n, edges)) == sorted(output)


# 그냥 다 brute force 로 해야하나...
