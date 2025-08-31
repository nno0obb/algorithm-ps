"""
# 리트코드
# No. 191 / number-of-1-bits
# Python 3.x.y
# by "nno0obb"
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()


def test_solution(subtests):
    with subtests.test("Example 1"):
        n = 11
        output = 3
        assert Solution().hammingWeight(n) == output
    with subtests.test("Example 2"):
        n = 128
        output = 1
        assert Solution().hammingWeight(n) == output
    with subtests.test("Example 3"):
        n = 2147483645
        output = 30
        assert Solution().hammingWeight(n) == output
