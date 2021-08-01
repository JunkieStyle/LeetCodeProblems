class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return [""]
        
        result = []
        for i in range(0, n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n - i - 1):
                    result.append(f"({left}){right}")
                    
        return result

