class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k>1:
            return ''.join(sorted(s))    
        
        if len(s) == 1:
            return s
        dummy = s
        for i in range(len(s)):         
            s = s[1:] + s[0]
            dummy = min(dummy,s)         
        return dummy