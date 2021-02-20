# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.inorderTraversal_iter(root)

    def inorderTraversal_recur(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return (
            self.inorderTraversal(root.left) +
            [root.val] +
            self.inorderTraversal(root.right)
        )

    def inorderTraversal_iter(self, root: TreeNode) -> List[int]:
        stack = []
        res = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res
