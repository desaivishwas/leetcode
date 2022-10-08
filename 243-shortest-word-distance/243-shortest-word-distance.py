class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        right = -sys.maxsize
        left = sys.maxsize
        diff = sys.maxsize
        for i, word in enumerate(wordsDict):
            if word == word1:
                left = i
            elif word == word2:
                right = i
                
            diff = min(diff, abs(left - right))
        
        return diff