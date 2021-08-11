# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = [0]
        self.dfs(root, [], result)
        return result[0]
        
    def dfs(self, node, path, result):
        if node.left:
            self.dfs(node.left, path + [node.val], result)
        if node.right:
            self.dfs(node.right, path + [node.val], result)
        if not node.left and not node.right:
            result[0] += int("".join(str(v) for v in path + [node.val]))
