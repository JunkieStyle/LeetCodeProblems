from typing import List


class Solution:    
    def hIndex(self, citations: List[int]) -> int:     
        buckets = [0] * (len(citations) + 1)
        for c in citations:
            if c > len(citations):
                buckets[-1] += 1
            else:
                buckets[c] += 1
        
        s = 0
        for i in range(len(citations), -1, -1):
            s += buckets[i]
            if s >= i:
                return i
