"""
# 리트코드
# No. 23 / merge-k-sorted-lists
# Python 3.x.y
# by "nno0obb"
"""

import heapq
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for head in lists:
            curr = head
            while curr:
                heapq.heappush(heap, (curr.val, id(curr), curr))
                curr = curr.next
        heapq.heapify(heap)

        dummy = ListNode(-1)
        curr = dummy
        while heap:
            node = heapq.heappop(heap)[2]
            node.next = None
            curr.next = node
            curr = curr.next

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
        lists = [
            create_linked_list([1, 4, 5]),
            create_linked_list([1, 3, 4]),
            create_linked_list([2, 6]),
        ]
        output = create_linked_list([1, 1, 2, 3, 4, 4, 5, 6])
        assert Solution().mergeKLists(lists) == output
    with subtests.test("Example 2"):
        lists = []
        output = create_linked_list([])
        assert Solution().mergeKLists(lists) == output
    with subtests.test("Example 3"):
        lists = [create_linked_list([])]
        output = create_linked_list([])
        assert Solution().mergeKLists(lists) == output
