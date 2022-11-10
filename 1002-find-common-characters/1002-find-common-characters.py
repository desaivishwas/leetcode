class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        chars = [0] * 26
        
        for s in words[0]:
            chars[ord(s) - 97] += 1
            
        for i in range(1, len(words)):
            curr = [0] * 26
            
            for s in words[i]:
                curr[ord(s) - 97] += 1
            
            for j in range(26):
                chars[j] = min(chars[j], curr[j])
        
        res = []
        for i in range(len(chars)):
            
            if chars[i] > 0:
                count = chars[i]
                
                while count > 0:
                    res.append(chr(i+97))
                    count -= 1
        return res