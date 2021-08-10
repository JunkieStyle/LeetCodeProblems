# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, None, None)]
        
        while stack:
            node, min_value, max_value = stack.pop()
            
            if not node:
                continue
                
            if min_value is not None and node.val <= min_value:
                return False
            
            if max_value is not None and node.val >= max_value:
                return False
                        
            if node.left is not None:
                stack.append((node.left, min_value, node.val))
                
            if node.right is not None:
                stack.append((node.right, node.val, max_value))

        return True
