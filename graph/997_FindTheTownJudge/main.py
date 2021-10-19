from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        c = defaultdict(int)
        for a, b in trust:
            c[a] -= 1
            c[b] += 1
            
        for i in range(1, n + 1):
            if c[i] == n - 1:
                return i
            
        return -1
    