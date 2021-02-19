class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True] * (n - 2)

        for i in range(2, n):
            if not primes[i - 2]:
                continue
            j = i * i
            while j < n:
                primes[j - 2] = False
                j += i
        return sum(primes)
