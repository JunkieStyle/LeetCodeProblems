class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        while n:
            k = n & (n - 1)
            result += 1 << 32 - (n - k).bit_length()
            n = k
        
        return result
