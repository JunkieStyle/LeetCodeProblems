# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        stack = [(root, 0)]

        while stack:
            node, level = stack.pop()
            if not node:
                continue

            if len(result) == level:
                result.append([])
            result[level].append(node.val)

            stack.append((node.right, level + 1))
            stack.append((node.left, level + 1))

        return result[::-1]

