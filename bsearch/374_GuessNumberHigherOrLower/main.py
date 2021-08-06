# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        i = 1
        j = n
        while i < j:
            mid = (i + j) // 2
            guess_mid = guess(mid)
            
            if guess_mid == 0:
                return mid
            elif guess_mid == -1:
                j = mid
            elif guess_mid == 1:
                i = mid + 1
        return i
