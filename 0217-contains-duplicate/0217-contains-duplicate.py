class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visit = set(nums)
        
        return len(visit) < len(nums)
#         counter = Counter(nums)
#         x = 2
#         for num in nums:
#             if counter[num] >= 2:
#                 return True
            
#         return False
        