from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for counter in range(0, 2 ** len(nums)):
            bits = format(counter, '{}b'.format(len(nums)))
            result.append([n for n, bit in zip(nums, bits) if bit == "1"])
        return result
