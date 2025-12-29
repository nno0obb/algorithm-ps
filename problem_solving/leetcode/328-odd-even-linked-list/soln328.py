"""
# 리트코드
# No. 328 / odd-even-linked-list
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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_even, dummy_odd = ListNode(), ListNode()
        tail_even, tail_odd = dummy_even, dummy_odd

        idx = 1
        while head:
            if idx % 2 == 1:
                tail_odd.next = head
                tail_odd = tail_odd.next
            if idx % 2 == 0:
                tail_even.next = head
                tail_even = tail_even.next
            head = head.next
            idx += 1

        tail_odd.next = dummy_even.next
        tail_even.next = None
        return dummy_odd.next


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
        output = [1, 3, 5, 2, 4]
        output = create_linked_list(output)
        assert Solution().oddEvenList(head) == output
    with subtests.test("Example 2"):
        head = [2, 1, 3, 5, 6, 4, 7]
        head = create_linked_list(head)
        output = [2, 3, 6, 7, 1, 5, 4]
        output = create_linked_list(output)
        assert Solution().oddEvenList(head) == output
