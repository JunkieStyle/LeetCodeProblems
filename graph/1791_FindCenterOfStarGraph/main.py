from typing import List
from collections import defaultdict


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        counter = defaultdict(int)
        for a, b in edges:
            counter[a] += 1
            counter[b] += 1

        for k, v in counter.items():
            if v == len(counter) - 1:
                return k