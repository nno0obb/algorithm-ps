"""
# 리트코드
# No. 17 / letter-combinations-of-a-phone-number
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        d2l = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        curr = [""]
        for digit in digits:
            _next = []
            for letter in d2l[digit]:
                for letter_combination in curr:
                    _next.append(letter_combination + letter)
            curr = _next
        letter_combinations = curr

        return letter_combinations


def test_solution(subtests):
    with subtests.test("Example 1"):
        digits = "23"
        output = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        assert sorted(Solution().letterCombinations(digits)) == sorted(output)
    with subtests.test("Example 2"):
        digits = ""
        output = []
        assert sorted(Solution().letterCombinations(digits)) == sorted(output)
    with subtests.test("Example 3"):
        digits = "2"
        output = ["a", "b", "c"]
        assert sorted(Solution().letterCombinations(digits)) == sorted(output)
