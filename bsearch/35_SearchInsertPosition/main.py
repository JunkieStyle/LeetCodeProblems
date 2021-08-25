import bisect
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1

        return i

    def searchInsert_buitin(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)

s = Solution()
assert s.searchInsert([1,3,5,6], 5) ==  s.searchInsert_buitin([1,3,5,6], 5)