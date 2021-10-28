from heapq import heapify, heappush, heappushpop, nsmallest
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return nsmallest(k, points, key=lambda x: x[0]**2 + x[1]**2)
    
    def kClosest_2(self, points, k):
        h = []
        heapify(h)

        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            heappush(h, (-dist, point)) if len(h) < k else heappushpop(h, (-dist, point))
        
        return [v[1] for v in h]

    def kClosest_3(self, points, k):
        self.sort(points, 0, len(points), k, key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:k]
    
    def sort(self, points, l, r, k, key=lambda x: x):      
        if l < r:
            p = self.partition_hoare(points, l, r, key=key)            
            if p == k:
                return
            elif p < k: 
                self.sort(points, p + 1, r, k, key=key)
            else:
                self.sort(points, l, p, k, key=key)


    def partition_lomuto(self, arr, l, r, key=lambda x: x):
        pivot = arr[r - 1]
        a = l
        for i in range(l, r):
            if key(arr[i]) < key(pivot):
                arr[a], arr[i] = arr[i], arr[a]
                a += 1

        arr[a], arr[r - 1] = arr[r - 1], arr[a]
        return a 

    def partition_hoare(self, arr, l, r, key=lambda x: x):
        i = l + 1
        j = r - 1
        pivot = arr[l]

        while i <= j:
            if key(arr[i]) < key(pivot):
                i += 1
            elif key(arr[j]) > key(pivot):
                j -= 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        
        arr[j], arr[l] = arr[l], arr[j]

        return j
