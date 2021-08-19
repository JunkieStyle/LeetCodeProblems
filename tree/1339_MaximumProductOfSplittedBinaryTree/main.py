# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        result = [0]
        total = self.helper(root)
        self.helper(root, total, result)
        return result[0] % (10**9 + 7)
        
    
    def helper(self, node, total=None, result=None):
        if not node:
            return 0
        
        s = node.val
        s += self.helper(node.left, total, result)
        s += self.helper(node.right, total, result)
        
        if total is not None and result is not None:
            result[0] = max(s * (total - s), result[0])
        return s
