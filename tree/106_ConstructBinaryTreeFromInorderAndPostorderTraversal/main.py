from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorder_hash = {v: i for i, v in enumerate(inorder)}

        def _build_node(l, r):
            if l > r:
                return None

            node = TreeNode(val=postorder.pop())
            root = inorder_hash[node.val]
            node.right = _build_node(root + 1, r)
            node.left = _build_node(l, root - 1)
            return node

        return _build_node(0, len(inorder) - 1)
