"""
# 리트코드
# No. 783 / minimum-distance-between-bst-nodes
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
    prev = -sys.maxsize
    min_diff = sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return

            dfs(node.left)
            self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val

            if node.right:
                dfs(node.right)

        dfs(root)
        return self.min_diff


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
        root = [4, 2, 6, 1, 3]
        root = create_tree(root)
        output = 1
        assert Solution().minDiffInBST(root) == output
    with subtests.test("Example 2"):
        root = [1, 0, 48, None, None, 12, 49]
        root = create_tree(root)
        output = 1
        assert Solution().minDiffInBST(root) == output
    with subtests.test("Example 3"):
        root = [99, 84, None, 27, None, 1, 53]
        root = create_tree(root)
        output = 15
        assert Solution().minDiffInBST(root) == output
