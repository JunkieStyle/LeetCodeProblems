from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return nums[0] if nums[0] < nums[1] else nums[1]

        mid = len(nums) // 2
        if nums[mid - 1] > nums[mid] < nums[mid + 1]:
            return nums[mid]
        elif nums[-1] < nums[mid] > nums[0]:
            return self.findMin(nums[mid:])
        else:
            return self.findMin(nums[:mid + 1])
