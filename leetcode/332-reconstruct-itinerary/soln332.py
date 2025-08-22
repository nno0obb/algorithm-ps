"""
# 리트코드
# No. 332 / reconstruct-itinerary
# Python 3.x.y
# by "nno0obb"
"""

from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        ans = []

        def dfs(curr: str):
            while graph[curr]:
                dfs(graph[curr].pop())
            ans.append(curr)

        dfs("JFK")
        return ans[::-1]


def test_solution(subtests):
    with subtests.test("Example 1"):
        tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        output = ["JFK", "MUC", "LHR", "SFO", "SJC"]
        assert Solution().findItinerary(tickets) == output
    with subtests.test("Example 2"):
        tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
        output = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
        assert Solution().findItinerary(tickets) == output
    with subtests.test("Example 3"):
        tickets = [
            ["JFK", "SFO"],
            ["JFK", "ATL"],
            ["SFO", "JFK"],
            ["ATL", "AAA"],
            ["AAA", "ATL"],
            ["ATL", "BBB"],
            ["BBB", "ATL"],
            ["ATL", "CCC"],
            ["CCC", "ATL"],
            ["ATL", "DDD"],
            ["DDD", "ATL"],
            ["ATL", "EEE"],
            ["EEE", "ATL"],
            ["ATL", "FFF"],
            ["FFF", "ATL"],
            ["ATL", "GGG"],
            ["GGG", "ATL"],
            ["ATL", "HHH"],
            ["HHH", "ATL"],
            ["ATL", "III"],
            ["III", "ATL"],
            ["ATL", "JJJ"],
            ["JJJ", "ATL"],
            ["ATL", "KKK"],
            ["KKK", "ATL"],
            ["ATL", "LLL"],
            ["LLL", "ATL"],
            ["ATL", "MMM"],
            ["MMM", "ATL"],
            ["ATL", "NNN"],
            ["NNN", "ATL"],
        ]
        output = [
            "JFK",
            "SFO",
            "JFK",
            "ATL",
            "AAA",
            "ATL",
            "BBB",
            "ATL",
            "CCC",
            "ATL",
            "DDD",
            "ATL",
            "EEE",
            "ATL",
            "FFF",
            "ATL",
            "GGG",
            "ATL",
            "HHH",
            "ATL",
            "III",
            "ATL",
            "JJJ",
            "ATL",
            "KKK",
            "ATL",
            "LLL",
            "ATL",
            "MMM",
            "ATL",
            "NNN",
            "ATL",
        ]
        assert Solution().findItinerary(tickets) == output
