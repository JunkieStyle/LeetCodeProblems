class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c == "(":
                stack.append(")")
            elif c == "[":
                stack.append("]")
            elif c == "{":
                stack.append("}")
            elif c in ")}]":
                if not len(stack):
                    return False
                if c != stack.pop():
                    return False

        return len(stack) == 0


s = Solution()
assert s.isValid("")
assert s.isValid("([])")
assert s.isValid(")") is False
assert s.isValid("([)]") is False