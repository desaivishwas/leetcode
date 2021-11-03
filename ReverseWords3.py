class Solution:
    def reverseWords(self, s: str) -> str:
        # split the strings
        s = s.split()
        for i in range(len(s)):
            # reverse each substring
            s[i] = s[i][::-1]
            
        return " ".join(s)
        