import functools
import operator

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        i, j = min(m, n), max(m, n)
        num = functools.reduce(operator.mul, range(j, i + j - 1), 1)
        while i - 1 > 1:
            num //= i - 1
            i -= 1
        return num
