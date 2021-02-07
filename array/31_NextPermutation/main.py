from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                k = i
                for j in range(i, len(nums)):
                    if nums[k] >= nums[j] > nums[i - 1]:
                        k = j
                nums[i - 1], nums[k] = nums[k], nums[i - 1]

                l, r = i, len(nums) - 1
                while l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1

                return

        nums.sort()
