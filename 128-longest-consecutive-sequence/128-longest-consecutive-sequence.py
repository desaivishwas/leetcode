class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 not in nums:
                length = 0
                while num in nums:
                    num = num + 1
                    length += 1
                max_len = max(max_len, length)
        return max_len
            
        