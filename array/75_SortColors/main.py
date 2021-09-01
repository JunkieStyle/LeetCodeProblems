from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = j = 0
        k = len(nums) - 1
        
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            else:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1
