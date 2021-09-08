from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        hi = len(nums) - 1
        lo = 0
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
                
        return nums[lo]
