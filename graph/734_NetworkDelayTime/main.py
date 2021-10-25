from typing import List
from math import inf
from heapq import heapify, heappop, heappush


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        results = [inf] * n
        visited = set()

        nn = [[] for _ in range(n)]
        for v, w, t in times:
            nn[v - 1].append((t, w - 1))
            

        heap = [(0, k - 1)]
        heapify(heap)
        results[k - 1] = 0
        
        while heap:
            curr, v = heappop(heap)
            visited.add(v)
            
            for t, w in nn[v]:
                if w not in visited:
                    if results[v] + t < results[w]:
                        results[w] = results[v] + t
                        heappush(heap, (results[w], w))
        
        res = max(results)
        if res is inf:
            res = -1
        
        return res
