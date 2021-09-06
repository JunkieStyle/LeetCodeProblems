from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        self.helper(s, 0, "", [])
        return result


    def helper(self, s, start, output, result):
        if len(s[start:]) == 0:
            result.append(output)
        elif s[start].isdigit():
            self.helper(s, start + 1, output + s[start], result)
        else:
            self.helper(s, start + 1, output + s[start].lower(), result)
            self.helper(s, start + 1, output + s[start].upper(), result)
