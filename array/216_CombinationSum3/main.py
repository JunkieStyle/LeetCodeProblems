from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        nums = list(range(1, 10))
        self.dfs(nums, k, n, [], result)
        return result

    def dfs(self, nums, k, n, cur, result):
        if k == 0 and n == 0:
            result.append(cur)
            return

        if k < 0 or n < 0:
            return

        for i in range(len(nums)):
            self.dfs(nums[i + 1:], k - 1, n - nums[i], [nums[i]] + cur, result)
