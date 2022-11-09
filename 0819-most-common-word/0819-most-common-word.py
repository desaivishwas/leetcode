class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # if len(paragraph) == 1 and len(banned) == 0:
        #     return paragraph
        d = {}
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        words = normalized_str.split()        
        for w in words:
            if w not in banned:
                d[w] = 1 + d.get(w, 0)
            
        
        return max(d.items(), key=operator.itemgetter(1))[0]

            
    