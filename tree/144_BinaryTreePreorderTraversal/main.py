# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.preorderTraversal_iterative(root)
    
    def preorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    
    def preorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            if not node:
                continue
                
            result.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
                
        return result
