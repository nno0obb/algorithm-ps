"""
# 리트코드
# No. 783 / minimum-distance-between-bst-nodes
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
    def __init__(self):
        self.nums = []

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            self.nums.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        self.nums.sort()
        return min(self.nums[i] - self.nums[i - 1] for i in range(1, len(self.nums)))


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
