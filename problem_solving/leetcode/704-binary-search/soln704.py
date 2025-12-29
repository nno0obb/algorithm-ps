"""
# 리트코드
# No. 704 / binary-search
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left: int, right: int) -> int:
            if left > right:
                return -1
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, right)
            elif nums[mid] > target:
                return binary_search(left, mid - 1)
            else:
                raise RuntimeError()

        return binary_search(0, len(nums) - 1)


def test_solution(subtests):
    with subtests.test("Example 1"):
        nums, target = [-1, 0, 3, 5, 9, 12], 9
        output = 4
        assert Solution().search(nums, target) == output
    with subtests.test("Example 2"):
        nums, target = [-1, 0, 3, 5, 9, 12], 2
        output = -1
        assert Solution().search(nums, target) == output
