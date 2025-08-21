"""
# 리트코드
# No. 39 / combination-sum
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        curr, _next, ans = [([], 0)], [], []
        while curr:
            curr_comb, curr_sum = curr.pop()
            for candidate in candidates:
                if curr_comb and candidate < curr_comb[-1]:
                    continue

                if curr_sum + candidate > target:
                    break
                elif curr_sum + candidate == target:
                    ans.append(curr_comb + [candidate])
                elif curr_sum + candidate < target:
                    _next.append((curr_comb + [candidate], curr_sum + candidate))
            curr = _next
        return ans


def test_solution(subtests):
    with subtests.test("Example 1"):
        candidates, target = [2, 3, 6, 7], 7
        output = [[2, 2, 3], [7]]
        assert sorted(Solution().combinationSum(candidates, target)) == sorted(output)
    with subtests.test("Example 2"):
        candidates, target = [2, 3, 5], 8
        output = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        assert sorted(Solution().combinationSum(candidates, target)) == sorted(output)
    with subtests.test("Example 3"):
        candidates, target = [2], 1
        output = []
        assert sorted(Solution().combinationSum(candidates, target)) == sorted(output)
