"""
# 리트코드
# No. 92 / reverse-linked-list-ii
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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy

        for _ in range(left - 1):
            node = node.next
        reverse_head_prev = node
        reverse_head = reverse_head_prev.next

        for _ in range(right - left + 1):
            node = node.next
        reverse_tail = node
        reverse_tail_next = node.next
        reverse_tail.next = None

        # Reverse
        curr, prev = reverse_head, None
        for _ in range(right - left + 1):
            _next, curr.next = curr.next, prev
            curr, prev = _next, curr

        reverse_head_prev.next = reverse_tail
        reverse_head.next = reverse_tail_next
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
        head, left, right = [1, 2, 3, 4, 5], 2, 4
        head = create_linked_list(head)
        output = [1, 4, 3, 2, 5]
        output = create_linked_list(output)
        assert Solution().reverseBetween(head, left, right) == output
    with subtests.test("Example 2"):
        head, left, right = [5], 1, 1
        head = create_linked_list(head)
        output = [5]
        output = create_linked_list(output)
        assert Solution().reverseBetween(head, left, right) == output
    with subtests.test("Example 3"):
        head, left, right = [3, 5], 1, 2
        head = create_linked_list(head)
        output = [5, 3]
        output = create_linked_list(output)
        assert Solution().reverseBetween(head, left, right) == output
