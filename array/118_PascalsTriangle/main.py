from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        result = self.generate(numRows - 1)
        new_row = [1] * numRows  # [1, 1, 1]

        for i in range(0, numRows - 2):
            new_row[i + 1] = result[-1][i] + result[-1][i + 1]
        result.append(new_row)
        return result
