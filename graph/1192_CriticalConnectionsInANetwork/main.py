from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        neighbours = [[] for _ in range(n)]
        ranks = [i for i in range(n)]
        visited = [0] * n
        result = []
        
        for a, b in connections:
            neighbours[a].append(b) 
            neighbours[b].append(a)

        def dfs(v, p, depth):
            visited[v] = 1
            ranks[v] = depth

            for w in neighbours[v]:
                if w == p:
                    continue

                if not visited[w]:
                    dfs(w, v, depth + 1)  
                    
                ranks[v] = min(ranks[v], ranks[w])
                    
                if ranks[w] > depth:
                    result.append([v, w])                        

        dfs(0, None, 0)

        return result
