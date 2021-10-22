from typing import List
from math import inf
    

class UnionFindSet:
    def __init__(self, n) -> None:
        self.parents = list(range(n))
        self.ranks = [1] * n
        self.count = n

    def find(self, v) -> int:
        if v != self.parents[v]:
            self.parents[v] = self.find(self.parents[v])
        return self.parents[v]

    def union(self, v, w) -> bool:
        pv = self.find(v)
        pw = self.find(w)

        if pv == pw:
            return False

        if self.ranks[pv] > self.ranks[pw]:
            self.parents[pw] = self.parents[pv]
        elif self.ranks[pv] < self.ranks[pw]:
            self.parents[pv] = self.parents[pw]
        else:
            self.parents[pv] = self.parents[pw]
            self.ranks[pv] += 1

        self.count -= 1

        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indices = sorted(range(len(edges)), key=lambda x: edges[x][2])

        def mst(include=None, exclude=None):
            ufs = UnionFindSet(n)
            score = 0
            result = []

            if include is not None:
                edge = edges[include]
                ufs.union(edge[0], edge[1])
                score += edge[2]
                result.append(edge)

            for i in indices:
                if i == exclude or i == include:
                    continue

                edge = edges[i]
                if ufs.union(edge[0], edge[1]):
                    score += edge[2]
                    result.append(edge)
                
                if len(result) == n - 1:
                    return score
            
            return inf

        base = mst()
        crit = []
        pcrit = []
        for i in range(len(edges)):
            if mst(exclude=i) > base:
                crit.append(i)
            elif mst(include=i) == base:
                pcrit.append(i)
                       
        return [crit, pcrit]
        