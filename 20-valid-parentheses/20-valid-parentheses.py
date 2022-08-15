class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(', '}':'{', ']':'['}
        stack = []
        
        for p in s:
            if p in d:
                peek = stack.pop() if stack else '#'
                if d[p] != peek:
                    return False
            else:
                stack.append(p)
                
        return not stack
                    
        
        
        
        
        
        
        
#         s1 = []
#         d = {")": "(", "}": "{", "]": "["}
#         for char in s:
#             if char in d:
#                 top = s1.pop() if s1 else '#'
#                 if d[char] != top:
#                     return False
#             else:
#                 s1.append(char)
            
            
#         return not s1
        