"""
# 리트코드
# No. 771 / jewels-and-stones
# Python 3.x.y
# by "nno0obb"
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in jewels for stone in stones)


def test_solution(subtests):
    with subtests.test("Example 1"):
        jewels, stones = "aA", "aAAbbbb"
        output = 3
        assert Solution().numJewelsInStones(jewels, stones) == output
    with subtests.test("Example 2"):
        jewels, stones = "z", "ZZ"
        output = 0
        assert Solution().numJewelsInStones(jewels, stones) == output
