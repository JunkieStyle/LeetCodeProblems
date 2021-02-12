from typing import List


class Solution:
    def bsearch(self, arr, target, left):
        lo = 0
        hi = len(arr)

        while lo != hi:
            mid = (hi + lo) // 2
            if arr[mid] > target or (arr[mid] == target and left):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = self.bsearch(nums, target, left=True)
        if lo == len(nums) or nums[lo] != target:
            return [-1, -1]

        return [lo,  self.bsearch(nums, target, left=False) - 1]