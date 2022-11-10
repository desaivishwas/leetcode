class Solution:
    def countLetters(self, s: str) -> int:
        res = 1
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            
            res += count
            
        return res