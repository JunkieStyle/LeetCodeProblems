class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = ""
        extra = 0
        for i in range(0, max(len(a), len(b))):
            v = extra
            if i < len(a):
                v += int(a[len(a) - i - 1])
            if i < len(b):
                v += int(b[len(b) - i - 1])
            
            extra = v // 2
            c = str(v % 2) + c
        
        if extra:
            c = str(extra) + c

        return c

s = Solution()
print(s.addBinary("111", "1"))
print(s.addBinary("0", "0"))