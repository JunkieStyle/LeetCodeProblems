# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        n = 0
                
        while root:
            r_h = self.get_height(root)
            mid_h = self.get_height(root.left) + 1
            n += 2 ** (mid_h - 1)

            if mid_h == r_h:
                root = root.left
            else:
                root = root.right                

        return n
    
    def get_height(self, node):
        h = 0
        while node:
            h += 1
            node = node.right
        return h
