"""
# 리트코드
# No. 2 / add-two-numbers
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr, c1, c2 = dummy, l1, l2
        carry = 0
        while c1 or c2 or carry:
            v1 = c1.val if c1 else 0
            v2 = c2.val if c2 else 0
            carry, val = divmod(v1 + v2 + carry, 10)

            curr.next = ListNode(val)

            curr = curr.next
            c1 = c1.next if c1 else None
            c2 = c2.next if c2 else None

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
        l1, l2 = [2, 4, 3], [5, 6, 4]
        l1, l2 = create_linked_list(l1), create_linked_list(l2)
        output = [7, 0, 8]
        output = create_linked_list(output)
        assert Solution().addTwoNumbers(l1, l2) == output
    with subtests.test("Example 2"):
        l1, l2 = [0], [0]
        l1, l2 = create_linked_list(l1), create_linked_list(l2)
        output = [0]
        output = create_linked_list(output)
        assert Solution().addTwoNumbers(l1, l2) == output
    with subtests.test("Example 3"):
        l1, l2 = [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]
        l1, l2 = create_linked_list(l1), create_linked_list(l2)
        output = [8, 9, 9, 9, 0, 0, 0, 1]
        output = create_linked_list(output)
        assert Solution().addTwoNumbers(l1, l2) == output
