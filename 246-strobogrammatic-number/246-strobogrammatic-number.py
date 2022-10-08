class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = {"0":"0", "1":"1", "6":"9", "9":"6", "8":"8"}
    
        res = ""
        for c in num:
            if c not in d:
                return False
            res += d[c]
        return num == res[::-1]
        