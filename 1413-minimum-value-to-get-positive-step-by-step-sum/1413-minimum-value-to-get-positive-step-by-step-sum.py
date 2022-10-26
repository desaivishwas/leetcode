class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_start = 1
        startValue = 1
        for num in nums:
            startValue += num
            if startValue < 1:
                min_start += -startValue + 1
                startValue = 1
                
        return min_start