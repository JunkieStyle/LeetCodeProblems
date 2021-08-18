class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = {}
        
        for i in range(len(s)):
            if s[i] not in h:
                h[s[i]] = i
            else:
                h[s[i]] = -1
                
        
        result = [v for v in h.values() if v >= 0]
        return  min(result) if result else -1
