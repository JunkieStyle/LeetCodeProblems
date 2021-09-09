from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines = set(tuple(mine) for mine in mines)
        dp = [[0] * n for _ in range(n)]
        result = 0
        
        for row in range(0, n):
            count = 0
            for col in range(0, n):
                count = count + 1 if (row, col) not in mines else 0
                dp[row][col] = count
                
            count = 0
            for col in range(n - 1, -1, -1):
                count = count + 1 if (row, col) not in mines else 0
                dp[row][col] = min(count, dp[row][col])
                
        for col in range(0, n):
            count = 0
            for row in range(0, n):
                count = count + 1 if (row, col) not in mines else 0
                dp[row][col] = min(count, dp[row][col])
                
            count = 0
            for row in range(n - 1, -1, -1):
                count = count + 1 if (row, col) not in mines else 0
                dp[row][col] = min(count, dp[row][col])
                result = max(result, dp[row][col])
                
        return result
