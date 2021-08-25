from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        result = [0] * len(nums)
        
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                result[j - i]  = nums[i] ** 2
                i += 1
            else:        
                result[j - i]  = nums[j] ** 2
                j -= 1
        
        return result  
