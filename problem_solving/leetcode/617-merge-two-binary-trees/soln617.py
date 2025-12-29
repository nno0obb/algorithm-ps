"""
# 리트코드
# No. 617 / merge-two-binary-trees
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
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2

        if not root2:
            return root1

        root3 = TreeNode()

        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode], node3: Optional[TreeNode]) -> None:
            node3.val = node1.val + node2.val

            if node1.left and node2.left:
                node3.left = TreeNode()
                dfs(node1.left, node2.left, node3.left)
            elif node1.left:
                node3.left = TreeNode()
                dfs(node1.left, TreeNode(), node3.left)
            elif node2.left:
                node3.left = TreeNode()
                dfs(TreeNode(), node2.left, node3.left)
            else:
                node3.left = None

            if node1.right and node2.right:
                node3.right = TreeNode()
                dfs(node1.right, node2.right, node3.right)
            elif node1.right:
                node3.right = TreeNode()
                dfs(node1.right, TreeNode(), node3.right)
            elif node2.right:
                node3.right = TreeNode()
                dfs(TreeNode(), node2.right, node3.right)
            else:
                node3.right = None

        dfs(root1, root2, root3)
        return root3


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
        root1, root2 = [1, 3, 2, 5], [2, 1, 3, None, 4, None, 7]
        root1, root2 = create_tree(root1), create_tree(root2)
        output = [3, 4, 5, 5, 4, None, 7]
        output = create_tree(output)
        assert Solution().mergeTrees(root1, root2) == output
    with subtests.test("Example 2"):
        root1, root2 = [1], [1, 2]
        root1, root2 = create_tree(root1), create_tree(root2)
        output = [2, 2]
        output = create_tree(output)
        assert Solution().mergeTrees(root1, root2) == output
