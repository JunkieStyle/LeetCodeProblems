from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        result = triangle[-1][:]
        for row in triangle[-2::-1]:
            for i in range(len(row)):
                result[i] = min(result[i], result[i + 1]) + row[i]
        return result[0]
