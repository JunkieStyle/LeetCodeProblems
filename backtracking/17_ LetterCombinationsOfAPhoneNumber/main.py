from typing import List


class Solution:
    m = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        prev = self.letterCombinations(digits[1:])
        if not prev:
            prev = [""]
    
        return [letter + c for c in prev for letter in self.m[int(digits[0])]]
