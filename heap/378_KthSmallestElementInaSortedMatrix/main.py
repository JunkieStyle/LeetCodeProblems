import heapq


class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        i = j = counter = 0
        heap, seen = [], set()
        heapq.heappush(heap, (matrix[i][j], i, j))

        while counter < k:
            val, i, j = heapq.heappop(heap)
            seen.add((i, j))

            if j + 1 < n and (i == 0 or (i - 1, j + 1) in seen):
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))

            if i + 1 < n and (j == 0 or (i + 1, j - 1) in seen):
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))

            counter += 1
        
        return val


s = Solution()
print(s.kthSmallest([[1]], 1))
print(s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))