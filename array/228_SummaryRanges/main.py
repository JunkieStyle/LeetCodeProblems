from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        start = 0
        for i in range(0, len(nums)):
            if i > 0 and nums[i] != nums[i - 1] + 1:
                ranges.append((start, i - 1))
                start = i
            
            if i == (len(nums) - 1):
                ranges.append((start, i))
            
        return [str(nums[i]) if i == j else f"{nums[i]}->{nums[j]}" for i, j in ranges]
