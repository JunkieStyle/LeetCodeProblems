class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for t in tokens[::-1]:
            if t in "+-*/":
                stack.append(t)
            else:
                n1 = int(t)
                while stack and isinstance(stack[-1], int):
                    n2 = stack.pop()
                    op = stack.pop()
                    if op == "+": n1 += n2
                    elif op == "-": n1 -= n2
                    elif op == "*": n1 *= n2
                    elif op == "/": n1 = int(n1 / n2)
                stack.append(n1)
                        
        return stack[0]
