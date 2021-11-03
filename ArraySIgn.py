from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
     
        if 0 in nums:
            return 0
        product = 1
        for num in nums:
            if num < 0:
                product = -product
            
        return product
            
        