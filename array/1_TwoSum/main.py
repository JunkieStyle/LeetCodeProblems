from typing import List


# array
# hash table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saved = {}
        for i, n in enumerate(nums):
            if saved.get(target - n, None) is not None:
                return [saved[target - n], i]
            saved[n] = i
        return []