"""
# 리트코드
# No. 349 / intersection-of-two-arrays
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


def test_solution(subtests):
    with subtests.test("Example 1"):
        nums1, nums2 = [1, 2, 2, 1], [2, 2]
        output = [2]
        assert sorted(Solution().intersection(nums1, nums2)) == sorted(output)
    with subtests.test("Example 2"):
        nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
        output = [9, 4]
        assert sorted(Solution().intersection(nums1, nums2)) == sorted(output)
    with subtests.test("Example 3"):
        nums1, nums2 = [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]
        output = []
        assert sorted(Solution().intersection(nums1, nums2)) == sorted(output)
