from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([root])
        x_ = None
        y_ = None
        depth = 0

        while queue and (not x_ or not y_):
            for _ in range(len(queue)):
                node = queue.pop()
                if not node:
                    continue

                if node.left and node.left.val == x:
                    x_ = (node, depth)
                
                if node.right and node.right.val == y:
                    y_ = (node, depth)

                queue.appendleft(node.left)
                queue.appendleft(node.right)

            depth += 1

        return x_[0] != y_[0] and x[1] == y[1]            
