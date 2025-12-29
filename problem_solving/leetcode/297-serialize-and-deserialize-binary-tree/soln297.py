"""
# 리트코드
# No. 297 / serialize-and-deserialize-binary-tree
# Python 3.x.y
# by "nno0obb"
"""

from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other) -> bool:
        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and dfs(node1.left, node2.left) and dfs(node1.right, node2.right)

        return dfs(self, other)


class Codec:

    def serialize(self, root: TreeNode):
        if not root:
            return "None"

        que, vals = deque([root]), []
        while que:
            node = que.popleft()
            if node:
                vals.append(str(node.val))
                que.append(node.left)
                que.append(node.right)
            else:
                vals.append("None")

        return ",".join(vals)

    def deserialize(self, data: str):
        values = data.split(",")
        values = list(map(lambda x: int(x) if x != "None" else None, values))
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
        ser, deser = Codec(), Codec()
        root = [1, 2, 3, None, None, 4, 5]
        root = create_tree(root)
        assert deser.deserialize(ser.serialize(root)) == root
    with subtests.test("Example 2"):
        ser, deser = Codec(), Codec()
        root = []
        root = create_tree(root)
        assert deser.deserialize(ser.serialize(root)) == root
