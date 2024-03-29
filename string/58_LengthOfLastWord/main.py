class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        res = 0
        while i >= 0 and s[i] == " ": i -= 1
        while i >= 0 and s[i] != " ": 
            i -= 1
            res += 1
        return res
        
s = Solution()
val = "Hello World"
assert s.lengthOfLastWord(val) == len(val.strip().split(" ")[-1])
