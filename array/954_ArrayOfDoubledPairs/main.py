from collections import Counter
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        
        for k in sorted(counts.keys(), key=abs):
            if counts[k] < 0:
                return False
            counts[k * 2] -= counts[k]
            counts[k] = 0
        
        return not any(counts.values())
