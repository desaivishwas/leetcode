class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for char in s:
            d[char] = 1 + d.get(char, 0)
            
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        
        return -1