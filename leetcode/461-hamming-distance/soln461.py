"""
# 리트코드
# No. 461 / hamming-distance
# Python 3.x.y
# by "nno0obb"
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")


def test_solution(subtests):
    with subtests.test("Example 1"):
        x, y = 1, 4
        output = 2
        assert Solution().hammingDistance(x, y) == output
    with subtests.test("Example 2"):
        x, y = 3, 1
        output = 1
        assert Solution().hammingDistance(x, y) == output
