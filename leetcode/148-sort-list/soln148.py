"""
# 리트코드
# No. 148 / sort-list
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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        nodes.sort(key=lambda x: x.val)
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


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
        assert Solution().sortList(head) == output
    with subtests.test("Example 2"):
        head = [-1, 5, 3, 4, 0]
        head = create_linked_list(head)
        output = [-1, 0, 3, 4, 5]
        output = create_linked_list(output)
        assert Solution().sortList(head) == output
