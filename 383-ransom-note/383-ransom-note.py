class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = Counter(magazine)
        for char in ransomNote:
            if char not in d or d[char] == 0:
                return False
            else:
                d[char] -= 1
                
                
        return True