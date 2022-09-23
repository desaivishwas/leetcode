class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
        
        p =  list(palindrome)
        for i, letter in enumerate(p[: len(p)//2]):
            if letter != 'a':
                p[i] = 'a'
                return ''.join(p)
        
        p[-1] = 'b'
        return ''.join(p)