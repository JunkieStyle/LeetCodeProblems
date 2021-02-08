from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1

        mid = len(nums) // 2
        if nums[mid - 1] < nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid - 1] > nums[mid] > nums[mid + 1]:
            return self.findPeakElement(nums[:mid])
        else:
            return self.findPeakElement(nums[mid + 1:]) + mid + 1
