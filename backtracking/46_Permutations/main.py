from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        self.permute_helper(nums, [], result)
        return result

    def permute_helper(self, nums, path, result):
        if len(nums) == 0:
            result.append(path)
        else:
            for i in range(len(nums)):
                self.permute_helper(nums[:i] + nums[i+1:], path + [nums[i]], result)

