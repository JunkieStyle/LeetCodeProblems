from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0
        for i in range(len(nums)):
            res = max(prev2 + nums[i], prev1)
            prev1, prev2 = res, prev1
        return prev1
