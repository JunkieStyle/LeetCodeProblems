class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        result = 0
        start = end = 0
        for i in range(len(s)):
            if s[i] in h and start <= h[s[i]]:
                result = max(result, end - start)
                start = h[s[i]] + 1

            h[s[i]] = i
            end = i + 1
            
        return max(result,  end - start)
