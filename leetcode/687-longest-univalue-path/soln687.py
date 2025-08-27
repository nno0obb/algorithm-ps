"""
# 리트코드
# No. 687 / longest-univalue-path
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
    length_of_longest_path = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            if node.left and node.left.val == node.val:
                left_depth += 1
            else:
                left_depth = 0
            if node.right and node.right.val == node.val:
                right_depth += 1
            else:
                right_depth = 0

            self.length_of_longest_path = max(self.length_of_longest_path, left_depth + right_depth)
            return max(left_depth, right_depth)

        dfs(root)
        return self.length_of_longest_path


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
        root, output = [5, 4, 5, 1, 1, None, 5], 2
        root = create_tree(root)
        assert Solution().longestUnivaluePath(root) == output
    with subtests.test("Example 2"):
        root, output = [1, 4, 5, 4, 4, None, 5], 2
        root = create_tree(root)
        assert Solution().longestUnivaluePath(root) == output
