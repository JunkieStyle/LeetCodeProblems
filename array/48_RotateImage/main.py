from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for k1 in range(len(matrix) // 2):
            m = len(matrix) - 2 * k1 - 1
            for k2 in range(m):                
                (
                    matrix[k1][k1 + k2],
                    matrix[k1 + k2][k1 + m],
                    matrix[k1 + m][k1 + m - k2],
                    matrix[k1 + m - k2][k1]
                ) = (
                    matrix[k1 + m - k2][k1], 
                    matrix[k1][k1 + k2],
                    matrix[k1 + k2][k1 + m],
                    matrix[k1 + m][k1 + m - k2]
                )
