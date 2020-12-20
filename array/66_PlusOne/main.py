from typing import List


class Solution:
    # specially not one liner solution
    def plusOne(self, digits: List[int]) -> List[int]:
        inc = True
        for i in range(len(digits), 0, -1):
            if not inc:
                break
            else:
                digits[i - 1] = (digits[i - 1] + inc) % 10
                inc = digits[i - 1] == 0

        if inc:
            digits = [1] + digits

        return digits

    def plusOne_oneliner(self, digits: List[int]) -> List[int]:
        return [int(v) for v in str(int(''.join(str(d) for d in digits)) + 1)]
