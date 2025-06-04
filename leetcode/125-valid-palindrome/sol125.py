"""
# 리트코드
# No. 125 / Valid Palindrome
# Python 3.11.9
# by "nno0obb"
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = "".join(c for c in s if c.isalnum()).lower()
        return t == t[::-1]


def test_solution(subtests):
    with subtests.test("Example 1"):
        assert Solution().isPalindrome(s="A man, a plan, a canal: Panama") is True
    with subtests.test("Example 2"):
        assert Solution().isPalindrome(s="race a car") is False
    with subtests.test("Example 3"):
        assert Solution().isPalindrome(s=" ") is True
