class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for index, char in enumerate(s):
            if char not in d:
                if t[index] in d.values():
                    return False
                else:
                    d[char] = t[index]
            else:
                if d[char] != t[index]:
                    return False
        return True
        