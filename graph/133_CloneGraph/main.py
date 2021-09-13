# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        cloned = {node.val: Node(node.val)}
        stack = [node]
        
        while stack:
            node = stack.pop()                
            neighbors = []
            for n in node.neighbors:
                if n.val not in cloned:
                    cloned[n.val] = Node(n.val)
                    stack.append(n)
                neighbors.append(cloned[n.val])
            cloned[node.val].neighbors = neighbors                
        
        return cloned.get(1)
