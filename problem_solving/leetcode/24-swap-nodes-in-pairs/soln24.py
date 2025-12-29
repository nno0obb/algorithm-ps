"""
# 리트코드
# No. 24 / swap-nodes-in-pairs
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
    def swapPair(self, curr: Optional[ListNode]) -> Optional[ListNode]:
        if not curr or not curr.next:
            return curr
        _next = curr.next
        _next.next, curr.next = curr, self.swapPair(_next.next)
        return _next

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.swapPair(head)


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
        head = [1, 2, 3, 4]
        head = create_linked_list(head)
        output = [2, 1, 4, 3]
        output = create_linked_list(output)
        assert Solution().swapPairs(head) == output
    with subtests.test("Example 2"):
        head = []
        head = create_linked_list(head)
        output = []
        output = create_linked_list(output)
        assert Solution().swapPairs(head) == output
    with subtests.test("Example 3"):
        head = [1]
        head = create_linked_list(head)
        output = [1]
        output = create_linked_list(output)
        assert Solution().swapPairs(head) == output
    with subtests.test("Example 4"):
        head = [1, 2, 3]
        head = create_linked_list(head)
        output = [2, 1, 3]
        output = create_linked_list(output)
        assert Solution().swapPairs(head) == output
