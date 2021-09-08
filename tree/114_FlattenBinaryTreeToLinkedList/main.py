# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = [root]
        curr = TreeNode(None)
        
        while stack:
            node = stack.pop()
            if not node:
                continue
            
            curr.left = None
            curr.right = node
            stack.append(node.right)
            stack.append(node.left)
            curr = curr.right
            
        return root
            