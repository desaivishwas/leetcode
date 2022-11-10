class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        idx = 0
        nlen, tlen = len(name), len(typed)
        
        for i, char in enumerate(typed):
            if idx < nlen and name[idx] == char:
                idx += 1
                
            elif i == 0 or typed[i] != typed[i-1]:
                return False
            
        return idx == nlen
        
        