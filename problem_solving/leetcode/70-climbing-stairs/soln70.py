"""
# 리트코드
# No. 70 / climbing-stairs
# Python 3.x.y
# by "nno0obb"
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


def test_solution(subtests):
    with subtests.test("Example 1"):
        n = 2
        output = 2
        assert Solution().climbStairs(n) == output
    with subtests.test("Example 2"):
        n = 3
        output = 3
        assert Solution().climbStairs(n) == output
