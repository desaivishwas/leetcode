class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))
        visit = set()
        
        for num in nums:
            if num in visit:
                return True
            else:
                visit.add(num)
                
        return False