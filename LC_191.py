class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

        """ Another way"""
        # i  = 0
        # while n!= 0:
        #     i+=1
        #     n &= (n-1)
        # return i