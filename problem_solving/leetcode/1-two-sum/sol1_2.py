"""
# 리트코드
# No. 1 / Two Sum
# Python 3.x.y
# by "nno0obb"
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, num in enumerate(nums):
            if target - num in nums[i + 1 :]:
                return [i, nums.index(target - num, i + 1)]
        raise RuntimeError()


def test_solution(subtests):
    with subtests.test("Example 1"):
        nums, target = [2, 7, 11, 15], 9
        output = [0, 1]
        assert Solution().twoSum(nums, target) == output
    with subtests.test("Example 2"):
        nums, target = [3, 2, 4], 6
        output = [1, 2]
        assert Solution().twoSum(nums, target) == output
    with subtests.test("Example 3"):
        nums, target = [3, 3], 6
        output = [0, 1]
        assert Solution().twoSum(nums, target) == output
