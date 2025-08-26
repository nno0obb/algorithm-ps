"""
# 리트코드
# No. 543 / diameter-of-binary-tree
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
    diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            self.diameter = max(self.diameter, left_depth + right_depth)
            return max(left_depth, right_depth) + 1

        dfs(root)
        return self.diameter


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
        root = [1, 2, 3, 4, 5]
        root = create_tree(root)
        assert Solution().diameterOfBinaryTree(root) == 3
    with subtests.test("Example 2"):
        root = [1, 2]
        root = create_tree(root)
        assert Solution().diameterOfBinaryTree(root) == 1
    with subtests.test("Example 3"):
        root = [
            4,
            -7,
            -3,
            None,
            None,
            -9,
            -3,
            9,
            -7,
            -4,
            None,
            6,
            None,
            -6,
            -6,
            None,
            None,
            0,
            6,
            5,
            None,
            9,
            None,
            None,
            -1,
            -4,
            None,
            None,
            None,
            -2,
        ]
        root = create_tree(root)
        assert Solution().diameterOfBinaryTree(root) == 8
