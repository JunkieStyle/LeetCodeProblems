# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        self.dfs(root, [], result)
        return result
    
    
    def dfs(self, node, path, result):
        for child in [node.left, node.right]:
            if child is not None:
                self.dfs(child, path + [node.val], result)

        if node.left is None and node.right is None:
            result.append("->".join(str(v) for v in path + [node.val]))
