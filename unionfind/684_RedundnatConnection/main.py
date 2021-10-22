from typing import List 


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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ufs = UnionFindSet(1001)
        
        result = None
        for edge in edges:
            if not ufs.union(*edge):
                result = edge

        return result