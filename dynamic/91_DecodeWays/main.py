class Solution:
    def numDecodings(self, s: str) -> int:        
        prev1 = 1
        prev2 = 0
        correct = set(map(str, range(1, 27)))
        
        for i in range(len(s)):
            curr = (s[i] in correct) * prev1
            if i > 0:
                curr += (s[i-1:i+1] in correct) * prev2
            prev2, prev1 = prev1, curr
        return curr
