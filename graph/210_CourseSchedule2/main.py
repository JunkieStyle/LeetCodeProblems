from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        neighbours = [[] for _ in range(numCourses)]
        degrees = [0] * numCourses
        for a, b in prerequisites:
            neighbours[b].append(a)
            degrees[a] += 1

        result = []
        queue = deque([i for i, d in enumerate(degrees) if d == 0])
        while queue:
            v = queue.pop()
            result.append(v)
            for n in neighbours[v]:
                degrees[n] -= 1
                if degrees[n] == 0:
                    queue.appendleft(n)
        
        return result if len(result) == numCourses else []
