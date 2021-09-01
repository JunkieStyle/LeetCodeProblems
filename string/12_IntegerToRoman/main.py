class Solution:
    def intToRoman(self, num: int) -> str:
        romans = [
            ["I", "V", "X"],
            ["X", "L", "C"],
            ["C", "D", "M"],
            ["M"]
        ]
        
        def to_roman(p, r):
            if (p + 1) % 5 == 0:
                return r[0] + r[(p + 1) // 5]
            else:
                return r[p // 5] * (p // 5) + r[0] * (p % 5)

        c = 0
        result = ""
        while num:
            num, p = num // 10, num % 10
            result = to_roman(p, romans[c]) + result
            c = (c + 1) % len(romans)
        return result


    def intToRoman2(self, num):
        dict = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ""
        for letter, n in zip(dict, nums):
            result += letter * int(num / n)
            num %= n
        return result
