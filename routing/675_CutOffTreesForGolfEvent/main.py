# Headlocks algorithm

from typing import List
from collections import deque


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])

        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], (i, j)))

        trees.sort()

        # Check if trees are reachable
        queue = deque([(0, 0)])
        reachable = set()
        while queue:
            i, j = queue.pop()
            if (
                0 <= i < m and
                0 <= j < n and
                forest[i][j] > 0 and
                (i, j) not in reachable
            ):
                reachable.add((i, j))
                for di, dj in zip((1, -1, 0, 0), (0, 0, 1, -1)): 
                    queue.appendleft((i + di, j + dj))
        
        for tree in trees:
            if tree[1] not in reachable:
                return -1

        # accumulating the result 
        result = 0
        for i in range(1, [(0, (0, 0))] + trees):
            result += self.distance(forest, tree[i-1][1], tree[i][1]) 

        return result


    # Headlock algorithm
    def distance(self, forest, source, target):
        visited = set()
        cur, fut = [source], []
        detour = 0

        def manhatten(source, target):
            return abs(source[0] - target[0]) + abs(source[1] - target[1]) 

        while True:
            if not cur: 
                cur = fut
                fut = []
                detour += 1

            while cur:
                i, j = cur.pop()
                visited.add((i, j))

                if (i, j) == target:
                    return manhatten(source, target) + 2 * detour

                for di, dj in zip((1, -1, 0, 0), (0, 0, 1, -1)):
                    if (
                        0 <= i + di < len(forest) and
                        0 <= j + dj < len(forest[0]) and 
                        forest[i + di][j + dj] > 0 and
                        (i + di, j + dj) not in visited
                    ):
                        if manhatten((i, j), target) > manhatten((i + di, j + dj), target):
                            cur.append((i + di, j + dj))
                        else:
                            fut.append((i + di, j + dj))
