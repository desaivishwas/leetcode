class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        twos = 1
        ones = 1
        
        for i in range(1, len(s)):
            curr = 0
            if s[i] != '0':
                curr = ones
            
            digit = int(s[i-1:i+1])
            if digit >= 10 and digit <= 26:
                curr += twos
                
            twos = ones
            ones = curr
            
        return ones