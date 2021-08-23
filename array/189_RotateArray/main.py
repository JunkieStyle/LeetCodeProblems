from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k == 0:
            return
        
        self.reverse(nums, 0, len(nums) - 1 - k)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)
    
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        
s = Solution()
nums = [1, 2, 3, 4, 5, 6]
s.rotate(nums, 2)
assert nums == [5, 6, 1, 2, 3, 4]
