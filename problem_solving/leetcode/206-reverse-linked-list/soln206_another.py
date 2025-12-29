"""
# 리트코드
# No. 206 / reverse-linked-list
# Python 3.x.y
# by "nno0obb"
"""

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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(curr: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
            if not curr:
                return prev
            _next, curr.next = curr.next, prev
            return reverse(_next, curr)

        return reverse(head, None)


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
        head = [1, 2, 3, 4, 5]
        head = create_linked_list(head)
        output = [5, 4, 3, 2, 1]
        output = create_linked_list(output)
        assert Solution().reverseList(head) == output
    with subtests.test("Example 2"):
        head = [1, 2]
        head = create_linked_list(head)
        output = [2, 1]
        output = create_linked_list(output)
        assert Solution().reverseList(head) == output
    with subtests.test("Example 3"):
        head = []
        head = create_linked_list(head)
        output = []
        output = create_linked_list(output)
        assert Solution().reverseList(head) == output
