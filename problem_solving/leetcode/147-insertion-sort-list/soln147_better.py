"""
# 리트코드
# No. 147 / insertion-sort-list
# Python 3.x.y
# by "nno0obb"
"""

import sys
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next

    def __eq__(self, other) -> bool:
        node1, node2 = self, other
        while node1 and node2:
            if node1.val != node2.val:
                return False
            node1, node2 = node1.next, node2.next
        return node1 is None and node2 is None


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(-sys.maxsize)
        node = dummy

        curr = head
        while curr:
            while node.next and node.next.val < curr.val:
                node = node.next
            node.next, curr.next, curr = curr, node.next, curr.next

            if curr and curr.val < node.val:
                node = dummy

        return dummy.next


def create_linked_list(values: List[int]) -> ListNode:
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def test_solution(subtests):
    with subtests.test("Example 1"):
        head = [4, 2, 1, 3]
        head = create_linked_list(head)
        output = [1, 2, 3, 4]
        output = create_linked_list(output)
        assert Solution().insertionSortList(head) == output
    with subtests.test("Example 2"):
        head = [-1, 5, 3, 4, 0]
        head = create_linked_list(head)
        output = [-1, 0, 3, 4, 5]
        output = create_linked_list(output)
        assert Solution().insertionSortList(head) == output
