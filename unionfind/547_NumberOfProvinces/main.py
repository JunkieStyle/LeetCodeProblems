from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        neighbors = [
            [j for j, v in enumerate(row) if v and i != j] 
            for i, row in enumerate(isConnected)
        ]

        visited = set()
        components = 0

        for i in range(len(neighbors)):
            if i in visited:
                continue
                
            components += 1
            stack = [i]
            while stack:
                v = stack.pop()
                
                if v in visited:
                    continue

                visited.add(v)

                for vv in neighbors[v]:
                    stack.append(vv)

        return components
