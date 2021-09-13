from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        result = len(text)
        for c in "balloon":
            result = min(counts[c] // 2 if c in "lo" else counts[c], result)
        return result
