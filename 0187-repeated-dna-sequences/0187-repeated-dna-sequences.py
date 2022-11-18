class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l = 0
        r = 9
        seen = set()
        sub = set()
        while r < len(s):
            if s[l:r+1] not in seen:
                seen.add(s[l:r+1])
            else:
                sub.add(s[l:r+1])
            l += 1
            r += 1
        return list(sub)



