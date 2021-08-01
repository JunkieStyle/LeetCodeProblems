
import operator

class Solution:
    def calculate(self, s: str) -> int:        
        sign = "+"
        stack = []
        num = 0
        
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in set(["+-/*"]) or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(num * stack.pop())
                elif sign == "/":
                     stack.append(int(stack.pop() / num))
                num = 0
                sign = s[i]
                
        return sum(stack)
                

