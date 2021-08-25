import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(math.sqrt(c))

        while a <= b:
            if (diff := a ** 2 + b ** 2 - c) == 0:
                return True
            elif diff > 0:
                b -= 1
            else:
                a += 1
    
        return False
