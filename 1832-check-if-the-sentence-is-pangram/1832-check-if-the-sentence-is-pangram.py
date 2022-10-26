class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = [False] * 26
        
        for char in sentence:
            alpha[ord(char) - ord('a')] = True
            
        return all(alpha)