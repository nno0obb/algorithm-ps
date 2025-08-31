"""
# 리트코드
# No. 371 / sum-of-two-integers
# Python 3.x.y
# by "nno0obb"
"""

import sys


class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = int("0b" + "1" * sys.getsizeof(int()), 2)

        bin_a = bin(a & mask).lstrip("0b")[::-1]
        bin_b = bin(b & mask).lstrip("0b")[::-1]
        max_len = max(len(bin_a), len(bin_b))
        bin_a = bin_a.ljust(max_len, "0")
        bin_b = bin_b.ljust(max_len, "0")

        ret, _sum, carry = "", 0, 0
        for i in range(max_len):
            q1 = int(bin_a[i]) & int(bin_b[i])
            q2 = int(bin_a[i]) ^ int(bin_b[i])
            q3 = q2 & carry
            _sum = carry ^ q2
            carry = q1 | q3
            ret += str(_sum)
        if carry:
            ret += str(carry)

        ret = int(ret[::-1], 2) & mask
        if ret > (mask >> 1):
            ret = ~(ret ^ mask)

        return ret


def test_solution(subtests):
    with subtests.test("Example 1"):
        a, b = 1, 2
        output = 3
        assert Solution().getSum(a, b) == output
    with subtests.test("Example 2"):
        a, b = 2, 3
        output = 5
        assert Solution().getSum(a, b) == output
    with subtests.test("Example 3"):
        a, b = -1, 1
        output = 0
        assert Solution().getSum(a, b) == output
    with subtests.test("Example 4"):
        a, b = -12, -8
        output = -20
        assert Solution().getSum(a, b) == output
