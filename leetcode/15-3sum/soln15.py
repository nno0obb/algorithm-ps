"""
# 리트코드
# No. 15 / 3sum
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            ldx, rdx = i + 1, len(nums) - 1
            while ldx < rdx:
                _sum = nums[i] + nums[ldx] + nums[rdx]
                if _sum < 0:
                    ldx += 1
                elif _sum > 0:
                    rdx -= 1
                else:
                    result.append([nums[i], nums[ldx], nums[rdx]])
                    while ldx < rdx and nums[ldx] == nums[ldx + 1]:
                        ldx += 1
                    while ldx < rdx and nums[rdx] == nums[rdx - 1]:
                        rdx -= 1
                    ldx += 1
                    rdx -= 1

        return result


def test_solution(subtests):
    with subtests.test("Example 1"):
        nums = [-1, 0, 1, 2, -1, -4]
        assert Solution().threeSum(nums) == [[-1, -1, 2], [-1, 0, 1]]
    with subtests.test("Example 2"):
        nums = [0, 1, 1]
        assert Solution().threeSum(nums) == []
    with subtests.test("Example 3"):
        nums = [0, 0, 0]
        assert Solution().threeSum(nums) == [[0, 0, 0]]
