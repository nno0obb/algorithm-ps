"""
# 리트코드
# No. 104 / maximum-depth-of-binary-tree
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 0
        que = deque([root])
        while que:
            depth += 1
            for _ in range(len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return depth


def create_tree(values: List[int]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    que = [(root, 0)]
    while que:
        node, idx = que.pop(0)
        if idx * 2 + 1 < len(values):
            node.left = TreeNode(values[idx * 2 + 1])
            que.append((node.left, idx * 2 + 1))
        if idx * 2 + 2 < len(values):
            node.right = TreeNode(values[idx * 2 + 2])
            que.append((node.right, idx * 2 + 2))
    return root


def test_solution(subtests):
    with subtests.test("Example 1"):
        root = [3, 9, 20, None, None, 15, 7]
        root = create_tree(root)
        assert Solution().maxDepth(root) == 3
    with subtests.test("Example 2"):
        root = [1, None, 2]
        root = create_tree(root)
        assert Solution().maxDepth(root) == 2
