from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        result = None
        for num in nums:
            if counter == 0:
                result = num
                counter += 1
            elif num == result:
                counter += 1
            else:
                counter -= 1
        return result
