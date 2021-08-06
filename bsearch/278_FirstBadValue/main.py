def isBadVersion(v):
    pass


class Solution:
    def firstBadVersion(self, n):
        i = 1
        j = n
        
        while i < j:
            middle = (i + j) // 2
            if isBadVersion(middle):
                j = middle
            else:
                i = middle + 1
                
        return i
