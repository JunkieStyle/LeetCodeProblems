import heapq


class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        heapq.heapify(heap)

        for i in range(n):
            heapq.heappush(heap, (matrix[i][0], i, 0))

        for _ in range(k):
            val, i, j = heapq.heappop(heap)
            if j + 1 < n:
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
 
        return val


s = Solution()
print(s.kthSmallest([[1]], 1))
print(s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))