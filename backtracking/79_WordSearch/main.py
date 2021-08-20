
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i, j, board, word):
                    return True
        return False
        
    def dfs(self, i, j, board, word):
        if not word:
            return True
        
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and word[0] == board[i][j]:
            board[i][j] = "#"
            
            if any([
                self.dfs(i+1, j, board, word[1:]),
                self.dfs(i, j+1, board, word[1:]),
                self.dfs(i-1, j, board, word[1:]),
                self.dfs(i, j-1, board, word[1:])
            ]):
                return True
            
            board[i][j] = word[0]
        
        return False
