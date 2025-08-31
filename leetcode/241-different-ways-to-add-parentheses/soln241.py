"""
# 리트코드
# No. 241 / different-ways-to-add-parentheses
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        expr = expression
        if expr.isdigit():
            return [int(expr)]

        ret = []
        for i in range(len(expr)):
            if expr[i] in "+-*":
                left = self.diffWaysToCompute(expr[:i])
                right = self.diffWaysToCompute(expr[i + 1 :])
                for l in left:
                    for r in right:
                        if expr[i] == "+":
                            ret.append(l + r)
                        elif expr[i] == "-":
                            ret.append(l - r)
                        elif expr[i] == "*":
                            ret.append(l * r)
                        else:
                            raise RuntimeError()
        return ret


def test_solution(subtests):
    with subtests.test("Example 1"):
        expression = "2-1-1"
        output = [0, 2]
        assert sorted(Solution().diffWaysToCompute(expression)) == sorted(output)
    with subtests.test("Example 2"):
        expression = "2*3-4*5"
        output = [-34, -14, -10, -10, 10]
        assert sorted(Solution().diffWaysToCompute(expression)) == sorted(output)
