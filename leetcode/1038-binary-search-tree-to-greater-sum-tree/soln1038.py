"""
# 리트코드
# No. 1038 / binary-search-tree-to-greater-sum-tree
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

    def __eq__(self, other) -> bool:
        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and dfs(node1.left, node2.left) and dfs(node1.right, node2.right)

        return dfs(self, other)


class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode], acc: int) -> int:
            if not node:
                return acc

            acc = dfs(node.right, acc)
            node.val += acc
            return dfs(node.left, node.val)

        dfs(root, 0)
        return root


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
        root = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
        root = create_tree(root)
        output = [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]
        output = create_tree(output)
        assert Solution().bstToGst(root) == output
    with subtests.test("Example 2"):
        root = [0, None, 1]
        root = create_tree(root)
        output = [1, None, 1]
        output = create_tree(output)
        assert Solution().bstToGst(root) == output
