class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = maxTotal = nums[0]
        
        for num in nums[1:]:
            total = max(num, total + num)
            maxTotal = max(maxTotal, total)
            
        return maxTotal