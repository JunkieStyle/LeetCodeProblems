import string


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
    
        while columnNumber:
            columnNumber -= 1
            columnNumber, rem = columnNumber // 26, columnNumber % 26
            result = string.ascii_uppercase[rem] + result
            
        return result
