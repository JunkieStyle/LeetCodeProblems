from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        nn = defaultdict(list)
        out = defaultdict(int)

        for (fr, to) in tickets:
            nn[fr].append(to)
            out[fr] += 1

        for k, v in nn.items():
            nn[k] = sorted(v, reverse=True)

        result = []
        visited = set()

        def dfs(v):
            while nn[v]:
                w = nn[v].pop()
                dfs(w)

            visited.add(v)
            result.append(v) 

        dfs("JFK")

        return result[::-1]
