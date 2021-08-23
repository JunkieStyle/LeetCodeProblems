from collections import Counter
from functools import reduce
import operator


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(reduce(operator.xor, (ord(c) for c in s + t)))

    def findTheDifference2(self, s: str, t: str) -> str:
        return (Counter(t) - Counter(s)).popitem()[0]
