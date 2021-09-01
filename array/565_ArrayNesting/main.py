from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        seen = set()
        result = 0
        
        for i in range(len(nums)):
            res = 0
            while nums[i] not in seen:
                seen.add(nums[i])
                i = nums[i]
                res += 1
                
            result = max(res, result)
            
        return result
