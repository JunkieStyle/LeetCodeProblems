from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        store_index = 0
        
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
