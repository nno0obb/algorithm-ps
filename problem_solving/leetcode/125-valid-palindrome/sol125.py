"""
# 리트코드
# No. 125 / Valid Palindrome
# Python 3.x.y
# by "nno0obb"
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = "".join(c for c in s if c.isalnum()).lower()
        return t == t[::-1]


def test_solution(subtests):
    with subtests.test("Example 1"):
        s = "A man, a plan, a canal: Panama"
        output = True
        assert Solution().isPalindrome(s) == output
    with subtests.test("Example 2"):
        s = "race a car"
        output = False
        assert Solution().isPalindrome(s) == output
    with subtests.test("Example 3"):
        s = " "
        output = True
        assert Solution().isPalindrome(s) == output
