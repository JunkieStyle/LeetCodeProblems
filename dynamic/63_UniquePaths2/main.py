class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                else:
                    if i > 0:
                        obstacleGrid[i][j] += obstacleGrid[i-1][j]
                    if j > 0:
                        obstacleGrid[i][j] += obstacleGrid[i][j-1]
                    if not i and not j:
                        obstacleGrid[i][j] = -1
        
        return -obstacleGrid[-1][-1]
