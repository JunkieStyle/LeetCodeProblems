from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result =  max_ = min_ = nums[0]
        for i in range(1, len(nums)):
            candidates = [nums[i], max_ * nums[i], min_ * nums[i]]
            max_, min_ = max(candidates), min(candidates)
            result = max(result, max_, min_)
        return result
