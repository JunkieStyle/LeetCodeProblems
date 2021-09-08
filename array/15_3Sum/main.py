from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                continue
                          
            lo = i + 1
            hi = len(nums) - 1
            
            while lo < hi:
                if nums[lo] + nums[hi] == -nums[i]:
                    result.add((nums[i], nums[lo], nums[hi]))
                    lo += 1
                    hi -= 1
                elif nums[lo] + nums[hi] < -nums[i]:
                    lo += 1
                else:
                    hi -= 1
           
        return list(result)
    