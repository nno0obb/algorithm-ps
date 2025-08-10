"""
# 리트코드
# No. 316 / remove-duplicate-letters
# Python 3.x.y
# by "nno0obb"
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Redo
        pass


def test_solution(subtests):
    with subtests.test("Example 1"):
        s = "bcabc"
        assert Solution().removeDuplicateLetters(s) == "abc"
    with subtests.test("Example 2"):
        s = "cbacdcbc"
        assert Solution().removeDuplicateLetters(s) == "acdb"
    with subtests.test("Example 3"):
        s = "dcbadcba"
        assert Solution().removeDuplicateLetters(s) == "adcb"
