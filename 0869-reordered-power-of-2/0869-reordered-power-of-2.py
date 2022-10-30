class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = list(str(n))
        digits.sort()
        
        
        for i in range(32):
            num = 2**i
            
            lookup = list(str(num))
            lookup.sort()
            
            if digits == lookup:
                return True
            
        return False
