"""
# 리트코드
# No. 234 / palindrome-linked-list
# Python 3.x.y
# by "nno0obb"
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev, slow, fast = None, head, head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return rev is None


def create_linked_list(values: List[int]) -> ListNode:
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def test_solution(subtests):
    with subtests.test("Example 1"):
        head = [1, 2, 2, 1]
        head = create_linked_list(head)
        output = True
        assert Solution().isPalindrome(head) == output

    with subtests.test("Example 2"):
        head = [1, 2]
        head = create_linked_list(head)
        output = False
        assert Solution().isPalindrome(head) == output
