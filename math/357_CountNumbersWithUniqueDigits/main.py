from operator import mul
from functools import reduce


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n < 2:
            return 10 ** n
        
        return (
            self.countNumbersWithUniqueDigits(n - 1) + 
            reduce(mul, [9 - i + 2 for i in range(2, n + 1)], 9)
        )
