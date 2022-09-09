class Solution:
    def firstUniqChar(self, s: str) -> int:
        char = {}
        
        for c in s:
            char[c] = char.get(c,0) + 1
            
        for index, c in enumerate(s):
            if char[c] == 1:
                return index
        return -1
            
        
        
#         for c in s:
#             if c in char:
#                 char[c] += 1
#             else:
#                 char[c] = 1
                
                
#         for i, ch in enumerate(s):
#             if char[ch] == 1:
#                 return i
#         return -1