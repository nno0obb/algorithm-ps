"""
# 리트코드
# No. 509 / fibonacci-number
# Python 3.x.y
# by "nno0obb"
"""


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)


def test_solution(subtests):
    with subtests.test("Example 1"):
        n = 2
        output = 1
        assert Solution().fib(n) == output
    with subtests.test("Example 2"):
        n = 3
        output = 2
        assert Solution().fib(n) == output
    with subtests.test("Example 3"):
        n = 4
        output = 3
        assert Solution().fib(n) == output
