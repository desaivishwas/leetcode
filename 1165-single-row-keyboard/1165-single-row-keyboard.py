class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {char:idx for idx, char in enumerate(keyboard)}
        index = 0
        time = 0
        for char in word:  
                time += abs(index  - d[char])
                index = d[char]
        return time