from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        
        while i < j:
            if (numbers[j] + numbers[i]) > target: j -= 1
            elif (numbers[j] + numbers[i]) < target: i += 1
            else: return [i + 1, j + 1]
