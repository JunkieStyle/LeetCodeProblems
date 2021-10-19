from typing import List
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:        
        curr_set = set()
        other_set = set()
        
        for i in range(len(graph)):
            if i in curr_set | other_set:
                continue

            queue = deque([i])
            
            while queue:
                for _ in range(len(queue)):
                    v = queue.pop()

                    if v in other_set:
                        return False

                    if v in curr_set:
                        continue

                    curr_set.add(v)

                    for n in graph[v]:
                        queue.appendleft(n)

                curr_set, other_set = other_set, curr_set
    
        return True
