from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        hi = len(nums) - 1
        lo = 0
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if mid == lo:
                return lo if nums[lo] > nums[hi] else hi
           
            elif nums[mid] > max(nums[mid - 1], nums[mid + 1]):
                return mid
            
            elif nums[mid - 1] > nums[mid]:
                hi = mid - 1
               
            elif nums[mid + 1] > nums[mid]:
                lo = mid + 1
            
        return lo
