from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        arr = sorted(nums)
        result = None
        for i in range(0, len(arr) - 2):
            j = i + 1
            k = len(arr) - 1
            while j != k:
                score = arr[i] + arr[j] + arr[k]
                if score == target:
                    return score
                elif score < target:
                    j += 1
                else:
                    k -= 1
                if result is None or (abs(score - target) < abs(result - target)):
                    result = score
        return result
