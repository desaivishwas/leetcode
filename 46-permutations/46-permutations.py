class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            perms = self.permute(nums[0:i]+nums[i+1:])
            
            for perm in perms:
                perm.append(nums[i])
            
            res = [*res, *perms]
            
        return res