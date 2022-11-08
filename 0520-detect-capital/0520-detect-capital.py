class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        uc = 0
        for char in word:
            if char.isupper():
                uc += 1
                
        if uc == len(word) or uc == 0 or (uc == 1 and word[0].isupper()):
            return True
        else:
            return False