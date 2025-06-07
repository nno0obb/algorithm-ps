"""
# 리트코드
# No. 1 / Two Sum
# Python 3.x.y
# by "nno0obb"
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        raise RuntimeError()


def test_solution(subtests):
    with subtests.test("Example 1"):
        assert Solution().twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
    with subtests.test("Example 2"):
        assert Solution().twoSum(nums=[3, 2, 4], target=6) == [1, 2]
    with subtests.test("Example 3"):
        assert Solution().twoSum(nums=[3, 3], target=6) == [0, 1]
