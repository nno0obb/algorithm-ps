"""
# 리트코드
# No. 1 / Two Sum
# Python 3.x.y
# by "nno0obb"
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pairs = list(zip(nums, range(len(nums))))  # (num, index)
        pairs.sort(key=lambda x: x[0])

        sdx, edx = 0, len(pairs) - 1  # start, end
        while sdx < edx:
            if pairs[sdx][0] + pairs[edx][0] < target:
                sdx += 1
            elif pairs[sdx][0] + pairs[edx][0] > target:
                edx -= 1
            else:
                return [pairs[sdx][1], pairs[edx][1]]
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
