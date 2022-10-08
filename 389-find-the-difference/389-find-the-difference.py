class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1, t1 = 0, 0
        for c in s:
            s1 += ord(c)
            
        for d in t:
            t1 += ord(d)
            
        return chr(t1 - s1)