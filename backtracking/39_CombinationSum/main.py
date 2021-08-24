from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtrack(candidates, target, [], result)
        return result

    def backtrack(self, candidates, target, path, result):
        if target == 0:
            result.append(path)
        elif target > 0:
            for i, item in enumerate(candidates):
                self.backtrack(candidates[i:], target - item, path + [item], result)     
