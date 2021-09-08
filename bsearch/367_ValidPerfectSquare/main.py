class Solution:
    def isPerfectSquare__newton(self, num: int) -> bool:
        r = num
        while r*r > num:
            r = (r + num // r) >> 1
        return r*r == num
