"""
# 리트코드
# No. 21 / merge-two-sorted-lists
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = list1, list2
        if not node1 or (node2 and node1.val > node2.val):
            node1, node2 = node2, node1
        if node1:
            node1.next = self.mergeTwoLists(node1.next, node2)
        return node1


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
        list1, list2 = [1, 2, 4], [1, 3, 4]
        list1, list2 = create_linked_list(list1), create_linked_list(list2)
        output = [1, 1, 2, 3, 4, 4]
        output = create_linked_list(output)
        assert Solution().mergeTwoLists(list1, list2) == output
    with subtests.test("Example 2"):
        list1, list2 = [], []
        list1, list2 = create_linked_list(list1), create_linked_list(list2)
        output = []
        output = create_linked_list(output)
        assert Solution().mergeTwoLists(list1, list2) == output
    with subtests.test("Example 3"):
        list1, list2 = [], [0]
        list1, list2 = create_linked_list(list1), create_linked_list(list2)
        output = [0]
        output = create_linked_list(output)
        assert Solution().mergeTwoLists(list1, list2) == output
