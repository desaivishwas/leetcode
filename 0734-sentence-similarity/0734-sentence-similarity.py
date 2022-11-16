class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        
        if len(sentence1) != len(sentence2):
            return False
        
        def check(a,b):
            return [a,b] in similarPairs or [b,a] in similarPairs or len(a) == len(b)
        
        for i in range(len(sentence1)):
            if not check(sentence1[i], sentence2[i]):
                return False
            
        return True