class Solution:
    def jump(self, nums: List[int]) -> int:
        
        start, end = 0, 1
        count = 0
        while end < len(nums):
            start, end = end, max(nums[i] + i + 1 for i in range(start, end))
            count += 1
            
        return count 