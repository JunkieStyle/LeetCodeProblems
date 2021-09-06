from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.combine_helper(1, n + 1, k, [], result)
        return result

    def combine_helper(self, start, end, k, path, result):
        if k == 0:
            result.append(path)
        elif k > 0:
            while start + k <= end:
                self.combine_helper(start + 1, end, k - 1, path + [start], result)
                start += 1

s = Solution()
print(s.combine(3, 2))            
