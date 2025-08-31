"""
# 리트코드
# No. 75 / sort-colors
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        r, w, b = 0, 0, len(nums)

        while w < b:
            if nums[w] == 0:  # Red
                nums[r], nums[w] = nums[w], nums[r]
                r += 1
                w += 1
            elif nums[w] == 1:  # White
                w += 1
            elif nums[w] == 2:  # Blue
                b -= 1
                nums[b], nums[w] = nums[w], nums[b]
            else:
                raise RuntimeError()

        print(nums)


def test_solution(subtests, capsys):
    with subtests.test("Example 1"):
        nums = [2, 0, 2, 1, 1, 0]
        output = [0, 0, 1, 1, 2, 2]
        Solution().sortColors(nums)
        captured = capsys.readouterr()
        assert captured.out.strip() == str(output)
    with subtests.test("Example 2"):
        nums = [2, 0, 1]
        output = [0, 1, 2]
        Solution().sortColors(nums)
        captured = capsys.readouterr()
        assert captured.out.strip() == str(output)
    with subtests.test("Example 3"):
        nums = [0]
        output = [0]
        Solution().sortColors(nums)
        captured = capsys.readouterr()
        assert captured.out.strip() == str(output)
