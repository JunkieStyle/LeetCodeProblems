class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        result = area_a + area_b

        i1 = min(bx2, ax2) - max(bx1, ax1)
        i2 = min(by2, ay2) - max(by1, ay1)
        
        if i1 > 0 and i2 > 0:
            result -= i1 * i2

        return result
