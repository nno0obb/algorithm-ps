"""
# 리트코드
# No. 110 / balanced-binary-tree
# Python 3.x.y
# by "nno0obb"
"""

import sys
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    FALSE = -sys.maxsize

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)
            if left_height == self.FALSE or right_height == self.FALSE:
                return self.FALSE
            if abs(left_height - right_height) > 1:
                return self.FALSE
            return max(left_height, right_height) + 1

        return dfs(root) != self.FALSE


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
        root = [3, 9, 20, None, None, 15, 7]
        root = create_tree(root)
        assert Solution().isBalanced(root) is True
    with subtests.test("Example 2"):
        root = [1, 2, 2, 3, 3, None, None, 4, 4]
        root = create_tree(root)
        assert Solution().isBalanced(root) is False
    with subtests.test("Example 3"):
        root = []
        root = create_tree(root)
        assert Solution().isBalanced(root) is True
