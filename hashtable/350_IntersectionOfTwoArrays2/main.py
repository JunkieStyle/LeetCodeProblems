from typing import List
from collections import Counter


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)

        result = []
        for v in nums2:
            if c[v]:
                result.append(v)
                c[v] -= 1
        return result
