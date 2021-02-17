from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        in_hash = {v: i for i, v in enumerate(inorder)}

        def buildNode(c, l, r):
            if l > r or c < 0:
                return

            node = TreeNode(val=preorder[c])
            ci = in_hash[node.val]
            node.left = buildNode(c + 1, l, ci - 1)
            node.right = buildNode(c + 1 + (ci - l), ci + 1, r)
            return node

        return buildNode(0, 0, len(inorder) - 1)


if __name__ == '__main__':
    s = Solution()
    r = s.buildTree([3,9,20,15,7], [9,3,15,20,7])
