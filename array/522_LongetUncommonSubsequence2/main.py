from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        for s in sorted(strs, key=len, reverse=True):
            if sum(self.is_subsequence(s, s2) for s2 in strs if len(s2) >= len(s)) == 1:
                return len(s)
        return -1
    
    def is_subsequence(self, s1, s2):
        it = iter(s2)
        return all(c in it for c in s1)
