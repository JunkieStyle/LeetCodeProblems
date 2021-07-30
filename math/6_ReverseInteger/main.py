class Solution:
    def reverse(self, x: int) -> int:
        result = int(str(abs(x))[::-1])
        return (-result if x < 0 else result) if result.bit_length() < 32 else 0

s = Solution()
assert s.reverse(-21) == -12
assert s.reverse(0) == 0
assert s.reverse(234) == 432
assert s.reverse(10) == 1
assert s.reverse(1534236469) == 0
