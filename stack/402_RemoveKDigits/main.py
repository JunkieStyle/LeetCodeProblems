class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for i in range(len(num)):
            while stack and stack[-1] > num[i] and k > 0:
                stack.pop()
                k -= 1
            stack.append(num[i])
            
                    
        while k:
            stack.pop()
            k -= 1

        return "".join(stack).lstrip("0") or "0"
