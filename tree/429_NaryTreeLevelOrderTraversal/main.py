from collections import deque, defaultdict


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        queue = deque([(0, root)])
        result = defaultdict(list)

        while queue:
            level, node = queue.pop()
            if node is None:
                continue

            result[level].append(node.val)

            if node.children:
                for child in node.children:
                    queue.appendleft((level + 1, child))
        
        return [v for v in result.values()]

s = Solution()
print(s.levelOrder(Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])))
print(s.levelOrder(None))
