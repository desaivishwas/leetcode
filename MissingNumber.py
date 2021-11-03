from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """ O(n) complexity"""
        # new = set(nums)
        # n = len(nums)+1
        # for x in range(n):
        #     if x not in new:
        #         return x
        
        """O(n2)"""
        n = len(nums)+1
        newList = [x for x in range(n)]
        for i in range(len(newList)):
            if i not in nums:
                return i
                
        