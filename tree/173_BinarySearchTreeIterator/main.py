# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = [root]
        while (node := self.stack[-1]) and node.left:
            self.stack.append(node.left)

    def next(self) -> int:
        last = self.stack.pop()
        node = last.right
        while node:
            self.stack.append(node)
            node = node.left
        return last.val
           
    def hasNext(self) -> bool:
        return len(self.stack) > 0
