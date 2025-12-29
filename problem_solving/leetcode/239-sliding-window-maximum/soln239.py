"""
# 리트코드
# No. 239 / sliding-window-maximum
# Python 3.x.y
# by "nno0obb"
"""

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        window = deque()

        for idx, num in enumerate(nums):
            while window and window[-1] < num:
                window.pop()
            window.append(num)

            if idx >= k and nums[idx - k] == window[0]:
                window.popleft()

            if idx >= k - 1:
                ret.append(window[0])

        return ret


def test_solution(subtests):
    with subtests.test("Example 1"):
        nums, k = [1, 3, -1, -3, 5, 3, 6, 7], 3
        output = [3, 3, 5, 5, 6, 7]
        assert Solution().maxSlidingWindow(nums, k) == output
    with subtests.test("Example 2"):
        nums, k = [1], 1
        output = [1]
        assert Solution().maxSlidingWindow(nums, k) == output
    with subtests.test("Example 3"):
        nums, k = [9, 10, 9, -7, -4, -8, 2, -6], 5
        output = [10, 10, 9, 2]
        assert Solution().maxSlidingWindow(nums, k) == output
