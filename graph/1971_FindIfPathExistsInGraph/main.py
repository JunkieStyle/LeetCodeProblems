from typing import List
from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adj_lists = defaultdict(list)
        for edge in edges:
            adj_lists[edge[0]].append(edge[1])
            adj_lists[edge[1]].append(edge[0])

        stack = [start]
        visited = set()

        while stack:
            vertex = stack.pop()
            if vertex == end:
                return True

            visited.add(vertex)

            for v in adj_lists[vertex]:
                if v not in visited:
                    stack.append(v)

        return False
