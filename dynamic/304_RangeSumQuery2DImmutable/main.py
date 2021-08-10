class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        n, m = len(matrix), len(matrix[0])
        
        self.sums = [[matrix[i][j] for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i > 0: self.sums[i][j] += self.sums[i-1][j]
                if j > 0: self.sums[i][j] += self.sums[i][j-1]
                if i > 0 and j > 0: self.sums[i][j] -= self.sums[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.sums[row2][col2]
        
        if row1 > 0: result -= self.sums[row1-1][col2]
        if col1 > 0: result -= self.sums[row2][col1-1]
        if row1 > 0 and col1 > 0: result += self.sums[row1-1][col1-1]
            
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)