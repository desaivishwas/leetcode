class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        lsum = 0
        for i in range(len(nums)):
            # calculate right sum wich toal - curr - leftsum
            rsum = total - nums[i] - lsum
            if lsum == rsum:
                return i 
            lsum += nums[i]
            
        return -1