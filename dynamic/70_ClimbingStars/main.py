class Solution:
    def climbStairs(self, n: int) -> int:
        p1 = p2 = 1
        for _ in range(1, n):
            p1, p2 = p2 + p1, p1
        return p1
