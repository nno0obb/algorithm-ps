"""
# 리트코드
# No. 105 / construct-binary-tree-from-preorder-and-inorder-traversal
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

    def __eq__(self, other: object) -> bool:
        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and dfs(node1.left, node2.left) and dfs(node1.right, node2.right)

        return dfs(self, other)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def makeTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            if not preorder or not inorder:
                return None

            root = TreeNode(preorder[0])

            mid_idx = inorder.index(root.val)

            root.left = makeTree(preorder[1 : mid_idx + 1], inorder[:mid_idx])
            root.right = makeTree(preorder[mid_idx + 1 :], inorder[mid_idx + 1 :])

            return root

        return makeTree(preorder, inorder)


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
        preorder, inorder = [3, 9, 20, 15, 7], [9, 3, 15, 20, 7]
        output = [3, 9, 20, None, None, 15, 7]
        output = create_tree(output)
        assert Solution().buildTree(preorder, inorder) == output
    with subtests.test("Example 2"):
        preorder, inorder = [-1], [-1]
        output = [-1]
        output = create_tree(output)
        assert Solution().buildTree(preorder, inorder) == output
