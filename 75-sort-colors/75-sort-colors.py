class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        for c in (0, 1, 2):
            for i in range(start, len(nums)):
                if nums[i] == c:
                    nums[i], nums[start] = nums[start], nums[i]
                    start += 1
                    
                    
        