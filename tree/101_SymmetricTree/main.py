from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.symmetric_iterative(root)
        return self.symmetric_recursive(root.left, root.right)
        
    def symmetric_recursive(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None:
            return False
        if t2 is None:
            return False
            
        return (
            t1.val == t2.val
            and self.symmetric_recursive(t1.right, t2.left)
            and self.symmetric_recursive(t1.left, t2.right)
        )
    
    def symmetric_iterative(self, root):
        queue = deque([root, root])
        while queue:
            node1 = queue.pop()
            node2 = queue.pop()

            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False

            queue.appendleft(node1.left)
            queue.appendleft(node2.right)
            queue.appendleft(node2.left)
            queue.appendleft(node1.right)

        return True
