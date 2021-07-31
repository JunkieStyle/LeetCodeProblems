class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        p = self.prefix(needle)  #  O(m)
        i = j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                j += 1
                i += 1
            elif j == 0:
                i += 1
            else:
                j = p[j-1]

        if j == len(needle):
            return i - j
                
        return -1 


    def prefix(self, s: str) -> list[int]:
        p = [0] * len(s)
        for i in range(1, len(s)):
            k = p[i - 1]

            while k > 0 and s[i] != s[k]:
                k = p[k - 1]
            
            if s[i] == s[k]:
                k += 1

            p[i] = k
        return p

s = Solution()
assert s.strStr("acar", "car") == 1
assert s.strStr("carcar", "car") == 0
assert s.strStr("carcar", "") == 0
assert s.strStr("", "") == 0
assert s.strStr("acar", "rcar") == -1
assert s.strStr("mississippi", "issip") == 4
