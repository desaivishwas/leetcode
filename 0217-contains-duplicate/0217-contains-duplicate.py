class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        x = 2
        for num in nums:
            if counter[num] >= 2:
                return True
            
        return False
        