"""
# 리트코드
# No. 207 / course-schedule
# Python 3.x.y
# by "nno0obb"
"""

from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph_in, graph_out = defaultdict(set), defaultdict(set)
        for course, pre in prerequisites:
            graph_in[course].add(pre)
            graph_out[pre].add(course)

        que, is_visited = [], [False] * numCourses
        for course in range(numCourses):
            if len(graph_in[course]) == 0:
                que.append(course)

        while que:
            curr = que.pop(0)
            is_visited[curr] = True
            for _next in graph_out[curr]:
                graph_in[_next].discard(curr)
                if len(graph_in[_next]) == 0:
                    que.append(_next)

        return all(is_visited)


def test_solution(subtests):
    with subtests.test("Example 1"):
        numCourses, prerequisites = 2, [[1, 0]]
        output = True
        assert Solution().canFinish(numCourses, prerequisites) == output
    with subtests.test("Example 2"):
        numCourses, prerequisites = 2, [[1, 0], [0, 1]]
        output = False
        assert Solution().canFinish(numCourses, prerequisites) == output
