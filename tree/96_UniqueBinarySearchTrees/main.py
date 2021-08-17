class Solution:
    def numTrees(self, n: int) -> int:
        h = {1: 1, 0: 1}
        
        def inner(n):
            if n in h:
                return h[n]

            result = 0
            for i in range(0, n):
                result += inner(i) * inner(n - i - 1)
            h[n] = result
            return result
            
        return inner(n)
