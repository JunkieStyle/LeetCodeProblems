# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.dfs(1, n + 1)
        
    def dfs(self, start, end):
        if start == end:
            return [None]
        
        result = []
        for i in range(start, end):
            for left in self.dfs(start, i):
                for right in self.dfs(i + 1, end):
                    node = TreeNode(i, left, right) 
                    result.append(node)
        return result        
