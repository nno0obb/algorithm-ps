"""
# 리트코드
# No. 3 / longest-substring-without-repeating-characters
# Python 3.x.y
# by "nno0obb"
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        ans = 1
        l, r = 0, 0
        while r <= len(s)
            c = s[l:r]
            if len(c) == len(set(c)):
                ans = max(ans, len(c))
                r += 1
            else:
                l += 1
        return ans


def test_solution(subtests):
    with subtests.test("Example 1"):
        s = "abcabcbb"
        output = 3
        assert Solution().lengthOfLongestSubstring(s) == output
    with subtests.test("Example 2"):
        s = "bbbbb"
        output = 1
        assert Solution().lengthOfLongestSubstring(s) == output
    with subtests.test("Example 3"):
        s = "pwwkew"
        output = 3
        assert Solution().lengthOfLongestSubstring(s) == output
    with subtests.test("Example 4"):
        s = "apzivnhwqapyttsmaboaqhcqn"
        output = 11
        assert Solution().lengthOfLongestSubstring(s) == output
    with subtests.test("Example 5"):
        s = ""
        output = 0
        assert Solution().lengthOfLongestSubstring(s) == output
    with subtests.test("Example 6"):
        s = " "
        output = 1
        assert Solution().lengthOfLongestSubstring(s) == output
    with subtests.test("Example 7"):
        s = "au"
        output = 2
        assert Solution().lengthOfLongestSubstring(s) == output
