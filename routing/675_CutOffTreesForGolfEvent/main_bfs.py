from collections import deque
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        paths = [[0, (0, 0)]]
        
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    paths.append([forest[i][j], (i, j)])
        
        paths.sort()
        
        result = 0
        for i in range(1, len(paths)):
            steps = self.bfs(forest, paths[i-1][1], paths[i][1])
            if steps == -1:
                return -1
            result += steps
            
        return result
    

    def bfs(self, forest, start, end):
        m, n = len(forest), len(forest[0])
        queue = deque([start])
        steps = 0
        seen = set()
        
        while queue:
            for _ in range(len(queue)):
                i, j = queue.pop()

                if (i, j) == end:
                    return steps

                seen.add((i, j))

                for di, dj in zip([1, -1, 0, 0], [0, 0, 1, -1]):
                    if (
                        (i + di, j + dj) not in seen and 
                        0 <= i + di < m and
                        0 <= j + dj < n and
                        forest[i + di][j + dj] > 0
                    ):
                        queue.appendleft((i + di, j + dj))
             
            steps += 1
            
        return -1