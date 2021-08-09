import itertools

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        carry = 0
        for n1, n2 in itertools.zip_longest(num1[::-1], num2[::-1], fillvalue="0"):
            val = int(n1) + int(n2) + carry
            result.append(str(val % 10))
            carry = val // 10

        if carry:
            result.append("1")

        return "".join(result[::-1])
