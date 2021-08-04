# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        if not root:
            return []
        
        if not root.left and not root.right:
            if targetSum == root.val:
                return [[root.val]]
            return []
        
        diff = targetSum - root.val
        paths = self.pathSum(root.left, diff) + self.pathSum(root.right, diff)
        return [[root.val] + p for p in paths]
