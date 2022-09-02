class Solution:
    def firstUniqChar(self, s: str) -> int:
        char = {}
        for c in s:
            if c in char:
                char[c] += 1
            else:
                char[c] = 1
                
                
        for i, ch in enumerate(s):
            if char[ch] == 1:
                return i
        return -1