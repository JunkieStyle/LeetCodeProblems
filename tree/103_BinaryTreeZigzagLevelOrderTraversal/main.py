from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:   
        if not root:
            return []
        
        queue = deque([root])
        result = []
        mode = "zag"
        
        while queue:
            curr = []
            for _ in range(len(queue)):
                if mode == "zig":
                    node = queue.pop()
                    if node.right: queue.appendleft(node.right)
                    if node.left: queue.appendleft(node.left)
                        
                if mode == "zag":
                    node = queue.popleft()
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
                        
                curr.append(node.val)

            mode = "zig" if mode == "zag" else "zag"
            
            if curr:
                result.append(curr)
                
        return result
