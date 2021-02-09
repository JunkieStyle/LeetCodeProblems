from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        result = 0
        for v in nums:
            if v - 1 not in nums:
                size = 1
                while v + size in nums:
                    size += 1
                result = max(result, size)
        return result
