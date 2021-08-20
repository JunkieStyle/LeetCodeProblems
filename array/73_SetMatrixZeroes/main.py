from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_col = False
        
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                is_col = True
                
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0 
                    matrix[0][j] = 0 
                    
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        if matrix[0][0] == 0:
            for j in range(0, len(matrix[0])):
                matrix[0][j] = 0
        
        if is_col:
            for i in range(0, len(matrix)):
                matrix[i][0] = 0
