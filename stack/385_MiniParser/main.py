class NestedInteger:
    pass


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = [NestedInteger()]
        i = 0
        while i < len(s):
            if s[i] == "[":
                ni = NestedInteger()
                stack[-1].add(ni)
                stack.append(ni)
            elif s[i] == "]":
                stack.pop()
            elif s[i] == ",":
                pass
            else:
                j = i
                while j < len(s) and (s[j].isdigit() or s[j] == "-"):
                    j += 1
                ni = NestedInteger(int(s[i: j]))
                stack[-1].add(ni)
                i = j - 1
            i += 1
        
        return stack[0].getList()[0]
