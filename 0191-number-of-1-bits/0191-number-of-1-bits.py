class Solution:
    
    def helper(self, n):
        res = ""
        while n != 0:
            res += str(n % 2)
            n = (n // 2)
        return res
        
    def hammingWeight(self, n: int) -> int:
        x = self.helper(n)
        return x.count("1")