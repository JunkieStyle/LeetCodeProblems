class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lo = 0
        hi = m * n

        def enough(x):
            count = 0
            for i in range(1, m + 1):
                count += min(x // i, n)
            return count >= k
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if enough(mid):
                hi = mid
            else:
                lo = mid + 1 

        return lo
