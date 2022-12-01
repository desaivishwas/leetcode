class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) // 2
        
        a = s[:mid]
        b = s[mid:]
        
        vowels = "aeiouAEIOU"
        countA, countB = 0, 0
        for char in a:
            if char in vowels:
                countA += 1
                
        for char in b:
            if char in vowels:
                countB += 1
                
                
        return countA == countB