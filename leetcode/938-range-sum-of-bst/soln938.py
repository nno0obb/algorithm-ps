"""
# 리트코드
# No. 938 / range-sum-of-bst
# Python 3.x.y
# by "nno0obb"
"""

from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node: Optional[TreeNode], acc: int) -> int:
            if not node:
                return acc

            if low <= node.val <= high:
                acc += node.val

            if node.val > high:
                acc = dfs(node.left, acc)
            elif node.val < low:
                acc = dfs(node.right, acc)
            else:
                acc = dfs(node.left, acc)
                acc = dfs(node.right, acc)

            return acc

        return dfs(root, 0)


def create_tree(values: List[int]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    que, idx = deque([root]), 1

    while que:
        node = que.popleft()
        if idx < len(values) and values[idx] is not None:
            node.left = TreeNode(values[idx])
            que.append(node.left)
        idx += 1
        if idx < len(values) and values[idx] is not None:
            node.right = TreeNode(values[idx])
            que.append(node.right)
        idx += 1
    return root


def test_solution(subtests):
    with subtests.test("Example 1"):
        root, low, high = [10, 5, 15, 3, 7, None, 18], 7, 15
        root = create_tree(root)
        output = 32
        assert Solution().rangeSumBST(root, low, high) == output
    with subtests.test("Example 2"):
        root, low, high = [10, 5, 15, 3, 7, 13, 18, 1, None, 6], 6, 10
        root = create_tree(root)
        output = 23
        assert Solution().rangeSumBST(root, low, high) == output
