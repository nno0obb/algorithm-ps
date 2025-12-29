"""
# 리트코드
# No. 226 / invert-binary-tree
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return

            dfs(node.left)
            dfs(node.right)

            node.left, node.right = node.right, node.left

        dfs(root)
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
        root, output = [4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]
        root, output = create_tree(root), create_tree(output)
        assert Solution().invertTree(root) == output
    with subtests.test("Example 2"):
        root, output = [2, 1, 3], [2, 3, 1]
        root, output = create_tree(root), create_tree(output)
        assert Solution().invertTree(root) == output
