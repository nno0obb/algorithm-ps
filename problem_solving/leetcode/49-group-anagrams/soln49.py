"""
# 리트코드
# No. 49 / group-anagrams
# Python 3.x.y
# by "nno0obb"
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            anagrams["".join(sorted(word))].append(word)
        return list(anagrams.values())


def test_solution(subtests):
    with subtests.test("Example 1"):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        assert Solution().groupAnagrams(strs) == output
    with subtests.test("Example 2"):
        strs = [""]
        output = [[""]]
        assert Solution().groupAnagrams(strs) == output
    with subtests.test("Example 3"):
        strs = ["a"]
        output = [["a"]]
        assert Solution().groupAnagrams(strs) == output
