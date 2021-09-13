from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def norm_rev(rev):
            rev = rev.lstrip("0")
            return int(rev) if rev else 0
        
        for rev1, rev2 in zip_longest(version1.split("."), version2.split("."), fillvalue="0"):
            rev1 = norm_rev(rev1)
            rev2 = norm_rev(rev2)
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
            
        return 0
