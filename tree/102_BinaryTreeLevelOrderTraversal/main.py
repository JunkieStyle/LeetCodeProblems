# Definition for a binary tree node.
from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        result = []
        while queue:
            level = [] 
            for _ in range(len(queue)):
                node = queue.pop()
                if node:
                    queue.appendleft(node.left)
                    queue.appendleft(node.right)
                    level.append(node.val)
            if level:
                result.append(level)
        return result
