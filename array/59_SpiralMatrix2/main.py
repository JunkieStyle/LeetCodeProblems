from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        i = j = 0
        di, dj = 0, 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        for k in range(n * n):
            matrix[i][j] = k + 1
            if  not (0 <= (i + di) < n) or not (0 <= (j + dj) < n) or matrix[i + di][j + dj] != 0:
                di, dj = dj, -di
            i += di
            j += dj
            
        return matrix
