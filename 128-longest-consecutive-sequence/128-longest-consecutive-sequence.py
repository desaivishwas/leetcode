class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_count = 0
        for elem in nums:
            if elem - 1 not in nums:
                length = 0
                while elem in nums:
                    elem = elem+1
                    length+=1
                max_count = max(max_count, length)
        return max_count
            
        