import itertools


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        prev = list(itertools.accumulate(grid[0]))

        for i in range(1, len(grid)):
            for j in range(0, len(grid[i])):
                prev[j] = grid[i][j] + (min(prev[j-1], prev[j]) if j > 0 else prev[j])

        return prev[-1]
