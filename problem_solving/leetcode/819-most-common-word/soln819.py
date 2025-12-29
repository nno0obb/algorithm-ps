"""
# 리트코드
# No. 819 / most-common-word
# Python 3.x.y
# by "nno0obb"
"""

import re
from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words_cleaned = re.sub(r"[^\w]", " ", paragraph).lower().split()
        words_not_banned = [word for word in words_cleaned if word not in banned]
        return Counter(words_not_banned).most_common(1)[0][0]


def test_solution(subtests):
    with subtests.test("Example 1"):
        paragraph, banned = "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]
        output = "ball"
        assert Solution().mostCommonWord(paragraph, banned) == output
    with subtests.test("Example 2"):
        paragraph, banned = "a.", []
        output = "a"
        assert Solution().mostCommonWord(paragraph, banned) == output
