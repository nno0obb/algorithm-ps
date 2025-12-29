"""
# 리트코드
# No. 937 / reorder-data-in-log-files
# Python 3.x.y
# by "nno0obb"
"""

from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        for log in logs:
            if log.split()[1].isalpha():
                letter_logs.append(log)
            elif log.split()[1].isdigit():
                digit_logs.append(log)
        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letter_logs + digit_logs


def test_solution(subtests):
    with subtests.test("Example 1"):
        logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
        output = ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
        assert Solution().reorderLogFiles(logs) == output
    with subtests.test("Example 2"):
        logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
        output = ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
        assert Solution().reorderLogFiles(logs) == output
