class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = 0        
        for i in range(min(len(s) for s in strs)):
            if not len(set(s[i] for s in strs)) == 1:
                break
            res += 1
            
        return strs[0][:res]
