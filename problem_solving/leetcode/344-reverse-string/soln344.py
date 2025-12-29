"""
# 리트코드
# No. 344 / reverse-string
# Python 3.x.y
# by "nno0obb"
"""


class Solution:
    def reverseString(self, s: list[str]) -> None:
        s.reverse()


def test_solution(subtests):
    with subtests.test("Example 1"):
        s = ["h", "e", "l", "l", "o"]
        output = ["o", "l", "l", "e", "h"]
        Solution().reverseString(s)
        assert s == output
    with subtests.test("Example 2"):
        s = ["H", "a", "n", "n", "a", "h"]
        output = ["h", "a", "n", "n", "a", "H"]
        Solution().reverseString(s)
        assert s == output
