class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        while n != 1:
            cache.add(n)
            n = self.sum_of_digits(n)
            if n in cache:
                return False
        return True

    # sum(int(v) ** 2 for v on str(n))
    def sum_of_digits(self, n):
        res = 0
        while n:
            res += (n % 10) ** 2
            n //= 10
        return res
