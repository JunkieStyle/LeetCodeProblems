class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i + j] += int(num1[-(i+1)]) * int(num2[-(j+1)])
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
        
        return "".join(map(str, res[::-1])).lstrip("0") or "0"
