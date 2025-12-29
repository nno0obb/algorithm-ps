"""
# 리트코드
# No. 20 / valid-parentheses
# Python 3.x.y
# by "nno0obb"
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            elif c in ")}]":
                if not stack:
                    return False
                if c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        return not stack


def test_solution(subtests):
    with subtests.test("Example 1"):
        s = "()"
        assert Solution().isValid(s) is True
    with subtests.test("Example 2"):
        s = "()[]{}"
        assert Solution().isValid(s) is True
    with subtests.test("Example 3"):
        s = "(]"
        assert Solution().isValid(s) is False
    with subtests.test("Example 4"):
        s = "([)]"
        assert Solution().isValid(s) is False
