from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        result = []
        up, down = 0, n - 1 
        left, right = 0, m - 1
        
        while len(result) < n * m:
            for j in range(left, right + 1):
                result.append(matrix[up][j])
            
            for i in range(up + 1, down + 1):
                result.append(matrix[i][right])
                
            if up != down:
                for j in range(right - 1, left - 1, -1):
                    result.append(matrix[down][j])
            
            if left != right:
                for i in range(down - 1, up, -1):
                    result.append(matrix[i][left])

            up += 1
            down -= 1
            left += 1
            right -= 1
        
        return result
