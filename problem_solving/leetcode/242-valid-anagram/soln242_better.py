"""
# 리트코드
# No. 242 / valid-anagram
# Python 3.x.y
# by "nno0obb"
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


def test_solution(subtests):
    with subtests.test("Example 1"):
        s, t = "anagram", "nagaram"
        output = True
        assert Solution().isAnagram(s, t) == output
    with subtests.test("Example 2"):
        s, t = "rat", "car"
        output = False
        assert Solution().isAnagram(s, t) == output
