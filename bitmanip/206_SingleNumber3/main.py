import operator
from typing import List
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = reduce(operator.xor, nums)
        diff = xor & -xor
        n = reduce(operator.xor, filter(lambda x: x & diff, nums))
        return [n, xor ^ n]
