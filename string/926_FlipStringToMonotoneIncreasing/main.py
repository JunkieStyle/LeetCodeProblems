class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flips = len([v for v in s if v == "0"])
        min_flips = flips
        
        for c in s:
            flips -= int(c == "0")
            flips += int(c == "1")
            min_flips = min(flips, min_flips)

        return min_flips
