from itertools import groupby

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        return "".join(str(len(list(items))) + key for key, items in groupby(self.countAndSay(n-1)))


s = Solution()
assert s.countAndSay(2) == "11"
assert s.countAndSay(4) == "1211"
assert s.countAndSay(5) == "111221"
assert s.countAndSay(6) == "312211"