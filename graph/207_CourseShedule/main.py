from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0] * numCourses
        
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a) 

        def dfs(v):
            if visited[v] == -1:
                return False

            if visited[v] == 1:
                return True 

            visited[v] = -1
            result = all(dfs(p) for p in graph[v])
            visited[v] = 1

            return result

        for course in range(numCourses):
            if visited[course] == 1:
                continue
            
            if not dfs(course):
                return False
        
        return True

    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        outs = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses
        for a, b in prerequisites:
            outs[b].append(a)
            in_degrees[a] += 1

        queue = deque(i for i, d in enumerate(in_degrees) if d == 0)
        
        n = numCourses

        while queue:
            v = queue.pop()
            n -= 1

            for p in outs[v]: 
                in_degrees[p] -= 1
                if in_degrees[p] == 0:
                    queue.appendleft(p)

        return n == 0