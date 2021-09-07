from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [self.bsearch_left(nums, target)]
        return result + [self.bsearch_right(nums, target) - 1] if target in nums[result[0]:result[0] + 1] else [-1, -1]  
    
    def bsearch_left(self, nums, target):
        lo, hi = 0, len(nums)  
        while lo < hi: 
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
         
        return lo
               
    def bsearch_right(self, nums, target):
        lo, hi = 0, len(nums)
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return lo
