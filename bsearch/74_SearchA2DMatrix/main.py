import bisect
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = bisect.bisect([row[0] for row in matrix], target) - 1
        if i < 0:
            return False

        j = bisect.bisect(matrix[i], target) - 1
        if j < 0:
            return False

        return matrix[i][j] == target

