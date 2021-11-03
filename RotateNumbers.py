from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #creasting an extra array to store the resultant array         
        extra =  [0] * len(nums)
        for i in range(len(nums)):
            extra[(i + k)%len(nums)] = nums[i]
            
        for i in range(len(nums)):
            nums[i] = extra[i]