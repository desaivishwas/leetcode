class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
        
        palindrome = list(palindrome)
        
        for i, letter in enumerate(palindrome[: len(palindrome) // 2]):
            if letter != 'a':
                palindrome[i] = 'a'
                return ''.join(palindrome)
            
        palindrome[-1] = 'b'
        return ''.join(palindrome)