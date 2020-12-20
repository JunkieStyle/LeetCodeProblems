from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        cur_sum = 0
        left = 0
        result = 0
        for right in range(0, len(nums)):
            cur_sum += nums[right]
            while cur_sum >= s:
                result = min(result, 1 + right - left) if result else right - left + 1
                cur_sum -= nums[left]
                left += 1

        return result
