"""
# 리트코드
# No. 78 / subsets
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(idx: int, curr: List[int]) -> None:
            if idx >= len(nums):
                ans.append(curr)
                return
            dfs(idx + 1, curr)
            dfs(idx + 1, curr + [nums[idx]])

        dfs(0, [])
        return ans


def test_solution(subtests):
    with subtests.test("Example 1"):
        nums = [1, 2, 3]
        output = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        assert sorted(Solution().subsets(nums)) == sorted(output)
    with subtests.test("Example 2"):
        nums = [0]
        output = [[], [0]]
        assert sorted(Solution().subsets(nums)) == sorted(output)
